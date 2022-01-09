<template>
  <div id="app">
    <GiveMeTheOdds/>
    <div id="footer">
        Background by <a href="https://unsplash.com/@andyjh07?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Andy Holmes</a> on <a href="https://unsplash.com/s/photos/space?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
    </div>
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
body {
    margin: 0px;
    background: url("./assets/andy-holmes-rCbdp8VCYhQ-unsplash.jpg") no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}
#footer {
    position: fixed;
    bottom:0%;
    width:100%;
    color:white;
    background-color:#292354;
    display:flex;
    justify-content: flex-end;
}
#footer a {
    color:white;
    padding:0px 5px;
}
</style>
