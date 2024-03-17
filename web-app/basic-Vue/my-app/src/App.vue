<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <section>
    <!-- <h1>Register : {{firstName}}</h1> -->
    <img :src="picture" :width="size" :height="size" ref="imagesURL"><br>
    <!-- Midle Name : <input type="text" v-on:input="setMidleName"/> -->
    <form @submit.prevent="submitForm">
      <label>Input Midle Name :</label>
      <!-- <input type="text" v-on:input="setMidleName" ref="midleNameEL"/> -->
      <input type="text" ref="midleNameEL" />
      <button type="submit">submit</button>
    </form>

    <h1>Register fullname : {{ getFullName }}</h1>
    <h2>Midle Name : {{ midleName }}</h2>
    <h1>Age : {{ age }}</h1>
    <h1>Salary : ${{ salary }}</h1>
    <h1>Annual income : ${{ getIncome }}</h1>
    <h1>Position : {{ getPosition }}</h1><br>
    <button @click="inCrementSalary(1000000000)">Increase Salary</button>
    <button @click="deCrementSalary(1000000000)">Decrease Salary</button><br>
    <!-- <h2>Method1 : {{ getRandombyMethod() }}</h2>
    <h2>Method2 : {{ getRandombyMethod() }}</h2>
    <h2>Method3 : {{ getRandombyMethod() }}</h2>
    <hr/>
    <h2>Compute1 : {{ getRandombyComputed }}</h2>
    <h2>Compute2 : {{ getRandombyComputed }}</h2>
    <h2>Compute3 : {{ getRandombyComputed }}</h2> -->
    
    <button @click="toggleVisible">{{ isVisible ? "Hidde": "Show" }} Detial</button>
    <article v-show="isVisible">
      <p>Address : <span v-html="address"></span></p>
      <p>Social : <a :href="social" target="_blank">Dune Part Two</a></p>

      <p v-if="hobby.length === 0">No Hobbies</p>
      <div v-else>
        <p>Hobbies</p>
        <ul>
          <!-- <li>{{ hobby[0] }}</li>
        <li>{{ hobby[1] }}</li>
        <li>{{ hobby[2] }}</li> -->
          <li v-for="(item, index) in hobby" :key="index">{{ item }}</li>
        </ul>
      </div>

      <p>General Data :</p>
      <ul>
        <!-- <li>Gender : {{ general.gender }}</li>
      <li>Weight : {{ general.weigh }} Kg</li>
      <li>Height : {{ general.height }} Cm</li> -->
        <li v-for="(item, key) in general" :key="key">{{ item }}</li>
      </ul>
    </article>

  </section>

  <button @click="showData">Shows Data</button>
  <button @click.ctrl="inCrement(10)">Increase</button>
  <button @click.middle="deCrement(10)">Decrease</button>
</template>

<script>
// import { values } from 'core-js/core/array';

// import { defineSSRCustomElement } from 'vue';

// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  // components: {
  //   HelloWorld
  // }
  data() {
    return {
      firstName: "Pual",
      lastName: "Atreides",
      midleName: "",
      age: 23,
      address: "<i>Bangkok</i>",
      picture: "https://variety.com/wp-content/uploads/2020/09/dune-warner-bros-e1600210676962.jpg",
      size: 500,
      social: "https://en.wikipedia.org/wiki/Dune:_Part_Two",
      hobby: ["Ride Worms", "Attack the Impire", "Procuce Sprite"],
      general: { gender: "Male", weigh: 65, height: 185, status: false },
      isVisible:false,
      salary:20000000,
    }
  },

  methods: {
    // getFullName() {
    //   // return this.firstName + this.lastName
    //   return `${this.firstName + " " + this.lastName}`
    // },
    showData() {
      alert(this.firstName + " " + this.lastName)
    },
    inCrement(value) {
      this.age += value
    },
    inCrementSalary(value) {
      this.salary += value
    },

    deCrement(value) {
      this.age -= value
    },
    deCrementSalary(value) {
      this.salary -= value
    },
    // setMidleName(event){
    //   // console.log(event.target.value)
    //   this.midleName=event.target.value
    // },
    submitForm() {
      // e.preventDefault()
      // alert("Submit Success")
      // console.log(this.$refs.imagesURL)
      this.midleName = this.$refs.midleNameEL.value
    },
    toggleVisible(){
      this.isVisible = !this.isVisible
    },
    getRandombyMethod(){
      return Math.random()
    }
  },
  computed:{
    getFullName() {
      // return this.firstName + this.lastName
      return `${this.firstName + " " + this.lastName}`
    },
    getRandombyComputed(){
      return Math.random()
    },
    getIncome(){
      return this.salary*12
    },
    getPosition(){
      return this.salary >= 20000 ? "lisan al gaib" : "muad'dib"
    }
  },

  watch:{
    salary(value){
      if(value > 5000000000){
        alert("!Lisan Al Gaib!");
        setTimeout(()=>{
          this.salary = 20000000
        }, 2000)
      }
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
