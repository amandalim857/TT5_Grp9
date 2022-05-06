<template>
  <div id="app">
    <EachProject/>
  </div>
</template>

<script>
// import Dashboard from '@/components/Dashboard.vue'
// import HelloWorld from './components/HelloWorld.vue'
import EachProject from './components/Project.vue'

export default {
  name: 'App',
  components: {
    EachProject
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
