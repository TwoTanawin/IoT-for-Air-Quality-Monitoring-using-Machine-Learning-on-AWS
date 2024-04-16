#include "secrets.h"
#include <WiFiClientSecure.h>
#include <MQTTClient.h>
#include <ArduinoJson.h>
#include "WiFi.h"
#include <Arduino.h>
#include "PMS.h"
#include <ctime>
#include <Crypto.h>
// #include <TridentTD_LineNotify.h>

// #define LINE_TOKEN "1A8i7VgRtTaik6xL8PSSFGlT1FvBjBLy5IQDhnYhEO3"

// The MQTT topics that this device should publish/subscribe
#define AWS_IOT_PUBLISH_TOPIC "esp32_2/pub"
#define AWS_IOT_SUBSCRIBE_TOPIC "esp32_2/sub"

WiFiClientSecure net = WiFiClientSecure();
MQTTClient client = MQTTClient(256);

// Declare the messageHandler function before it's used
void messageHandler(String &topic, String &payload);

const char *ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 25200;
const int daylightOffset_sec = 0;

#define MAX_TIME_STRING_LENGTH 80 // Adjust the size as per your requirement

String station_number = "1";

PMS pms(Serial);
PMS::DATA data;

unsigned long previousMillis = 0; // Variable to store the last time the interval was updated
const long interval = 1000;       // Interval in milliseconds

unsigned long previousResetMillis = 0; // Variable to store the last time the reset was done
const long resetInterval = 1800000;    // Interval to reset (in milliseconds)

void printLocalTime()
{
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo))
  {
    Serial.println("Failed to obtain time");
    return;
  }
  Serial.println(&timeinfo, "%A, %B %d %Y %H:%M:%S");
}

String getLocalTimeForDB()
{
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo))
  {
    Serial.println("Failed to obtain time");
    return "";
  }

  char timestamp[20]; // Assuming the timestamp format is YYYY-MM-DD HH:MM:SS
  snprintf(timestamp, sizeof(timestamp), "%04d-%02d-%02d %02d:%02d:%02d",
           timeinfo.tm_year + 1900, timeinfo.tm_mon + 1, timeinfo.tm_mday,
           timeinfo.tm_hour, timeinfo.tm_min, timeinfo.tm_sec);

  return String(timestamp);
}

void connectAWS()
{
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.println("Connecting to Wi-Fi");

  while (WiFi.status() != WL_CONNECTED)
  {
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

  while (!client.connect(THINGNAME))
  {
    Serial.print(".");
    delay(100);
  }

  if (!client.connected())
  {
    Serial.println("AWS IoT Timeout!");
    return;
  }

  // Subscribe to a topic
  client.subscribe(AWS_IOT_SUBSCRIBE_TOPIC);

  Serial.println("AWS IoT Connected!");

  // init and get the time
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  printLocalTime();
}

unsigned long modInverse(unsigned long a, unsigned long m)
{
  long long m0 = m, t, q;
  long long x0 = 0, x1 = 1;

  if (m == 1)
    return 0;

  // Apply extended Euclidean algorithm
  while (a > 1)
  {
    q = a / m;
    t = m;
    m = a % m, a = t;
    t = x0;
    x0 = x1 - q * x0;
    x1 = t;
  }

  if (x1 < 0)
    x1 += m0;

  return x1;
}

void encrypt(unsigned long plaintext, unsigned long e, unsigned long n, unsigned long &ciphertext)
{
  ciphertext = 1;
  for (unsigned long i = 0; i < e; ++i)
  {
    ciphertext = (ciphertext * plaintext) % n;
  }
}

void decrypt(unsigned long ciphertext, unsigned long d, unsigned long n, unsigned long &decrypted)
{
  decrypted = 1;
  for (unsigned long i = 0; i < d; ++i)
  {
    decrypted = (decrypted * ciphertext) % n;
  }
}

unsigned long p = 61;
unsigned long q = 53;
unsigned long n = p * q;
unsigned long phi_n = (p - 1) * (q - 1);
unsigned long e = 65537;
unsigned long d = modInverse(e, phi_n);

void publishMessage()
{
  int pm1, pm25, pm10;
  StaticJsonDocument<200> doc;

  String timestamp = getLocalTimeForDB();

  if (pms.read(data))
  {
    // testPMS();
    pm1 = data.PM_AE_UG_1_0;
    pm25 = data.PM_AE_UG_2_5;
    pm10 = data.PM_AE_UG_10_0;

    // Nothing to do here
    unsigned long plaintext_pm1 = pm1;
    unsigned long ciphertext_pm1;
    encrypt(plaintext_pm1, e, n, ciphertext_pm1);

      // Nothing to do here
    unsigned long plaintext_pm25 = pm25;
    unsigned long ciphertext_pm25;
    encrypt(plaintext_pm25, e, n, ciphertext_pm25);

    unsigned long plaintext_pm10 = pm10;
    unsigned long ciphertext_pm10;
    encrypt(plaintext_pm10, e, n, ciphertext_pm10);
    

    doc["timestamp"] = timestamp;
    doc["station_number"] = "1";
    doc["pm1"] = ciphertext_pm1; // Random value generation
    doc["pm25"] = ciphertext_pm25;
    doc["pm10"] = ciphertext_pm10;

    char jsonBuffer[512];
    serializeJson(doc, jsonBuffer); // print to client

    client.publish(AWS_IOT_PUBLISH_TOPIC, jsonBuffer);
  }
}

// Definition of the messageHandler function
void messageHandler(String &topic, String &payload)
{
  Serial.println("incoming: " + topic + " - " + payload);
}

void testPMS()
{

  if (pms.read(data))
  {
    Serial.print("PM 1.0 (ug/m3): ");
    Serial.println(data.PM_AE_UG_1_0);
    Serial.print("PM 2.5 (ug/m3): ");
    Serial.println(data.PM_AE_UG_2_5);
    Serial.print("PM 10.0 (ug/m3): ");
    Serial.println(data.PM_AE_UG_10_0);
    Serial.println();
  }
}

void setup()
{
  Serial.begin(9600);

  connectAWS();
}

void loop()
{
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval)
  {
    previousMillis = currentMillis;

    publishMessage();
    client.loop();
  }

  // Reset every 1 minute
  if (currentMillis - previousResetMillis >= resetInterval)
  {
    // Save the last time the reset was done
    previousResetMillis = currentMillis;
    // Perform the reset
    Serial.println("Resetting ESP32...");
    ESP.restart();
  }
}
