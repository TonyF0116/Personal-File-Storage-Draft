const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    // entry: './src/account/main.js',
    entry: './src/index/main.js',
    // entry: './src/edit/main.js',
  },
})
