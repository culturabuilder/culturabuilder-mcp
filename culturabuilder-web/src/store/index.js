import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      name: 'Desenvolvedor',
      language: 'pt-BR'
    },
    theme: 'light',
    metrics: {
      totalCommands: 0,
      successRate: 0,
      timeSaved: 0
    },
    commands: [],
    activities: []
  },
  
  mutations: {
    SET_LANGUAGE(state, language) {
      state.user.language = language
    },
    
    SET_THEME(state, theme) {
      state.theme = theme
    },
    
    UPDATE_METRICS(state, metrics) {
      state.metrics = { ...state.metrics, ...metrics }
    },
    
    ADD_ACTIVITY(state, activity) {
      state.activities.unshift(activity)
      if (state.activities.length > 100) {
        state.activities.pop()
      }
    }
  },
  
  actions: {
    changeLanguage({ commit }, language) {
      commit('SET_LANGUAGE', language)
      localStorage.setItem('cb-language', language)
    },
    
    toggleTheme({ commit, state }) {
      const newTheme = state.theme === 'light' ? 'dark' : 'light'
      commit('SET_THEME', newTheme)
      localStorage.setItem('cb-theme', newTheme)
      document.body.className = newTheme
    },
    
    updateMetrics({ commit }, metrics) {
      commit('UPDATE_METRICS', metrics)
    }
  }
})