#include <Servo.h>

Servo servoPan;
Servo servoTilt;

const int panServoPin = 10;  // Pan servo is now on pin 10
const int tiltServoPin = 9;  // Tilt servo is now on pin 9
const int sensorPin = A0;    // Distance sensor

int panAngle = 0;
int tiltAngle = 0;

float sensorMinDist = 20;  // Minimum measurable distance (in cm)
float sensorMaxDist = 150; // Maximum measurable distance (in cm)

void setup() {
  servoPan.attach(panServoPin);
  servoTilt.attach(tiltServoPin);
  Serial.begin(9600);
}

bool running = true;

void loop() {
  if (running) {
    for (tiltAngle = 0; tiltAngle <= 90; tiltAngle += 5) {  // Increase density: smaller step size (5 degrees)
      servoTilt.write(tiltAngle);
      delay(300);  // Adjust delay for smoother movement

      for (panAngle = 0; panAngle <= 90; panAngle += 5) {  // Increase density: smaller step size (5 degrees)
        servoPan.write(panAngle);
        delay(300);  // Adjust delay for smoother movement

        int sensorValue = analogRead(sensorPin);
        float distance = map(sensorValue, 0, 1023, sensorMinDist, sensorMaxDist);  // Map sensor value to distance

        // Send pan, tilt, and distance data over serial
        Serial.print(panAngle);
        Serial.print(",");
        Serial.print(tiltAngle);
        Serial.print(",");
        Serial.println(distance);
      }
    }
    running = false;  // Stop after one scan
  }
}
