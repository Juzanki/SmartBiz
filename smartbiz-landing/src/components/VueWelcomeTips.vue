<script setup>
import WelcomeItem from "./WelcomeItem.vue";
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";

const openReadmeInEditor = () => fetch("/__open-in-editor?file=README.md");
</script>

<template>
  <!-- Documentation -->
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Documentation</template>
    Vue’s
    <a href="https://vuejs.org/" target="_blank" rel="noopener">
      official documentation
    </a>
    provides you with all information you need to get started.
  </WelcomeItem>

  <!-- Tooling -->
  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Tooling</template>
    This project is served and bundled with
    <a href="https://vite.dev/guide/features.html" target="_blank" rel="noopener">Vite</a>.
    The recommended IDE setup is
    <a href="https://code.visualstudio.com/" target="_blank" rel="noopener">VSCode</a> +
    <a href="https://github.com/johnsoncodehk/volar" target="_blank" rel="noopener">Volar</a>.
    <br />
    For testing: use
    <a href="https://vitest.dev/" target="_blank" rel="noopener">Vitest</a>,
    <a href="https://www.cypress.io/" target="_blank" rel="noopener">Cypress</a>,
    or
    <a href="https://playwright.dev/" target="_blank" rel="noopener">Playwright</a>.
    <br /><br />
    More instructions:
    <a href="javascript:void(0)" @click="openReadmeInEditor">
      <code>README.md</code>
    </a>
  </WelcomeItem>

  <!-- Ecosystem -->
  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Ecosystem</template>
    Official tools:
    <a href="https://pinia.vuejs.org/" target="_blank" rel="noopener">Pinia</a>,
    <a href="https://router.vuejs.org/" target="_blank" rel="noopener">Vue Router</a>,
    <a href="https://test-utils.vuejs.org/" target="_blank" rel="noopener">Vue Test Utils</a>,
    <a href="https://github.com/vuejs/devtools" target="_blank" rel="noopener">Vue Dev Tools</a>.
    <br />
    More resources at
    <a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">Awesome Vue</a>.
  </WelcomeItem>

  <!-- Community -->
  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Community</template>
    Ask for help on
    <a href="https://chat.vuejs.org" target="_blank" rel="noopener">Vue Land</a>,
    <a href="https://stackoverflow.com/questions/tagged/vue.js" target="_blank" rel="noopener">StackOverflow</a>,
    or follow
    <a href="https://bsky.app/profile/vuejs.org" target="_blank" rel="noopener">@vuejs.org</a> /
    <a href="https://x.com/vuejs" target="_blank" rel="noopener">@vuejs</a>.
  </WelcomeItem>

  <!-- Support -->
  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Support Vue</template>
    Vue relies on community support.
    <a href="https://vuejs.org/sponsor/" target="_blank" rel="noopener">Become a sponsor</a>.
  </WelcomeItem>
</template>
