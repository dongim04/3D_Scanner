#include <Servo.h>

Servo servoPan;
Servo servoTilt;

const int panServoPin = 9;
const int tiltServoPin = 10;
const int sensorPin = A0;

int panAngle = 0;
int tiltAngle = 0;

float sensorMinDist = 20;
float sensorMaxDist = 150;

void setup() {
  servoPan.attach(panServoPin);
  servoTilt.attach(tiltServoPin);
  Serial.begin(9600);
}

bool running = true;

void loop() {
  if (running) {
    for (tiltAngle = 0; tiltAngle <= 90; tiltAngle += 10) {
      servoTilt.write(tiltAngle);
      delay(500);

      for (panAngle = 0; panAngle <= 180; panAngle += 10) {
        servoPan.write(panAngle);
        delay(500);

        int sensorValue = analogRead(sensorPin);
        float distance = map(sensorValue, 0, 1023, sensorMinDist, sensorMaxDist);  // calibration

        Serial.print(panAngle);
        Serial.print(",");
        Serial.print(tiltAngle);
        Serial.print(",");
        Serial.println(distance);
      }
    }
    running = false;
  }
}
