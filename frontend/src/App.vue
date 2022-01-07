<template>
  <div id="app">
    <GiveMeTheOdds/>
  </div>
</template>

<script>
import GiveMeTheOdds from './components/GiveMeTheOdds.vue'

export default {
  name: 'App',
  components: {
    GiveMeTheOdds
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
