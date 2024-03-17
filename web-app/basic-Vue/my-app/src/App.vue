<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <section>
    <!-- <h1>Register : {{firstName}}</h1> -->
    <img :src="picture" :width="size" :height="size">
    <h1>Register fullname : {{ getFullName() }}</h1>
    <h1>Age : {{ age }}</h1>
    <p>Address : <span v-html="address"></span></p>
    <p>Social : <a :href="social" target="_blank">Dune Part Two</a></p>
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
      firstName:"Pual",
      lastName:"Atreides",
      age:23,
      address:"<i>Bangkok</i>",
      picture:"https://variety.com/wp-content/uploads/2020/09/dune-warner-bros-e1600210676962.jpg",
      size:500,
      social:"https://en.wikipedia.org/wiki/Dune:_Part_Two",
    }
  },
  methods:{
    getFullName(){
      // return this.firstName + this.lastName
      return `${this.firstName+" "+this.lastName}`
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
