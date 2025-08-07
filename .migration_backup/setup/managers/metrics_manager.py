"""
Metrics Manager for SuperClaude Framework
Handles usage metrics collection, storage, and export functionality
"""

import json
import csv
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from enum import Enum

from .settings_manager import SettingsManager
from ..utils.logger import Logger


class ExportFormat(Enum):
    """Supported export formats for metrics"""
    JSON = "json"
    CSV = "csv"
    HTML = "html"
    MARKDOWN = "markdown"


class MetricsManager(SettingsManager):
    """
    Manages usage metrics for the SuperClaude Framework.
    Extends SettingsManager to leverage existing infrastructure.
    """
    
    def __init__(self, install_dir: Path):
        """
        Initialize the MetricsManager.
        
        Args:
            install_dir: The installation directory path
        """
        super().__init__(install_dir)
        self.logger = Logger()
        self.metrics_file = install_dir / ".superclaude-metrics.json"
        self.metrics_enabled = self._check_metrics_consent()
        self.session_id = self._generate_session_id()
        self.session_start = time.time()
        
        # Initialize metrics structure
        self._ensure_metrics_file()
    
    def _check_metrics_consent(self) -> bool:
        """Check if user has consented to metrics collection."""
        try:
            settings = self.load_settings()
            return settings.get("metrics", {}).get("enabled", False)
        except:
            return False
    
    def _generate_session_id(self) -> str:
        """Generate a unique session identifier."""
        return f"session_{int(time.time() * 1000)}"
    
    def _ensure_metrics_file(self):
        """Ensure metrics file exists with proper structure."""
        if not self.metrics_file.exists():
            initial_metrics = {
                "version": "1.0.0",
                "created_at": datetime.now().isoformat(),
                "privacy": {
                    "enabled": False,
                    "anonymous": True,
                    "last_consent_check": datetime.now().isoformat()
                },
                "usage": {
                    "commands": {},
                    "flags": {},
                    "components": {},
                    "sessions": []
                },
                "performance": {
                    "operations": [],
                    "averages": {}
                },
                "errors": {
                    "by_type": {},
                    "by_command": {},
                    "recent": []
                },
                "export_history": []
            }
            self._save_metrics(initial_metrics)
    
    def _load_metrics(self) -> Dict[str, Any]:
        """Load metrics from file."""
        try:
            if self.metrics_file.exists():
                with open(self.metrics_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load metrics: {e}")
        
        self._ensure_metrics_file()
        return json.loads(self.metrics_file.read_text(encoding='utf-8'))
    
    def _save_metrics(self, metrics: Dict[str, Any]) -> bool:
        """Save metrics to file."""
        try:
            with open(self.metrics_file, 'w', encoding='utf-8') as f:
                json.dump(metrics, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            self.logger.error(f"Failed to save metrics: {e}")
            return False
    
    def enable_metrics(self, anonymous: bool = True) -> bool:
        """
        Enable metrics collection with user consent.
        
        Args:
            anonymous: Whether to collect anonymous metrics only
            
        Returns:
            Success status
        """
        metrics = self._load_metrics()
        metrics["privacy"]["enabled"] = True
        metrics["privacy"]["anonymous"] = anonymous
        metrics["privacy"]["last_consent_check"] = datetime.now().isoformat()
        
        self.metrics_enabled = True
        return self._save_metrics(metrics)
    
    def disable_metrics(self) -> bool:
        """Disable metrics collection."""
        metrics = self._load_metrics()
        metrics["privacy"]["enabled"] = False
        metrics["privacy"]["last_consent_check"] = datetime.now().isoformat()
        
        self.metrics_enabled = False
        return self._save_metrics(metrics)
    
    def record_command(self, command: str, flags: List[str] = None, 
                      success: bool = True, duration: float = 0.0,
                      metadata: Dict[str, Any] = None):
        """
        Record a command execution.
        
        Args:
            command: The command that was executed
            flags: List of flags used
            success: Whether the command succeeded
            duration: Execution duration in seconds
            metadata: Additional metadata to record
        """
        if not self.metrics_enabled:
            return
        
        metrics = self._load_metrics()
        
        # Update command counts
        if command not in metrics["usage"]["commands"]:
            metrics["usage"]["commands"][command] = {
                "count": 0,
                "success": 0,
                "failed": 0,
                "total_duration": 0.0,
                "flags_used": {}
            }
        
        cmd_metrics = metrics["usage"]["commands"][command]
        cmd_metrics["count"] += 1
        cmd_metrics["success" if success else "failed"] += 1
        cmd_metrics["total_duration"] += duration
        
        # Track flags usage
        if flags:
            for flag in flags:
                if flag not in metrics["usage"]["flags"]:
                    metrics["usage"]["flags"][flag] = {"count": 0, "commands": {}}
                metrics["usage"]["flags"][flag]["count"] += 1
                
                if command not in metrics["usage"]["flags"][flag]["commands"]:
                    metrics["usage"]["flags"][flag]["commands"][command] = 0
                metrics["usage"]["flags"][flag]["commands"][command] += 1
                
                # Track flag combinations for this command
                if flag not in cmd_metrics["flags_used"]:
                    cmd_metrics["flags_used"][flag] = 0
                cmd_metrics["flags_used"][flag] += 1
        
        # Record in performance history
        operation = {
            "timestamp": datetime.now().isoformat(),
            "command": command,
            "flags": flags or [],
            "success": success,
            "duration": duration,
            "session_id": self.session_id
        }
        
        if metadata:
            operation["metadata"] = metadata
        
        metrics["performance"]["operations"].append(operation)
        
        # Keep only last 1000 operations to prevent unbounded growth
        if len(metrics["performance"]["operations"]) > 1000:
            metrics["performance"]["operations"] = metrics["performance"]["operations"][-1000:]
        
        # Update averages
        self._update_averages(metrics)
        
        self._save_metrics(metrics)
    
    def record_component_usage(self, component: str, operation: str = "used"):
        """
        Record component usage.
        
        Args:
            component: The component name
            operation: The operation performed (install, update, use, etc.)
        """
        if not self.metrics_enabled:
            return
        
        metrics = self._load_metrics()
        
        if component not in metrics["usage"]["components"]:
            metrics["usage"]["components"][component] = {
                "install_count": 0,
                "update_count": 0,
                "use_count": 0,
                "last_used": None
            }
        
        comp_metrics = metrics["usage"]["components"][component]
        
        if operation == "install":
            comp_metrics["install_count"] += 1
        elif operation == "update":
            comp_metrics["update_count"] += 1
        else:
            comp_metrics["use_count"] += 1
        
        comp_metrics["last_used"] = datetime.now().isoformat()
        
        self._save_metrics(metrics)
    
    def record_error(self, error_type: str, command: str = None, 
                    details: str = None):
        """
        Record an error occurrence.
        
        Args:
            error_type: Type of error
            command: Command where error occurred
            details: Error details
        """
        if not self.metrics_enabled:
            return
        
        metrics = self._load_metrics()
        
        # Track by error type
        if error_type not in metrics["errors"]["by_type"]:
            metrics["errors"]["by_type"][error_type] = 0
        metrics["errors"]["by_type"][error_type] += 1
        
        # Track by command if provided
        if command:
            if command not in metrics["errors"]["by_command"]:
                metrics["errors"]["by_command"][command] = {}
            if error_type not in metrics["errors"]["by_command"][command]:
                metrics["errors"]["by_command"][command][error_type] = 0
            metrics["errors"]["by_command"][command][error_type] += 1
        
        # Add to recent errors
        error_record = {
            "timestamp": datetime.now().isoformat(),
            "type": error_type,
            "command": command,
            "details": details,
            "session_id": self.session_id
        }
        
        metrics["errors"]["recent"].append(error_record)
        
        # Keep only last 100 errors
        if len(metrics["errors"]["recent"]) > 100:
            metrics["errors"]["recent"] = metrics["errors"]["recent"][-100:]
        
        self._save_metrics(metrics)
    
    def record_session_end(self):
        """Record the end of a session."""
        if not self.metrics_enabled:
            return
        
        metrics = self._load_metrics()
        
        session_duration = time.time() - self.session_start
        session_record = {
            "id": self.session_id,
            "start": datetime.fromtimestamp(self.session_start).isoformat(),
            "end": datetime.now().isoformat(),
            "duration": session_duration
        }
        
        metrics["usage"]["sessions"].append(session_record)
        
        # Keep only last 100 sessions
        if len(metrics["usage"]["sessions"]) > 100:
            metrics["usage"]["sessions"] = metrics["usage"]["sessions"][-100:]
        
        self._save_metrics(metrics)
    
    def _update_averages(self, metrics: Dict[str, Any]):
        """Update performance averages."""
        operations = metrics["performance"]["operations"]
        if not operations:
            return
        
        # Calculate overall averages
        total_duration = sum(op["duration"] for op in operations)
        success_count = sum(1 for op in operations if op["success"])
        
        metrics["performance"]["averages"] = {
            "duration": total_duration / len(operations) if operations else 0,
            "success_rate": success_count / len(operations) if operations else 0,
            "total_operations": len(operations)
        }
        
        # Calculate per-command averages
        command_stats = defaultdict(lambda: {"count": 0, "duration": 0, "success": 0})
        for op in operations:
            cmd = op["command"]
            command_stats[cmd]["count"] += 1
            command_stats[cmd]["duration"] += op["duration"]
            command_stats[cmd]["success"] += 1 if op["success"] else 0
        
        metrics["performance"]["averages"]["by_command"] = {}
        for cmd, stats in command_stats.items():
            metrics["performance"]["averages"]["by_command"][cmd] = {
                "avg_duration": stats["duration"] / stats["count"],
                "success_rate": stats["success"] / stats["count"],
                "total_count": stats["count"]
            }
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """
        Get summary statistics.
        
        Returns:
            Dictionary containing summary statistics
        """
        metrics = self._load_metrics()
        
        # Calculate summary
        summary = {
            "total_commands": sum(
                cmd["count"] for cmd in metrics["usage"]["commands"].values()
            ),
            "unique_commands": len(metrics["usage"]["commands"]),
            "total_flags_used": sum(
                flag["count"] for flag in metrics["usage"]["flags"].values()
            ),
            "unique_flags": len(metrics["usage"]["flags"]),
            "total_sessions": len(metrics["usage"]["sessions"]),
            "total_errors": sum(metrics["errors"]["by_type"].values()),
            "error_types": len(metrics["errors"]["by_type"]),
            "components_used": len(metrics["usage"]["components"]),
            "performance": metrics["performance"]["averages"]
        }
        
        # Add top commands
        if metrics["usage"]["commands"]:
            top_commands = sorted(
                metrics["usage"]["commands"].items(),
                key=lambda x: x[1]["count"],
                reverse=True
            )[:5]
            summary["top_commands"] = [
                {"name": cmd, "count": data["count"]} 
                for cmd, data in top_commands
            ]
        
        # Add top flags
        if metrics["usage"]["flags"]:
            top_flags = sorted(
                metrics["usage"]["flags"].items(),
                key=lambda x: x[1]["count"],
                reverse=True
            )[:5]
            summary["top_flags"] = [
                {"name": flag, "count": data["count"]} 
                for flag, data in top_flags
            ]
        
        return summary
    
    def get_time_series_data(self, period: str = "day") -> Dict[str, Any]:
        """
        Get time series data for visualization.
        
        Args:
            period: Aggregation period (hour, day, week, month)
            
        Returns:
            Time series data
        """
        metrics = self._load_metrics()
        operations = metrics["performance"]["operations"]
        
        if not operations:
            return {"periods": [], "data": {}}
        
        # Parse timestamps and group by period
        time_buckets = defaultdict(lambda: {
            "count": 0, "success": 0, "duration": 0, "commands": Counter()
        })
        
        for op in operations:
            timestamp = datetime.fromisoformat(op["timestamp"])
            
            if period == "hour":
                bucket = timestamp.replace(minute=0, second=0, microsecond=0)
            elif period == "day":
                bucket = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
            elif period == "week":
                # Start of week
                days_since_monday = timestamp.weekday()
                bucket = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
                bucket = bucket - timedelta(days=days_since_monday)
            else:  # month
                bucket = timestamp.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            
            bucket_key = bucket.isoformat()
            time_buckets[bucket_key]["count"] += 1
            time_buckets[bucket_key]["success"] += 1 if op["success"] else 0
            time_buckets[bucket_key]["duration"] += op["duration"]
            time_buckets[bucket_key]["commands"][op["command"]] += 1
        
        # Sort buckets and format
        sorted_buckets = sorted(time_buckets.items())
        
        return {
            "period": period,
            "periods": [bucket for bucket, _ in sorted_buckets],
            "data": {
                "operations": [data["count"] for _, data in sorted_buckets],
                "success_rate": [
                    (data["success"] / data["count"] * 100) if data["count"] > 0 else 0
                    for _, data in sorted_buckets
                ],
                "avg_duration": [
                    (data["duration"] / data["count"]) if data["count"] > 0 else 0
                    for _, data in sorted_buckets
                ],
                "top_commands": [
                    data["commands"].most_common(1)[0] if data["commands"] else ("", 0)
                    for _, data in sorted_buckets
                ]
            }
        }
    
    def export_metrics(self, format: ExportFormat, 
                      output_path: Optional[Path] = None,
                      time_range: Optional[Tuple[datetime, datetime]] = None) -> Path:
        """
        Export metrics to specified format.
        
        Args:
            format: Export format
            output_path: Output file path (auto-generated if None)
            time_range: Optional time range filter
            
        Returns:
            Path to exported file
        """
        metrics = self._load_metrics()
        
        # Filter by time range if specified
        if time_range:
            start, end = time_range
            metrics = self._filter_by_time_range(metrics, start, end)
        
        # Generate output path if not provided
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = self.install_dir / f"metrics_export_{timestamp}.{format.value}"
        
        # Export based on format
        if format == ExportFormat.JSON:
            self._export_json(metrics, output_path)
        elif format == ExportFormat.CSV:
            self._export_csv(metrics, output_path)
        elif format == ExportFormat.HTML:
            self._export_html(metrics, output_path)
        elif format == ExportFormat.MARKDOWN:
            self._export_markdown(metrics, output_path)
        
        # Record export
        metrics = self._load_metrics()  # Reload to avoid overwriting filtered data
        metrics["export_history"].append({
            "timestamp": datetime.now().isoformat(),
            "format": format.value,
            "path": str(output_path),
            "time_range": [t.isoformat() for t in time_range] if time_range else None
        })
        
        # Keep only last 50 exports
        if len(metrics["export_history"]) > 50:
            metrics["export_history"] = metrics["export_history"][-50:]
        
        self._save_metrics(metrics)
        
        return output_path
    
    def _filter_by_time_range(self, metrics: Dict[str, Any], 
                             start: datetime, end: datetime) -> Dict[str, Any]:
        """Filter metrics by time range."""
        filtered = json.loads(json.dumps(metrics))  # Deep copy
        
        # Filter operations
        filtered["performance"]["operations"] = [
            op for op in filtered["performance"]["operations"]
            if start <= datetime.fromisoformat(op["timestamp"]) <= end
        ]
        
        # Filter sessions
        filtered["usage"]["sessions"] = [
            session for session in filtered["usage"]["sessions"]
            if start <= datetime.fromisoformat(session["start"]) <= end
        ]
        
        # Filter errors
        filtered["errors"]["recent"] = [
            error for error in filtered["errors"]["recent"]
            if start <= datetime.fromisoformat(error["timestamp"]) <= end
        ]
        
        return filtered
    
    def _export_json(self, metrics: Dict[str, Any], output_path: Path):
        """Export metrics as JSON."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(metrics, f, indent=2, ensure_ascii=False)
    
    def _export_csv(self, metrics: Dict[str, Any], output_path: Path):
        """Export metrics as CSV."""
        # Create multiple CSV files for different sections
        base_path = output_path.with_suffix('')
        
        # Export commands
        commands_path = Path(f"{base_path}_commands.csv")
        with open(commands_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Command', 'Count', 'Success', 'Failed', 'Avg Duration'])
            for cmd, data in metrics["usage"]["commands"].items():
                avg_duration = (data["total_duration"] / data["count"]) if data["count"] > 0 else 0
                writer.writerow([cmd, data["count"], data["success"], 
                               data["failed"], f"{avg_duration:.2f}"])
        
        # Export flags
        flags_path = Path(f"{base_path}_flags.csv")
        with open(flags_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Flag', 'Count', 'Top Commands'])
            for flag, data in metrics["usage"]["flags"].items():
                top_commands = ', '.join(
                    sorted(data["commands"].keys(), 
                          key=lambda x: data["commands"][x], 
                          reverse=True)[:3]
                )
                writer.writerow([flag, data["count"], top_commands])
        
        # Export operations
        operations_path = Path(f"{base_path}_operations.csv")
        with open(operations_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Command', 'Flags', 'Success', 'Duration'])
            for op in metrics["performance"]["operations"]:
                writer.writerow([
                    op["timestamp"], op["command"], 
                    ' '.join(op["flags"]), op["success"], 
                    f"{op['duration']:.2f}"
                ])
    
    def _export_html(self, metrics: Dict[str, Any], output_path: Path):
        """Export metrics as HTML report."""
        summary = self.get_summary_stats()
        time_series = self.get_time_series_data("day")
        
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>SuperClaude Metrics Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }}
        h1 {{ color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
        h2 {{ color: #555; margin-top: 30px; }}
        .summary {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
        .metric-card {{ background: #f8f9fa; padding: 15px; border-radius: 5px; border-left: 4px solid #007bff; }}
        .metric-value {{ font-size: 24px; font-weight: bold; color: #007bff; }}
        .metric-label {{ color: #666; font-size: 14px; margin-top: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #007bff; color: white; }}
        tr:hover {{ background: #f5f5f5; }}
        .chart {{ margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 5px; }}
        .footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>SuperClaude Metrics Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <h2>Summary Statistics</h2>
        <div class="summary">
            <div class="metric-card">
                <div class="metric-value">{summary['total_commands']}</div>
                <div class="metric-label">Total Commands</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{summary['unique_commands']}</div>
                <div class="metric-label">Unique Commands</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{summary['total_sessions']}</div>
                <div class="metric-label">Total Sessions</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{summary.get('performance', {}).get('success_rate', 0):.1%}</div>
                <div class="metric-label">Success Rate</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{summary.get('performance', {}).get('duration', 0):.2f}s</div>
                <div class="metric-label">Avg Duration</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{summary['total_errors']}</div>
                <div class="metric-label">Total Errors</div>
            </div>
        </div>
        
        <h2>Top Commands</h2>
        <table>
            <tr>
                <th>Command</th>
                <th>Count</th>
                <th>Success Rate</th>
                <th>Avg Duration</th>
            </tr>"""
        
        for cmd, data in sorted(metrics["usage"]["commands"].items(), 
                               key=lambda x: x[1]["count"], reverse=True)[:10]:
            success_rate = (data["success"] / data["count"] * 100) if data["count"] > 0 else 0
            avg_duration = (data["total_duration"] / data["count"]) if data["count"] > 0 else 0
            html_content += f"""
            <tr>
                <td>{cmd}</td>
                <td>{data['count']}</td>
                <td>{success_rate:.1f}%</td>
                <td>{avg_duration:.2f}s</td>
            </tr>"""
        
        html_content += """
        </table>
        
        <h2>Top Flags</h2>
        <table>
            <tr>
                <th>Flag</th>
                <th>Count</th>
                <th>Used With Commands</th>
            </tr>"""
        
        for flag, data in sorted(metrics["usage"]["flags"].items(), 
                                key=lambda x: x[1]["count"], reverse=True)[:10]:
            top_commands = ', '.join(
                sorted(data["commands"].keys(), 
                      key=lambda x: data["commands"][x], 
                      reverse=True)[:3]
            )
            html_content += f"""
            <tr>
                <td>{flag}</td>
                <td>{data['count']}</td>
                <td>{top_commands}</td>
            </tr>"""
        
        html_content += """
        </table>
        
        <h2>Components Usage</h2>
        <table>
            <tr>
                <th>Component</th>
                <th>Installs</th>
                <th>Updates</th>
                <th>Uses</th>
                <th>Last Used</th>
            </tr>"""
        
        for comp, data in sorted(metrics["usage"]["components"].items(), 
                                key=lambda x: x[1]["use_count"], reverse=True):
            last_used = data.get("last_used", "Never")
            if last_used != "Never":
                last_used = datetime.fromisoformat(last_used).strftime('%Y-%m-%d %H:%M')
            html_content += f"""
            <tr>
                <td>{comp}</td>
                <td>{data['install_count']}</td>
                <td>{data['update_count']}</td>
                <td>{data['use_count']}</td>
                <td>{last_used}</td>
            </tr>"""
        
        html_content += """
        </table>
        
        <div class="footer">
            <p>SuperClaude Framework Metrics Report - Privacy-respecting local analytics</p>
        </div>
    </div>
</body>
</html>"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def _export_markdown(self, metrics: Dict[str, Any], output_path: Path):
        """Export metrics as Markdown report."""
        summary = self.get_summary_stats()
        
        md_content = f"""# SuperClaude Metrics Report

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Commands | {summary['total_commands']} |
| Unique Commands | {summary['unique_commands']} |
| Total Sessions | {summary['total_sessions']} |
| Success Rate | {summary.get('performance', {}).get('success_rate', 0):.1%} |
| Avg Duration | {summary.get('performance', {}).get('duration', 0):.2f}s |
| Total Errors | {summary['total_errors']} |
| Components Used | {summary['components_used']} |

## Top Commands

| Command | Count | Success Rate | Avg Duration |
|---------|-------|--------------|--------------|
"""
        
        for cmd, data in sorted(metrics["usage"]["commands"].items(), 
                               key=lambda x: x[1]["count"], reverse=True)[:10]:
            success_rate = (data["success"] / data["count"] * 100) if data["count"] > 0 else 0
            avg_duration = (data["total_duration"] / data["count"]) if data["count"] > 0 else 0
            md_content += f"| {cmd} | {data['count']} | {success_rate:.1f}% | {avg_duration:.2f}s |\n"
        
        md_content += """
## Top Flags

| Flag | Count | Top Commands |
|------|-------|--------------|
"""
        
        for flag, data in sorted(metrics["usage"]["flags"].items(), 
                                key=lambda x: x[1]["count"], reverse=True)[:10]:
            top_commands = ', '.join(
                sorted(data["commands"].keys(), 
                      key=lambda x: data["commands"][x], 
                      reverse=True)[:3]
            )
            md_content += f"| {flag} | {data['count']} | {top_commands} |\n"
        
        md_content += """
## Error Analysis

### Errors by Type
| Error Type | Count |
|------------|-------|
"""
        
        for error_type, count in sorted(metrics["errors"]["by_type"].items(), 
                                       key=lambda x: x[1], reverse=True):
            md_content += f"| {error_type} | {count} |\n"
        
        md_content += """
## Components Usage

| Component | Installs | Updates | Uses | Last Used |
|-----------|----------|---------|------|-----------|
"""
        
        for comp, data in sorted(metrics["usage"]["components"].items(), 
                                key=lambda x: x[1]["use_count"], reverse=True):
            last_used = data.get("last_used", "Never")
            if last_used != "Never":
                last_used = datetime.fromisoformat(last_used).strftime('%Y-%m-%d')
            md_content += f"| {comp} | {data['install_count']} | {data['update_count']} | {data['use_count']} | {last_used} |\n"
        
        md_content += """

---
*SuperClaude Framework - Privacy-respecting local analytics*
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
    
    def clear_metrics(self, confirm: bool = False) -> bool:
        """
        Clear all metrics data.
        
        Args:
            confirm: Safety confirmation flag
            
        Returns:
            Success status
        """
        if not confirm:
            self.logger.warning("Clear metrics requires confirmation flag")
            return False
        
        self._ensure_metrics_file()
        self.logger.info("All metrics data cleared")
        return True
    
    def get_privacy_status(self) -> Dict[str, Any]:
        """Get current privacy settings and status."""
        metrics = self._load_metrics()
        return {
            "enabled": metrics["privacy"]["enabled"],
            "anonymous": metrics["privacy"]["anonymous"],
            "last_consent_check": metrics["privacy"]["last_consent_check"],
            "data_location": str(self.metrics_file),
            "data_size_kb": self.metrics_file.stat().st_size / 1024 if self.metrics_file.exists() else 0
        }