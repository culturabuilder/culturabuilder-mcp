<template>
  <div class="dashboard">
    <!-- Welcome Section -->
    <section class="welcome-section">
      <h1 class="welcome-title">
        Bem-vindo ao CulturaBuilder! 🌟
      </h1>
      <p class="welcome-subtitle">
        Construa cultura através de tecnologia
      </p>
    </section>

    <!-- Quick Stats -->
    <section class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">📊</div>
        <div class="stat-value">{{ stats.commands }}</div>
        <div class="stat-label">Comandos Executados</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">✅</div>
        <div class="stat-value">{{ stats.successRate }}%</div>
        <div class="stat-label">Taxa de Sucesso</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">📈</div>
        <div class="stat-value">{{ stats.learning }}%</div>
        <div class="stat-label">Progresso</div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">⏱️</div>
        <div class="stat-value">{{ stats.timeSaved }}h</div>
        <div class="stat-label">Tempo Economizado</div>
      </div>
    </section>

    <!-- Main Features -->
    <section class="features-grid">
      <div class="feature-card">
        <h3>🚀 Comandos Rápidos</h3>
        <div class="command-list">
          <div class="command-item" v-for="cmd in commands" :key="cmd.name">
            <code>{{ cmd.name }}</code>
            <span>{{ cmd.description }}</span>
          </div>
        </div>
      </div>

      <div class="feature-card">
        <h3>📊 Métricas Recentes</h3>
        <div class="metrics-preview">
          <div class="metric-bar" v-for="day in weekData" :key="day.name">
            <div class="bar" :style="`height: ${day.value}%`"></div>
            <span>{{ day.name }}</span>
          </div>
        </div>
      </div>

      <div class="feature-card">
        <h3>💡 Dicas</h3>
        <ul class="tips-list">
          <li>Use <code>Ctrl+K</code> para abrir comandos</li>
          <li>Digite <code>/cb:help</code> para ajuda</li>
          <li>Troque idioma com o botão 🇧🇷/🇺🇸</li>
        </ul>
      </div>

      <div class="feature-card">
        <h3>🎯 Ações Rápidas</h3>
        <div class="actions">
          <button @click="executeCommand('build')" class="action-btn">
            🔨 Build
          </button>
          <button @click="executeCommand('analyze')" class="action-btn">
            🔍 Analyze
          </button>
          <button @click="executeCommand('deploy')" class="action-btn">
            🚀 Deploy
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Mock data
const stats = ref({
  commands: 127,
  successRate: 98,
  learning: 75,
  timeSaved: 4.5
})

const commands = ref([
  { name: '/cb:build', description: 'Constrói componentes' },
  { name: '/cb:analyze', description: 'Analisa código' },
  { name: '/cb:metrics', description: 'Visualiza métricas' }
])

const weekData = ref([
  { name: 'Seg', value: 60 },
  { name: 'Ter', value: 80 },
  { name: 'Qua', value: 70 },
  { name: 'Qui', value: 90 },
  { name: 'Sex', value: 85 }
])

// Methods
const executeCommand = async (command) => {
  console.log(`Executing: /cb:${command}`)
  
  // Call API
  try {
    const response = await fetch('http://localhost:8000/api/command/execute', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ command: `/cb:${command}`, flags: [] })
    })
    const result = await response.json()
    console.log('Result:', result)
  } catch (error) {
    console.error('Error:', error)
  }
}

// Load metrics on mount
onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/metrics/summary')
    const metrics = await response.json()
    console.log('Metrics:', metrics)
  } catch (error) {
    console.error('Failed to load metrics:', error)
  }
})
</script>

<style scoped>
.dashboard {
  padding: 0;
}

.welcome-section {
  text-align: center;
  margin-bottom: 3rem;
}

.welcome-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, var(--cb-primary) 0%, var(--cb-secondary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.welcome-subtitle {
  font-size: 1.2rem;
  color: var(--cb-text-secondary);
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: var(--cb-bg-secondary);
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
  border: 1px solid var(--cb-border);
  transition: transform 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--cb-primary);
}

.stat-label {
  color: var(--cb-text-secondary);
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: var(--cb-bg-secondary);
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid var(--cb-border);
}

.feature-card h3 {
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

/* Command List */
.command-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.command-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  background: var(--cb-bg-tertiary);
  border-radius: 6px;
}

.command-item code {
  color: var(--cb-primary);
  font-weight: 600;
}

/* Metrics Preview */
.metrics-preview {
  display: flex;
  align-items: flex-end;
  justify-content: space-around;
  height: 100px;
  gap: 0.5rem;
}

.metric-bar {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
}

.bar {
  width: 100%;
  background: linear-gradient(to top, var(--cb-primary), var(--cb-secondary));
  border-radius: 4px 4px 0 0;
  transition: height 0.3s;
}

.metric-bar span {
  margin-top: 0.5rem;
  font-size: 0.8rem;
  color: var(--cb-text-secondary);
}

/* Tips */
.tips-list {
  list-style: none;
  padding: 0;
}

.tips-list li {
  padding: 0.5rem 0;
  color: var(--cb-text-secondary);
}

.tips-list code {
  background: var(--cb-bg-tertiary);
  padding: 2px 6px;
  border-radius: 4px;
  color: var(--cb-primary);
}

/* Actions */
.actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.action-btn {
  flex: 1;
  min-width: 100px;
  padding: 0.75rem 1rem;
  background: var(--cb-primary);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.action-btn:hover {
  background: var(--cb-primary);
  transform: translateY(-2px);
  opacity: 0.9;
}
</style>