import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import App from './App.vue'
import router from './router'
import store from './store'

// Import styles
import './styles/main.scss'

// Import i18n messages
import ptBR from './i18n/pt-BR.json'
import enUS from './i18n/en-US.json'

// Create i18n instance
const i18n = createI18n({
  legacy: false,
  locale: 'pt-BR',
  fallbackLocale: 'en-US',
  messages: {
    'pt-BR': ptBR,
    'en-US': enUS
  }
})

// Create app
const app = createApp(App)

// Use plugins
app.use(router)
app.use(store)
app.use(i18n)

// Mount app
app.mount('#app')

// Signal app is ready
window.dispatchEvent(new Event('app-ready'))