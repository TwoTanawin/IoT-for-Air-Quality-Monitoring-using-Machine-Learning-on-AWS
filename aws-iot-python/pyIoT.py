from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

# AWS IoT Core configuration
endpoint = "a1vay9ecm5rwj1-ats.iot.ap-southeast-1.amazonaws.com"
root_ca_path = "/home/two-asus/Documents/cloudcomputing/project/free-tiar-kry/AmazonRootCA1.pem"
private_key_path = "/home/two-asus/Documents/cloudcomputing/project/free-tiar-kry/40678341dd707b2ffb000a5b48f801013641f4ba30e84c130e87642f8ca64dc6-private.pem.key"
certificate_path = "/home/two-asus/Documents/cloudcomputing/project/free-tiar-kry/40678341dd707b2ffb000a5b48f801013641f4ba30e84c130e87642f8ca64dc6-certificate.pem.crt"
client_id = "test_esp_data"

# Create an IoT MQTT client
mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint(endpoint, 8883)
mqtt_client.configureCredentials(root_ca_path, private_key_path, certificate_path)

# Connect to AWS IoT Core
mqtt_client.connect()

# JSON data to send
data = {
    "key1": "788",
    "key2": "969696",
    "key3": "007"
}

# Convert data to JSON string
payload = json.dumps(data)

# Publish JSON data to a specific IoT topic
topic = "esp32/pub"
mqtt_client.publish(topic, payload, 1)

# Disconnect from AWS IoT Core
mqtt_client.disconnect()
