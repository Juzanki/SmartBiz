// src/i18n.js
import { createI18n } from 'vue-i18n'

// 🌍 Import all locale files
import en from './locales/en.json'
import sw from './locales/sw.json'
import fr from './locales/fr.json'
import es from './locales/es.json'
import ar from './locales/ar.json'
import zh from './locales/zh.json'
import hi from './locales/hi.json'
import pt from './locales/pt.json'
import ru from './locales/ru.json'
import de from './locales/de.json'
import ja from './locales/ja.json'
import tr from './locales/tr.json'

// 🗂️ Group messages
const messages = {
  en, sw, fr, es, ar, zh, hi, pt, ru, de, ja, tr
}

// 🌐 Create i18n instance
const i18n = createI18n({
  legacy: false,                  // Composition API support
  locale: localStorage.getItem('language') || 'en',
  fallbackLocale: 'en',
  messages
})

export default i18n
