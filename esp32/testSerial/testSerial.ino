#include <ESP32Servo.h>

String nom = "ESP32";
String msg;
Servo steering;


void setup() {
	Serial.begin(115200);
	steering.attach(4);
}

void loop() {
	readSerialPort();

	if (msg != ""){
		if (msg == "left"){
			steering.write(130);
		}
		else if (msg == "right"){
		
			steering.write(30);
		}
		else if (msg == "straight"){
			steering.write(90);
		}
	sendData();
	}
	/*
	if (Serial.available()){
		delay(10);
		while (Serial.available() > 0){
			
	}
	}
*/
	 delay(500);
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
