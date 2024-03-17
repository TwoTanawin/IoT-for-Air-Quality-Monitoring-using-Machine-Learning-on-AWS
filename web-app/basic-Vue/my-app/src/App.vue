<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <section>
    <h1>Register : {{firstName}}</h1>
    <h1>Register fullname : {{ lastName }}</h1>
    <h1>Age : {{ age }}</h1>
    <p>Address : <span v-html="address"></span></p>
  </section>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // }
  data(){
    return{
      firstName:"Two",
      lastName:"Tanawin",
      age:23,
      address:"<i>Bangkok</i>"
    }
  }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */

</style>
