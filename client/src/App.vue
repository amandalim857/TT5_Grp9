<template>
  <div id="app">
<<<<<<< Updated upstream
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <LoginPage></LoginPage>
    <Dashboard></Dashboard>
=======
    <EachProject/>
>>>>>>> Stashed changes
  </div>
</template>

<script>
<<<<<<< Updated upstream
import Dashboard from '@/components/Dashboard.vue'
import HelloWorld from './components/HelloWorld.vue'
import LoginPage from './components/Login.vue'
=======
// import Dashboard from '@/components/Dashboard.vue'
// import HelloWorld from './components/HelloWorld.vue'
import EachProject from './components/Project.vue'
>>>>>>> Stashed changes

export default {
  name: 'App',
  components: {
<<<<<<< Updated upstream
    HelloWorld,
    Dashboard,
    LoginPage
=======
    EachProject
>>>>>>> Stashed changes
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
