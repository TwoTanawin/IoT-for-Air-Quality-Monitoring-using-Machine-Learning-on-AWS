<!-- App.vue -->
<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <p><strong>Rangsit</strong> Air Pollution: Real-time Air Quality Index (AQI)</p>
      </div>
    </nav>


    <div class="container mt-4">
      <AirQuality />
      <PMData />
      <DataChart />
    </div>

    <footer class="footer">
      <div class="container">
        <span class="text-muted">Developed By Tanawin Mechatronics and Machine Intelligence</span>
      </div>
    </footer>
  </div>
</template>


<script>
import AirQuality from './components/AirQuality.vue';
import PMData from './components/PMData.vue';
import DataChart from './components/DataChart.vue';
import 'bootstrap/dist/css/bootstrap.min.css';


export default {
  components: {
    AirQuality,
    PMData,
    DataChart
  }
};
</script>

<style>
/* Global styles or component-specific styles go here */
.box {
  background-color: #f0f0f0;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 5px;
}

.footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: #f8f9fa;
  text-align: center;
}

.navbar {
  display: flex;
  justify-content: center; /* Horizontally center */
  align-items: center; /* Vertically center */
  height: 100%; /* Ensure full height */
  margin: 0;
}

.navbar p {
  margin: 0; /* Remove default margin */
  font-size: 25px;
  font-family: Arial;
  text-align: center;
}

.navbar .container-fluid p {
        text-align: center;
        margin: 0; /* Optional: Removes any default margin */
    }

</style>
