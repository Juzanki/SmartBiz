<template>
  <div class="lang-switcher">
    <select v-model="currentLang" @change="switchLanguage">
      <option v-for="(label, code) in languages" :key="code" :value="code">
        {{ label }}
      </option>
    </select>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'

export default {
  setup() {
    const { locale } = useI18n()

    const languages = {
      en: 'English',
      sw: 'Kiswahili',
      fr: 'Français',
      es: 'Español',
      ar: 'العربية',
      zh: '中文',
      hi: 'हिन्दी',
      pt: 'Português',
      ru: 'Русский',
      de: 'Deutsch',
      ja: '日本語',
      tr: 'Türkçe'
    }

    const currentLang = locale

    const switchLanguage = () => {
      localStorage.setItem('language', currentLang.value)
    }

    return {
      languages,
      currentLang,
      switchLanguage
    }
  }
}
</script>

<style scoped>
.lang-switcher {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
}

select {
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
}
</style>
