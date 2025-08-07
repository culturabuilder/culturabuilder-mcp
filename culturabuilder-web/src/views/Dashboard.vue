<template>
  <div class="dashboard">
    <!-- Welcome Section -->
    <section class="welcome-section">
      <h1 class="welcome-title">
        {{ $t('dashboard.welcome', { name: userName }) }}
      </h1>
      <p class="welcome-subtitle">
        {{ $t('dashboard.subtitle') }}
      </p>
    </section>

    <!-- Quick Stats -->
    <section class="stats-grid">
      <StatCard
        v-for="stat in quickStats"
        :key="stat.id"
        :title="stat.title"
        :value="stat.value"
        :change="stat.change"
        :icon="stat.icon"
        :color="stat.color"
        @click="handleStatClick(stat)"
      />
    </section>

    <!-- Main Dashboard Grid -->
    <div class="dashboard-grid">
      <!-- Command Explorer Widget -->
      <DashboardWidget
        :title="t('dashboard.commandExplorer')"
        icon="command"
        :expandable="true"
        class="command-explorer-widget"
      >
        <CommandExplorer
          :commands="recentCommands"
          @execute="executeCommand"
          @favorite="toggleFavorite"
        />
      </DashboardWidget>

      <!-- Live Terminal Widget -->
      <DashboardWidget
        :title="t('dashboard.liveTerminal')"
        icon="terminal"
        :fullscreen="terminalFullscreen"
        @toggle-fullscreen="terminalFullscreen = !terminalFullscreen"
        class="terminal-widget"
      >
        <LiveTerminal
          ref="terminal"
          :height="terminalFullscreen ? '80vh' : '400px'"
          @command="handleTerminalCommand"
        />
      </DashboardWidget>

      <!-- Learning Path Widget -->
      <DashboardWidget
        :title="t('dashboard.learningPath')"
        icon="academic"
        class="learning-widget"
      >
        <LearningPath
          :progress="learningProgress"
          :next-lesson="nextLesson"
          @start-lesson="startLesson"
        />
      </DashboardWidget>

      <!-- Metrics Visualizer Widget -->
      <DashboardWidget
        :title="t('dashboard.metrics')"
        icon="chart"
        :refreshable="true"
        @refresh="refreshMetrics"
        class="metrics-widget"
      >
        <MetricsVisualizer
          :data="metricsData"
          :period="selectedPeriod"
          @period-change="selectedPeriod = $event"
        />
      </DashboardWidget>

      <!-- Recent Activity Widget -->
      <DashboardWidget
        :title="t('dashboard.recentActivity')"
        icon="activity"
        class="activity-widget"
      >
        <ActivityFeed
          :activities="recentActivities"
          :show-details="true"
        />
      </DashboardWidget>

      <!-- AI Insights Widget -->
      <DashboardWidget
        :title="t('dashboard.aiInsights')"
        icon="sparkles"
        class="insights-widget"
      >
        <AIInsights
          :insights="aiInsights"
          @action="handleInsightAction"
        />
      </DashboardWidget>
    </div>

    <!-- Floating Action Button -->
    <FloatingActionButton
      :actions="fabActions"
      @action="handleFabAction"
    />

    <!-- Interactive Tutorial -->
    <InteractiveTutorial
      v-if="showTutorial"
      :topic="currentTutorial"
      @complete="onTutorialComplete"
      @skip="showTutorial = false"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useStore } from '../store'
import { useMetrics } from '../composables/useMetrics'
import { useCommands } from '../composables/useCommands'
import { useLearning } from '../composables/useLearning'
import { useWebSocket } from '../composables/useWebSocket'

// Components
import DashboardWidget from '../components/dashboard/DashboardWidget.vue'
import StatCard from '../components/dashboard/StatCard.vue'
import CommandExplorer from '../components/dashboard/CommandExplorer.vue'
import LiveTerminal from '../components/dashboard/LiveTerminal.vue'
import LearningPath from '../components/dashboard/LearningPath.vue'
import MetricsVisualizer from '../components/dashboard/MetricsVisualizer.vue'
import ActivityFeed from '../components/dashboard/ActivityFeed.vue'
import AIInsights from '../components/dashboard/AIInsights.vue'
import FloatingActionButton from '../components/ui/FloatingActionButton.vue'
import InteractiveTutorial from '../components/tutorial/InteractiveTutorial.vue'

// Composables
const { t, locale } = useI18n()
const store = useStore()
const { getMetrics, refreshMetrics: fetchMetrics } = useMetrics()
const { executeCommand, getRecentCommands, toggleFavorite } = useCommands()
const { getLearningProgress, getNextLesson, startLesson } = useLearning()
const { send, subscribe } = useWebSocket()

// State
const userName = computed(() => store.user?.name || 'Desenvolvedor')
const terminalFullscreen = ref(false)
const selectedPeriod = ref('day')
const showTutorial = ref(false)
const currentTutorial = ref('')

// Data
const quickStats = computed(() => [
  {
    id: 'commands',
    title: t('stats.commandsExecuted'),
    value: store.metrics?.totalCommands || 0,
    change: '+12%',
    icon: 'command-line',
    color: 'primary'
  },
  {
    id: 'success',
    title: t('stats.successRate'),
    value: `${store.metrics?.successRate || 0}%`,
    change: '+5%',
    icon: 'check-circle',
    color: 'success'
  },
  {
    id: 'learning',
    title: t('stats.learningProgress'),
    value: `${store.learning?.progress || 0}%`,
    change: '+8%',
    icon: 'academic-cap',
    color: 'info'
  },
  {
    id: 'time',
    title: t('stats.timeSaved'),
    value: `${store.metrics?.timeSaved || 0}h`,
    change: '+15%',
    icon: 'clock',
    color: 'warning'
  }
])

const recentCommands = computed(() => getRecentCommands(10))
const metricsData = computed(() => getMetrics(selectedPeriod.value))
const learningProgress = computed(() => getLearningProgress())
const nextLesson = computed(() => getNextLesson())
const recentActivities = computed(() => store.activities?.slice(0, 10) || [])

// AI Insights
const aiInsights = computed(() => [
  {
    id: 1,
    type: 'optimization',
    title: t('insights.optimization.title'),
    message: t('insights.optimization.message', { 
      command: '/cb:build',
      times: 5 
    }),
    action: 'create-alias',
    priority: 'high'
  },
  {
    id: 2,
    type: 'learning',
    title: t('insights.learning.title'),
    message: t('insights.learning.message', {
      command: '/cb:analyze',
      improvement: '30%'
    }),
    action: 'learn-command',
    priority: 'medium'
  },
  {
    id: 3,
    type: 'achievement',
    title: t('insights.achievement.title'),
    message: t('insights.achievement.message', {
      percentage: '20%'
    }),
    action: 'view-details',
    priority: 'low'
  }
])

// FAB Actions
const fabActions = [
  {
    id: 'new-project',
    icon: 'plus',
    label: t('actions.newProject'),
    color: 'primary'
  },
  {
    id: 'open-terminal',
    icon: 'terminal',
    label: t('actions.openTerminal'),
    color: 'secondary'
  },
  {
    id: 'start-tutorial',
    icon: 'academic-cap',
    label: t('actions.startTutorial'),
    color: 'info'
  },
  {
    id: 'get-help',
    icon: 'question-mark-circle',
    label: t('actions.getHelp'),
    color: 'warning'
  }
]

// Methods
const handleStatClick = (stat: any) => {
  console.log('Stat clicked:', stat)
  // Navigate to detailed view
}

const handleTerminalCommand = async (command: string) => {
  const result = await executeCommand(command)
  // Handle result
}

const refreshMetrics = async () => {
  await fetchMetrics()
}

const handleInsightAction = (insight: any) => {
  switch (insight.action) {
    case 'create-alias':
      // Open alias creation dialog
      break
    case 'learn-command':
      showTutorial.value = true
      currentTutorial.value = 'command-learning'
      break
    case 'view-details':
      // Navigate to details
      break
  }
}

const handleFabAction = (action: string) => {
  switch (action) {
    case 'new-project':
      // Open new project dialog
      break
    case 'open-terminal':
      terminalFullscreen.value = true
      break
    case 'start-tutorial':
      showTutorial.value = true
      currentTutorial.value = 'getting-started'
      break
    case 'get-help':
      // Open help center
      break
  }
}

const onTutorialComplete = () => {
  showTutorial.value = false
  // Award achievement
}

// WebSocket subscriptions
onMounted(() => {
  // Subscribe to real-time updates
  subscribe('metrics.update', (data) => {
    store.updateMetrics(data)
  })
  
  subscribe('command.executed', (data) => {
    store.addActivity({
      type: 'command',
      ...data
    })
  })
  
  // Load initial data
  refreshMetrics()
})
</script>

<style scoped lang="scss">
.dashboard {
  max-width: 1600px;
  margin: 0 auto;
  padding: var(--cb-spacing-lg);
  
  @media (max-width: 768px) {
    padding: var(--cb-spacing-md);
  }
}

.welcome-section {
  margin-bottom: var(--cb-spacing-xl);
  text-align: center;
  
  .welcome-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--cb-text-primary);
    margin-bottom: var(--cb-spacing-sm);
    
    @media (max-width: 768px) {
      font-size: 1.8rem;
    }
  }
  
  .welcome-subtitle {
    font-size: 1.2rem;
    color: var(--cb-text-secondary);
    
    @media (max-width: 768px) {
      font-size: 1rem;
    }
  }
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--cb-spacing-md);
  margin-bottom: var(--cb-spacing-xl);
  
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
    gap: var(--cb-spacing-sm);
  }
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--cb-spacing-lg);
  
  .command-explorer-widget {
    grid-column: span 4;
    
    @media (max-width: 1200px) {
      grid-column: span 6;
    }
    
    @media (max-width: 768px) {
      grid-column: span 12;
    }
  }
  
  .terminal-widget {
    grid-column: span 8;
    
    @media (max-width: 1200px) {
      grid-column: span 6;
    }
    
    @media (max-width: 768px) {
      grid-column: span 12;
    }
  }
  
  .learning-widget {
    grid-column: span 6;
    
    @media (max-width: 768px) {
      grid-column: span 12;
    }
  }
  
  .metrics-widget {
    grid-column: span 6;
    
    @media (max-width: 768px) {
      grid-column: span 12;
    }
  }
  
  .activity-widget {
    grid-column: span 4;
    
    @media (max-width: 1200px) {
      grid-column: span 6;
    }
    
    @media (max-width: 768px) {
      grid-column: span 12;
    }
  }
  
  .insights-widget {
    grid-column: span 8;
    
    @media (max-width: 1200px) {
      grid-column: span 6;
    }
    
    @media (max-width: 768px) {
      grid-column: span 12;
    }
  }
}
</style>