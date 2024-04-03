#include <Arduino.h>

unsigned long previousResetMillis = 0;  // Variable to store the last time the reset was done
unsigned long previousPrintMillis = 0;  // Variable to store the last time the print statement was executed
const long resetInterval = 1300000;       // Interval to reset (in milliseconds)
const long printInterval = 1000;        // Interval to print (in milliseconds)
int i = 0;  // Variable to store the current iteration

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("System Start");
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis();

  // Reset every 1 minute
  if (currentMillis - previousResetMillis >= resetInterval) {
    // Save the last time the reset was done
    previousResetMillis = currentMillis;

    // Perform the reset
    Serial.println("Resetting ESP32...");
    ESP.restart();
  }

  // Print "ESP32 alive <current_iteration>" every 1 second
  if (currentMillis - previousPrintMillis >= printInterval) {
    // Save the last time the print statement was executed
    previousPrintMillis = currentMillis;

    // Print statement
    Serial.printf("ESP32 alive %d\n", i);
    i++;  // Increment iteration count
  }
}
