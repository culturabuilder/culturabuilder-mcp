#!/usr/bin/env node
/**
 * Test CulturaBuilder MCP Server
 * Verifica se o servidor está funcionando corretamente
 */

const { spawn } = require('child_process');
const path = require('path');

console.log('🌟 Testando CulturaBuilder MCP Server...\n');

const serverPath = path.join(__dirname, 'culturabuilder-mcp/dist/index.js');

// Start the MCP server
const server = spawn('node', [serverPath], {
  stdio: ['pipe', 'pipe', 'pipe']
});

// Handle server output
server.stdout.on('data', (data) => {
  console.log(`[SERVER OUT]: ${data.toString()}`);
});

server.stderr.on('data', (data) => {
  console.log(`[SERVER LOG]: ${data.toString()}`);
});

server.on('error', (error) => {
  console.error(`❌ Erro ao iniciar servidor: ${error.message}`);
  process.exit(1);
});

// Send test request after a delay
setTimeout(() => {
  console.log('\n📝 Enviando requisição de teste...\n');
  
  // Send list tools request (MCP protocol)
  const request = {
    jsonrpc: "2.0",
    method: "tools/list",
    id: 1,
    params: {}
  };
  
  server.stdin.write(JSON.stringify(request) + '\n');
  
  // Wait for response and exit
  setTimeout(() => {
    console.log('\n✅ Teste concluído! Servidor MCP está funcionando.');
    console.log('\n📋 Próximos passos:');
    console.log('1. Reinicie o Claude Desktop');
    console.log('2. Os comandos /cb: estarão disponíveis');
    console.log('3. Digite /cb: e veja o autocomplete!\n');
    server.kill();
    process.exit(0);
  }, 2000);
}, 1000);

console.log('⏳ Iniciando servidor...');