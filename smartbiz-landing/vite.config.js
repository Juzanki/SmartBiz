import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite'
import path from 'node:path'

export default defineConfig({
  plugins: [
    vue(),
    UnoCSS(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // Hakikisha 'src' ni mahali ambapo folda ya views iko
    },
  },
  server: {
    hmr: {
      overlay: false, // Hii itazuia makosa yasiyohitajika kuonyeshwa
    },
  },
})