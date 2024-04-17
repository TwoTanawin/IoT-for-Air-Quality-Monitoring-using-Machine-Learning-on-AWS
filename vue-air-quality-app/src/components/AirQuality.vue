<template>
    <div class="container text-center">
        <div class="row justify-content-center align-items-center">
            <div class="col-lg-8">
                <div class="box">
                    <div class="header">
                        <h2>Rangsit AQI </h2>
                        <div class="prediction-box" :style="{ backgroundColor: getPredictionColor(predictionResult) }"> <!-- Apply dynamic background color -->
                            <p class="prediction-text">{{ predictionResult }}</p>
                            <div v-if="predictionResult !== null">
                                <!-- Any other content -->
                            </div>
                            <div v-else>
                                <p>Loading...</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    // Component logic
    name: "AirQuality",
    data() {
        return {
            predictionResult: null
        };
    },
    created() {
        this.fetchPrediction();
    },
    methods: {
        async fetchPrediction() {
            try {
                console.log("Fetching prediction...");
                const response = await fetch('http://10.0.1.8:5000/get_ML_prediction');
                console.log("Response:", response);
                const data = await response.json();
                console.log("Data:", data);
                this.predictionResult = data.prediction;
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        getPredictionColor(prediction) {
            switch (prediction) {
                case "Good":
                    return "rgb(0, 128, 0)"; // Green
                case "Moderate":
                    return "rgb(255, 255, 0)"; // Yellow
                case "Unhealthy for sensitive":
                    return "rgb(255, 165, 0)"; // Orange
                case "Unhealthy":
                    return "rgb(255, 0, 0)"; // Red
                case "Hazardous":
                    return "rgb(128, 0, 128)"; // Purple
                default:
                    return "white"; // Default color
            }
        }
    }
};
</script>

<style scoped>
/* Component-specific styles go here */
.box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.prediction-box {
    border: 2px solid #000;
    border-radius: 5px;
    padding: 10px;
    text-align: center;
    margin-left: 10px;
    align-items: center;
    align-content: center;
}

.prediction-text {
    font-family: Arial, sans-serif;
    font-size: 30px;
    color: #333;
    font-weight: bold;
    margin: 0;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
