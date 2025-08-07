"""
CulturaBuilder Web Backend
FastAPI server for CLI-Web bridge and real-time communication
"""

import asyncio
import json
import subprocess
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

# Import CulturaBuilder modules
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from setup.managers.metrics_manager import MetricsManager
from setup.managers.settings_manager import SettingsManager


class CommandRequest(BaseModel):
    """Command execution request model"""
    command: str
    flags: List[str] = []
    context: Dict[str, Any] = {}


class CommandResponse(BaseModel):
    """Command execution response model"""
    command: str
    output: str
    error: Optional[str] = None
    exit_code: int
    duration: float
    metrics: Dict[str, Any] = {}
    visualization: Optional[Dict[str, Any]] = None


class AIQuery(BaseModel):
    """AI assistant query model"""
    query: str
    language: str = "pt-BR"
    context: Dict[str, Any] = {}


class CLIBridge:
    """Bridge between Web UI and CLI"""
    
    def __init__(self, install_dir: Path = Path.home() / ".culturabuilder"):
        self.install_dir = install_dir
        self.metrics_manager = MetricsManager(install_dir)
        self.settings_manager = SettingsManager(install_dir)
        self.active_sessions: Dict[str, WebSocket] = {}
        self.command_history: List[Dict[str, Any]] = []
    
    async def execute_command(self, command: str, flags: List[str] = None) -> CommandResponse:
        """Execute a CLI command and return structured response"""
        start_time = time.time()
        
        # Build full command
        full_command = ["culturabuilder", command]
        if flags:
            full_command.extend(flags)
        
        try:
            # Execute command
            result = subprocess.run(
                full_command,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            duration = time.time() - start_time
            
            # Record metrics
            self.metrics_manager.record_command(
                command=command,
                flags=flags,
                success=(result.returncode == 0),
                duration=duration
            )
            
            # Create response
            response = CommandResponse(
                command=command,
                output=result.stdout,
                error=result.stderr if result.stderr else None,
                exit_code=result.returncode,
                duration=duration,
                metrics=self._extract_metrics(result.stdout),
                visualization=self._create_visualization(command, result.stdout)
            )
            
            # Add to history
            self.command_history.append({
                "timestamp": datetime.now().isoformat(),
                "command": command,
                "flags": flags,
                "success": result.returncode == 0,
                "duration": duration
            })
            
            return response
            
        except subprocess.TimeoutExpired:
            return CommandResponse(
                command=command,
                output="",
                error="Command timed out after 30 seconds",
                exit_code=-1,
                duration=30.0
            )
        except Exception as e:
            return CommandResponse(
                command=command,
                output="",
                error=str(e),
                exit_code=-1,
                duration=time.time() - start_time
            )
    
    async def preview_command(self, command: str) -> Dict[str, Any]:
        """Generate command preview without execution"""
        # Parse command
        parts = command.split()
        cmd_name = parts[0] if parts else ""
        flags = parts[1:] if len(parts) > 1 else []
        
        # Get command info
        command_info = self._get_command_info(cmd_name)
        
        return {
            "command": cmd_name,
            "flags": flags,
            "description": command_info.get("description", ""),
            "examples": command_info.get("examples", []),
            "expectedOutput": command_info.get("expectedOutput", ""),
            "risks": self._assess_command_risks(cmd_name, flags),
            "suggestions": self._get_command_suggestions(cmd_name)
        }
    
    async def get_suggestions(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get command suggestions based on context"""
        recent_commands = context.get("recentCommands", [])
        current_input = context.get("currentInput", "")
        
        suggestions = []
        
        # Based on recent commands
        if recent_commands:
            last_command = recent_commands[-1]
            suggestions.extend(self._get_next_command_suggestions(last_command))
        
        # Based on current input
        if current_input:
            suggestions.extend(self._get_autocomplete_suggestions(current_input))
        
        # Add AI-powered suggestions
        suggestions.extend(await self._get_ai_suggestions(context))
        
        return suggestions[:10]  # Limit to top 10
    
    def _extract_metrics(self, output: str) -> Dict[str, Any]:
        """Extract metrics from command output"""
        metrics = {
            "lines": len(output.split('\n')),
            "size": len(output),
            "hasErrors": "error" in output.lower() or "fail" in output.lower(),
            "hasWarnings": "warning" in output.lower()
        }
        return metrics
    
    def _create_visualization(self, command: str, output: str) -> Optional[Dict[str, Any]]:
        """Create visualization data based on command and output"""
        if "analyze" in command:
            return self._create_analysis_visualization(output)
        elif "metrics" in command:
            return self._create_metrics_visualization(output)
        elif "build" in command:
            return self._create_build_visualization(output)
        return None
    
    def _create_analysis_visualization(self, output: str) -> Dict[str, Any]:
        """Create visualization for analysis commands"""
        return {
            "type": "tree",
            "data": {
                "name": "Project Analysis",
                "children": [
                    {"name": "Code Quality", "value": 85},
                    {"name": "Performance", "value": 92},
                    {"name": "Security", "value": 78},
                    {"name": "Documentation", "value": 65}
                ]
            }
        }
    
    def _create_metrics_visualization(self, output: str) -> Dict[str, Any]:
        """Create visualization for metrics commands"""
        return {
            "type": "chart",
            "data": {
                "labels": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                "datasets": [{
                    "label": "Commands Executed",
                    "data": [12, 19, 15, 25, 22]
                }]
            }
        }
    
    def _create_build_visualization(self, output: str) -> Dict[str, Any]:
        """Create visualization for build commands"""
        return {
            "type": "progress",
            "data": {
                "steps": [
                    {"name": "Dependencies", "status": "completed"},
                    {"name": "Compilation", "status": "completed"},
                    {"name": "Optimization", "status": "in-progress"},
                    {"name": "Packaging", "status": "pending"}
                ]
            }
        }
    
    def _get_command_info(self, command: str) -> Dict[str, Any]:
        """Get information about a command"""
        commands_db = {
            "/cb:build": {
                "description": "Build and configure project components",
                "examples": [
                    "/cb:build --component frontend",
                    "/cb:build --all --optimize"
                ],
                "expectedOutput": "Build progress and success message"
            },
            "/cb:analyze": {
                "description": "Analyze project code and architecture",
                "examples": [
                    "/cb:analyze --scope file",
                    "/cb:analyze --deep --report"
                ],
                "expectedOutput": "Analysis report with insights"
            }
        }
        return commands_db.get(command, {})
    
    def _assess_command_risks(self, command: str, flags: List[str]) -> Dict[str, Any]:
        """Assess risks associated with a command"""
        risks = {
            "level": "low",
            "warnings": []
        }
        
        if "deploy" in command:
            risks["level"] = "high"
            risks["warnings"].append("This will deploy to production")
        
        if "--force" in flags:
            risks["level"] = "medium"
            risks["warnings"].append("Force flag will skip confirmations")
        
        if "delete" in command or "remove" in command:
            risks["level"] = "high"
            risks["warnings"].append("This action cannot be undone")
        
        return risks
    
    def _get_command_suggestions(self, command: str) -> List[str]:
        """Get suggestions for a command"""
        suggestions = []
        
        if "build" in command:
            suggestions = [
                "Consider using --optimize for production builds",
                "Use --verbose to see detailed output",
                "Add --clean to ensure fresh build"
            ]
        elif "analyze" in command:
            suggestions = [
                "Use --deep for comprehensive analysis",
                "Add --report to generate detailed report",
                "Consider --focus security for security analysis"
            ]
        
        return suggestions
    
    def _get_next_command_suggestions(self, last_command: str) -> List[Dict[str, Any]]:
        """Suggest next commands based on last command"""
        next_commands = []
        
        if "build" in last_command:
            next_commands = [
                {"command": "/cb:test", "reason": "Test the build"},
                {"command": "/cb:deploy", "reason": "Deploy to staging"}
            ]
        elif "analyze" in last_command:
            next_commands = [
                {"command": "/cb:improve", "reason": "Apply improvements"},
                {"command": "/cb:document", "reason": "Update documentation"}
            ]
        
        return next_commands
    
    def _get_autocomplete_suggestions(self, input: str) -> List[Dict[str, Any]]:
        """Get autocomplete suggestions for input"""
        all_commands = [
            "/cb:build", "/cb:analyze", "/cb:deploy", "/cb:test",
            "/cb:improve", "/cb:document", "/cb:metrics"
        ]
        
        suggestions = []
        for cmd in all_commands:
            if cmd.startswith(input):
                suggestions.append({
                    "command": cmd,
                    "description": self._get_command_info(cmd).get("description", "")
                })
        
        return suggestions
    
    async def _get_ai_suggestions(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get AI-powered suggestions"""
        # Placeholder for AI integration
        return [
            {
                "command": "/cb:analyze --focus performance",
                "reason": "Recent builds show performance degradation",
                "confidence": 0.85
            }
        ]


class AIAssistant:
    """AI Assistant for natural language processing"""
    
    def __init__(self):
        self.context_history = []
    
    async def process_query(self, query: AIQuery) -> Dict[str, Any]:
        """Process natural language query"""
        # Analyze intent
        intent = self._analyze_intent(query.query, query.language)
        
        # Generate response based on intent
        if intent["type"] == "command_request":
            return await self._handle_command_request(intent, query)
        elif intent["type"] == "question":
            return await self._handle_question(intent, query)
        elif intent["type"] == "help":
            return await self._handle_help_request(intent, query)
        else:
            return await self._handle_general_query(intent, query)
    
    def _analyze_intent(self, query: str, language: str) -> Dict[str, Any]:
        """Analyze user intent from query"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["execute", "run", "executar", "rodar"]):
            return {"type": "command_request", "confidence": 0.9}
        elif "?" in query or any(word in query_lower for word in ["what", "how", "why", "o que", "como", "por que"]):
            return {"type": "question", "confidence": 0.85}
        elif any(word in query_lower for word in ["help", "ajuda", "tutorial"]):
            return {"type": "help", "confidence": 0.95}
        else:
            return {"type": "general", "confidence": 0.7}
    
    async def _handle_command_request(self, intent: Dict, query: AIQuery) -> Dict[str, Any]:
        """Handle command execution request"""
        # Extract command from natural language
        command = self._extract_command(query.query)
        
        return {
            "type": "command",
            "command": command,
            "explanation": f"I'll execute: {command}",
            "confidence": intent["confidence"]
        }
    
    async def _handle_question(self, intent: Dict, query: AIQuery) -> Dict[str, Any]:
        """Handle question"""
        # Generate answer based on knowledge base
        answer = self._generate_answer(query.query, query.language)
        
        return {
            "type": "answer",
            "answer": answer,
            "relatedCommands": self._find_related_commands(query.query),
            "confidence": intent["confidence"]
        }
    
    async def _handle_help_request(self, intent: Dict, query: AIQuery) -> Dict[str, Any]:
        """Handle help request"""
        topic = self._extract_help_topic(query.query)
        
        return {
            "type": "help",
            "topic": topic,
            "content": self._get_help_content(topic, query.language),
            "tutorials": self._get_related_tutorials(topic),
            "confidence": intent["confidence"]
        }
    
    async def _handle_general_query(self, intent: Dict, query: AIQuery) -> Dict[str, Any]:
        """Handle general query"""
        return {
            "type": "general",
            "response": "How can I help you with CulturaBuilder?",
            "suggestions": [
                "Try asking about specific commands",
                "Ask for help with a task",
                "Request a tutorial"
            ],
            "confidence": intent["confidence"]
        }
    
    def _extract_command(self, query: str) -> str:
        """Extract command from natural language"""
        # Simple extraction logic - can be enhanced with NLP
        if "build" in query.lower():
            return "/cb:build"
        elif "analyze" in query.lower() or "análise" in query.lower():
            return "/cb:analyze"
        elif "deploy" in query.lower():
            return "/cb:deploy"
        return "/cb:help"
    
    def _generate_answer(self, question: str, language: str) -> str:
        """Generate answer to question"""
        # Placeholder for knowledge base integration
        if language == "pt-BR":
            return "O CulturaBuilder é uma plataforma para construir cultura através de tecnologia."
        else:
            return "CulturaBuilder is a platform for building culture through technology."
    
    def _find_related_commands(self, query: str) -> List[str]:
        """Find commands related to query"""
        related = []
        
        if "build" in query.lower():
            related = ["/cb:build", "/cb:compile", "/cb:package"]
        elif "analyze" in query.lower():
            related = ["/cb:analyze", "/cb:inspect", "/cb:audit"]
        
        return related
    
    def _extract_help_topic(self, query: str) -> str:
        """Extract help topic from query"""
        if "command" in query.lower():
            return "commands"
        elif "tutorial" in query.lower():
            return "tutorials"
        elif "start" in query.lower() or "começar" in query.lower():
            return "getting-started"
        return "general"
    
    def _get_help_content(self, topic: str, language: str) -> str:
        """Get help content for topic"""
        help_db = {
            "commands": {
                "pt-BR": "Use /cb: seguido do nome do comando. Exemplo: /cb:build",
                "en-US": "Use /cb: followed by command name. Example: /cb:build"
            },
            "getting-started": {
                "pt-BR": "Bem-vindo! Comece com /cb:help para ver todos os comandos.",
                "en-US": "Welcome! Start with /cb:help to see all commands."
            }
        }
        return help_db.get(topic, {}).get(language, "Help content not found")
    
    def _get_related_tutorials(self, topic: str) -> List[Dict[str, str]]:
        """Get tutorials related to topic"""
        return [
            {"id": "basics", "title": "CulturaBuilder Basics"},
            {"id": "commands", "title": "Understanding Commands"},
            {"id": "advanced", "title": "Advanced Techniques"}
        ]


# FastAPI app with lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 CulturaBuilder Web Backend starting...")
    app.state.cli_bridge = CLIBridge()
    app.state.ai_assistant = AIAssistant()
    yield
    # Shutdown
    print("👋 CulturaBuilder Web Backend shutting down...")


app = FastAPI(
    title="CulturaBuilder Web API",
    description="Backend for CulturaBuilder Web Interface",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "CulturaBuilder Web API",
        "version": "1.0.0",
        "status": "running"
    }


@app.post("/api/command/execute")
async def execute_command(request: CommandRequest) -> CommandResponse:
    """Execute a CLI command"""
    cli_bridge = app.state.cli_bridge
    return await cli_bridge.execute_command(request.command, request.flags)


@app.post("/api/command/preview")
async def preview_command(request: CommandRequest) -> Dict[str, Any]:
    """Preview command without execution"""
    cli_bridge = app.state.cli_bridge
    return await cli_bridge.preview_command(request.command)


@app.post("/api/suggestions")
async def get_suggestions(context: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Get command suggestions"""
    cli_bridge = app.state.cli_bridge
    return await cli_bridge.get_suggestions(context)


@app.post("/api/ai/query")
async def ai_query(query: AIQuery) -> Dict[str, Any]:
    """Process AI assistant query"""
    ai_assistant = app.state.ai_assistant
    return await ai_assistant.process_query(query)


@app.get("/api/metrics/summary")
async def get_metrics_summary() -> Dict[str, Any]:
    """Get metrics summary"""
    cli_bridge = app.state.cli_bridge
    return cli_bridge.metrics_manager.get_summary_stats()


@app.get("/api/metrics/timeseries")
async def get_metrics_timeseries(period: str = "day") -> Dict[str, Any]:
    """Get time series metrics"""
    cli_bridge = app.state.cli_bridge
    return cli_bridge.metrics_manager.get_time_series_data(period)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication"""
    await websocket.accept()
    session_id = str(time.time())
    cli_bridge = app.state.cli_bridge
    cli_bridge.active_sessions[session_id] = websocket
    
    try:
        while True:
            data = await websocket.receive_json()
            
            if data["type"] == "execute":
                result = await cli_bridge.execute_command(
                    data["command"], 
                    data.get("flags", [])
                )
                await websocket.send_json({
                    "type": "result",
                    "data": result.dict()
                })
            
            elif data["type"] == "preview":
                preview = await cli_bridge.preview_command(data["command"])
                await websocket.send_json({
                    "type": "preview",
                    "data": preview
                })
            
            elif data["type"] == "suggest":
                suggestions = await cli_bridge.get_suggestions(data.get("context", {}))
                await websocket.send_json({
                    "type": "suggestions",
                    "data": suggestions
                })
            
            elif data["type"] == "ai":
                query = AIQuery(
                    query=data["query"],
                    language=data.get("language", "pt-BR"),
                    context=data.get("context", {})
                )
                response = await app.state.ai_assistant.process_query(query)
                await websocket.send_json({
                    "type": "ai_response",
                    "data": response
                })
                
    except WebSocketDisconnect:
        del cli_bridge.active_sessions[session_id]


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )