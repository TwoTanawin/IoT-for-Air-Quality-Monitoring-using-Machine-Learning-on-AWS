<template>
  <header>
    <h1>System Manage Employee Information</h1>
  </header>
  <section class="employee-content">
    <!-- <h1>App Component</h1> -->
    <!-- <FormComponent/> -->
    <h2>Employee Information</h2>
    <ListData/>
  </section>
</template>

<script>
// import component
import ListData from "./components/ListData.vue"
// import FormComponent from "./components/FormComponent.vue"

export default{
  name:"App",
  components:{
    ListData,
    // FormComponent
  },
  data(){
    return{
      employee:[
        {name:"Rick-c137", salary:1000},
        {name:"Morty-c137", salary:1000},
        {name:"Rick-616", salary:100},
        {name:"Morty-616", salary:100},
        {name:"Rick-a217", salary:10},
        {name:"Morty-a217", salary:10},
      ]
    }
  }
}

</script>

<style >
  /* h1{
    background: orange;
  } */
  *{
    box-sizing: border-box;
  }
  body{
    margin: 0;
  }
  header{
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    margin: 3rem;
    padding: 1rem;
    background-color: purple;
    color: white;
    text-align: center;
  }
  .employee-content{
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    margin: 3rem;
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
  }
  .employee-content h2{
    font-size: 2rem;
    border-bottom: 4px solid #ccc;
    color: purple;
    margin: 0 0 1rem 0;
  }
</style>