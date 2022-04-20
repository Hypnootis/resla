#include <ESP32Servo.h>

String nom = "ESP32";
String msg;
Servo steering;
Servo motor;

void setup() {
	Serial.begin(921600);
	steering.attach(4);
	motor.attach(5);
}

void loop() {
	readSerialPort();

	if (msg != ""){
		if (msg == "left"){
			steering.write(130);
		}

		if (msg == "right"){
		
			steering.write(30);
		}

		if (msg == "straight"){
			steering.write(90);
		}

		if (msg == "forward"){
			motor.write(90);
			delay(50);
			motor.write(95);
		}

		if (msg == "backward"){
		motor.write(90);
		delay(50);
		motor.write(85);
		}

		if (msg == "stop"){
		motor.write(90);
		}

	sendData();
	}
}

void readSerialPort(){
	msg = "";
	if (Serial.available()){
	delay(10);
	while (Serial.available() > 0){
		msg += (char)Serial.read();
		}
	Serial.flush();
	}	
}

void sendData(){
	Serial.print(nom);
	Serial.print(" received: ");
	Serial.print(msg);
}
