<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/>
    <LoginPage></LoginPage> -->
    <Dashboard></Dashboard>
    <!-- <EachProject/> -->
  </div>
</template>

<script>
import Dashboard from '@/components/Dashboard.vue'
// import HelloWorld from './components/HelloWorld.vue'
// import LoginPage from './components/Login.vue'
// import EachProject from './components/Project.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld,
    Dashboard,
    // LoginPage,
    // EachProject
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
