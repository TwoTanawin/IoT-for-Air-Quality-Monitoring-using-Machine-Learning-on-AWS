<template>
    <div class="container">
      <div class="row justify-content-center align-items-center">
        <div class="col-lg-8">
          <div class="box">
            <h4>Current Data Last 10 Time</h4>
            <canvas ref="lineChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js/auto';
  
  export default {
    // Component logic
    name: "DataChart",
    mounted() {
      this.fetchDataAndPlotChart();
    },
    methods: {
      async fetchDataAndPlotChart() {
        try {
          const response = await fetch('http://10.0.1.8:5000/get_last_10_data');
          const data = await response.json();
          this.plotChart(data.last_10_data);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
      plotChart(data) {
        const timestamps = data.map(item => item[Object.keys(item)[0]][3]); // Extract timestamps
        const pm1Data = data.map(item => parseInt(item[Object.keys(item)[0]][0]));
        const pm25Data = data.map(item => parseInt(item[Object.keys(item)[0]][1]));
        const pm10Data = data.map(item => parseInt(item[Object.keys(item)[0]][2]));
  
        const ctx = this.$refs.lineChart.getContext('2d');
        new Chart(ctx, {
          type: 'line',
          data: {
            labels: timestamps, // Use timestamps as x-axis labels
            datasets: [
              {
                label: 'PM1',
                data: pm1Data,
                borderColor: 'red',
                fill: false
              },
              {
                label: 'PM2.5',
                data: pm25Data,
                borderColor: 'blue',
                fill: false
              },
              {
                label: 'PM10',
                data: pm10Data,
                borderColor: 'green',
                fill: false
              }
            ]
          },
          options: {
            scales: {
              x: {
                title: {
                  display: true,
                //   text: 'Timestamp'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'AIR Quality'
                }
              }
            }
          }
        });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Component-specific styles go here */
  .box {
    height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  </style>
  