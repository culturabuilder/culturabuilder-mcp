<template>
  <div id="app" :class="[theme, locale]">
    <!-- Header Global -->
    <HeaderComponent 
      @toggle-theme="toggleTheme"
      @toggle-language="toggleLanguage"
      @open-command-palette="openCommandPalette"
    />
    
    <!-- Command Palette (Global) -->
    <CommandPalette 
      v-if="showCommandPalette"
      @close="showCommandPalette = false"
      @execute="executeCommand"
    />
    
    <!-- Main Content Area -->
    <div class="main-container">
      <!-- Sidebar Navigation -->
      <SidebarNav 
        :collapsed="sidebarCollapsed"
        @toggle="sidebarCollapsed = !sidebarCollapsed"
      />
      
      <!-- Content Area with Router -->
      <main class="content-area">
        <router-view v-slot="{ Component }">
          <transition name="page-transition" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </main>
      
      <!-- AI Assistant Panel -->
      <AIAssistant 
        v-if="showAssistant"
        @close="showAssistant = false"
      />
    </div>
    
    <!-- Global Notifications -->
    <NotificationCenter />
    
    <!-- Tutorial Overlay -->
    <TutorialOverlay 
      v-if="showTutorial"
      :step="currentTutorialStep"
      @next="nextTutorialStep"
      @skip="skipTutorial"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useTheme } from './composables/useTheme'
import { useCommandSystem } from './composables/useCommandSystem'
import { useTutorial } from './composables/useTutorial'
import { useWebSocket } from './composables/useWebSocket'

// Components
import HeaderComponent from './components/layout/HeaderComponent.vue'
import SidebarNav from './components/layout/SidebarNav.vue'
import CommandPalette from './components/CommandPalette.vue'
import AIAssistant from './components/AIAssistant.vue'
import NotificationCenter from './components/NotificationCenter.vue'
import TutorialOverlay from './components/TutorialOverlay.vue'

// Composables
const { locale, t } = useI18n()
const { theme, toggleTheme } = useTheme()
const { executeCommand } = useCommandSystem()
const { currentStep: currentTutorialStep, next: nextTutorialStep, skip: skipTutorial } = useTutorial()
const { connect, disconnect } = useWebSocket()

// State
const showCommandPalette = ref(false)
const showAssistant = ref(false)
const showTutorial = ref(false)
const sidebarCollapsed = ref(false)

// Language toggle
const toggleLanguage = () => {
  locale.value = locale.value === 'pt-BR' ? 'en-US' : 'pt-BR'
}

// Command Palette shortcut
const openCommandPalette = () => {
  showCommandPalette.value = true
}

// Keyboard shortcuts
onMounted(() => {
  // WebSocket connection
  connect()
  
  // Global keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    // Cmd/Ctrl + K for command palette
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault()
      openCommandPalette()
    }
    
    // Cmd/Ctrl + / for AI assistant
    if ((e.metaKey || e.ctrlKey) && e.key === '/') {
      e.preventDefault()
      showAssistant.value = !showAssistant.value
    }
    
    // Cmd/Ctrl + B for sidebar toggle
    if ((e.metaKey || e.ctrlKey) && e.key === 'b') {
      e.preventDefault()
      sidebarCollapsed.value = !sidebarCollapsed.value
    }
  })
  
  // Check if first time user
  const isFirstTime = !localStorage.getItem('cb-visited')
  if (isFirstTime) {
    showTutorial.value = true
    localStorage.setItem('cb-visited', 'true')
  }
})

// Cleanup
onUnmounted(() => {
  disconnect()
})
</script>

<style lang="scss">
@import './styles/variables.scss';
@import './styles/themes.scss';
@import './styles/animations.scss';

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: var(--cb-font-primary);
  min-height: 100vh;
  background: var(--cb-bg-primary);
  color: var(--cb-text-primary);
  transition: var(--cb-transition);
  
  &.dark {
    @include dark-theme;
  }
  
  &.light {
    @include light-theme;
  }
}

.main-container {
  display: flex;
  height: calc(100vh - var(--header-height));
  position: relative;
  
  @media (max-width: 768px) {
    flex-direction: column;
  }
}

.content-area {
  flex: 1;
  overflow-y: auto;
  padding: var(--cb-spacing-lg);
  background: var(--cb-bg-secondary);
  
  @media (max-width: 768px) {
    padding: var(--cb-spacing-md);
  }
}

// Page transitions
.page-transition-enter-active,
.page-transition-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.page-transition-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.page-transition-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

// Scrollbar styling
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: var(--cb-bg-tertiary);
}

::-webkit-scrollbar-thumb {
  background: var(--cb-primary);
  border-radius: 4px;
  
  &:hover {
    background: var(--cb-primary-dark);
  }
}
</style>