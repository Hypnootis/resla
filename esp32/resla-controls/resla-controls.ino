#include "ESP32Servo.h"

Servo servo_motor;
Servo esc_motor;

/*
	d = left
	s = straight
	l = right
*/

void setup() {
	Serial.begin(115200);
	servo_motor.attach(4);
	esc_motor.attach(5);
	Serial.println("Serial connection established");
}

void loop() {
	if (Serial.available()){
	Serial.write("hello")
	int value = Serial.read();
	Serial.write(value);

	if (value == 115){
		servo_motor.write(90);
		}

	if (value == 108){
		servo_motor.write(30);
		}
	if (value == 100){
		servo_motor.write(130);
		}
	}
}
