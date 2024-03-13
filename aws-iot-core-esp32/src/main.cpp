#include "secrets.h"
#include <WiFiClientSecure.h>
#include <MQTTClient.h>
#include <ArduinoJson.h>
#include "WiFi.h"
#include <Arduino.h>

// The MQTT topics that this device should publish/subscribe
#define AWS_IOT_PUBLISH_TOPIC   "esp32/pub"
#define AWS_IOT_SUBSCRIBE_TOPIC "esp32/sub"

WiFiClientSecure net = WiFiClientSecure();
MQTTClient client = MQTTClient(256);

// Declare the messageHandler function before it's used
void messageHandler(String &topic, String &payload);

void connectAWS()
{
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.println("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  // Configure WiFiClientSecure to use the AWS IoT device credentials
  net.setCACert(AWS_CERT_CA);
  net.setCertificate(AWS_CERT_CRT);
  net.setPrivateKey(AWS_CERT_PRIVATE);

  // Connect to the MQTT broker on the AWS endpoint we defined earlier
  client.begin(AWS_IOT_ENDPOINT, 8883, net);

  // Create a message handler
  client.onMessage(messageHandler);

  Serial.print("Connecting to AWS IOT");

  while (!client.connect(THINGNAME)) {
    Serial.print(".");
    delay(100);
  }

  if(!client.connected()){
    Serial.println("AWS IoT Timeout!");
    return;
  }

  // Subscribe to a topic
  client.subscribe(AWS_IOT_SUBSCRIBE_TOPIC);

  Serial.println("AWS IoT Connected!");
}

void publishMessage()
{
  StaticJsonDocument<200> doc;
  // Get current time in milliseconds since the program started
  unsigned long currentTimeMillis = millis();

  // Convert milliseconds to hours, minutes, and seconds
  int hours = (currentTimeMillis / 3600000) % 24; // 1 hour = 3600000 milliseconds
  int minutes = (currentTimeMillis / 60000) % 60;   // 1 minute = 60000 milliseconds
  int seconds = (currentTimeMillis / 1000) % 60;    // 1 second = 1000 milliseconds

  // Format the time as a string in "%H:%M:%S" format
  char formattedTime[9]; // HH:MM:SS + null terminator
  sprintf(formattedTime, "%02d:%02d:%02d", hours, minutes, seconds);

  // Update the time in your document
  doc["time"] = formattedTime;

  doc["random_value"] = random(0, 100); // Random value generation
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer); // print to client

  client.publish(AWS_IOT_PUBLISH_TOPIC, jsonBuffer);
}

// Definition of the messageHandler function
void messageHandler(String &topic, String &payload) {
  Serial.println("incoming: " + topic + " - " + payload);

//  StaticJsonDocument<200> doc;
//  deserializeJson(doc, payload);
//  const char* message = doc["message"];
}

void setup() {
  Serial.begin(115200);
  connectAWS();
}

void loop() {
  publishMessage();
  client.loop();
  delay(1000);
}
