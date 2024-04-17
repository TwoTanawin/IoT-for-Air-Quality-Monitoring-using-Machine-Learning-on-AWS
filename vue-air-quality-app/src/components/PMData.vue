<template>
    <div class="container">
      <div class="row justify-content-center align-items-center">
        <div class="col-lg-8">
          <div class="box">
            <h4>AIR Quality Data</h4>
            <div v-if="pmData !== null" class="circle-container">
              <div class="circle" v-for="(pm, index) in pmData" :key="index">
                <p class="circle-text">PM{{ index + 1 }}: {{ pm }}</p>
              </div>
            </div>
            <div v-else>
              <p>Loading...</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    // Component logic
    name: "PMData",
    data() {
      return {
        pmData: null
      };
    },
    created() {
      this.fetchPMData();
    },
    methods: {
      async fetchPMData() {
        try {
          const response = await fetch('http://10.0.1.8:5000/get_last_data');
          const data = await response.json();
          this.pmData = data.last_data;
        } catch (error) {
          console.error('Error fetching PM data:', error);
        }
      }
    }
  };
  </script>
  
  <style>
  /* Component-specific styles go here */
  .box {
    /* height: 300px; */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .circle-container {
    display: flex;
  }
  .circle {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background-color: lightblue;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 10px;
  }
  .circle-text {
    text-align: center;
    margin: 0; /* Remove default margin to ensure text is properly centered */
  }
  </style>
  