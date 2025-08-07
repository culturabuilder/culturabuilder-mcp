<template>
  <div id="app" :class="theme">
    <!-- Simple Header -->
    <header class="app-header">
      <div class="header-content">
        <div class="logo">
          <span class="logo-icon">🌟</span>
          <span class="logo-text">CulturaBuilder</span>
        </div>
        <nav class="nav-menu">
          <router-link to="/" class="nav-link">Dashboard</router-link>
          <router-link to="/commands" class="nav-link">Comandos</router-link>
          <router-link to="/metrics" class="nav-link">Métricas</router-link>
          <router-link to="/settings" class="nav-link">Configurações</router-link>
        </nav>
        <div class="header-actions">
          <button @click="toggleLanguage" class="btn-icon">{{ currentLang }}</button>
          <button @click="toggleTheme" class="btn-icon">{{ theme === 'light' ? '🌙' : '☀️' }}</button>
        </div>
      </div>
    </header>
    
    <!-- Main Content -->
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useStore } from 'vuex'

// Composables
const { locale } = useI18n()
const store = useStore()

// State
const theme = computed(() => store.state.theme)
const currentLang = computed(() => locale.value === 'pt-BR' ? '🇧🇷' : '🇺🇸')

// Methods
const toggleTheme = () => {
  store.dispatch('toggleTheme')
}

const toggleLanguage = () => {
  const newLang = locale.value === 'pt-BR' ? 'en-US' : 'pt-BR'
  locale.value = newLang
  store.dispatch('changeLanguage', newLang)
}

// Initialize
onMounted(() => {
  // Load saved preferences
  const savedTheme = localStorage.getItem('cb-theme') || 'light'
  const savedLang = localStorage.getItem('cb-language') || 'pt-BR'
  
  store.commit('SET_THEME', savedTheme)
  store.commit('SET_LANGUAGE', savedLang)
  locale.value = savedLang
  document.body.className = savedTheme
})
</script>

<style scoped>
#app {
  min-height: 100vh;
  background: var(--cb-bg-primary);
}

.app-header {
  background: var(--cb-bg-secondary);
  border-bottom: 1px solid var(--cb-border);
  height: var(--header-height);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  max-width: 1400px;
  margin: 0 auto;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--cb-spacing-md);
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 700;
  font-size: 1.25rem;
}

.logo-icon {
  font-size: 1.5rem;
}

.nav-menu {
  display: flex;
  gap: var(--cb-spacing-md);
}

.nav-link {
  color: var(--cb-text-secondary);
  text-decoration: none;
  font-weight: 500;
  transition: var(--cb-transition);
  
  &:hover {
    color: var(--cb-primary);
  }
  
  &.router-link-active {
    color: var(--cb-primary);
  }
}

.header-actions {
  display: flex;
  gap: var(--cb-spacing-sm);
}

.btn-icon {
  padding: 8px 12px;
  background: transparent;
  border: 1px solid var(--cb-border);
  border-radius: 8px;
  cursor: pointer;
  transition: var(--cb-transition);
  font-size: 1.2rem;
  
  &:hover {
    background: var(--cb-bg-tertiary);
  }
}

.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: var(--cb-spacing-lg) var(--cb-spacing-md);
}
</style>