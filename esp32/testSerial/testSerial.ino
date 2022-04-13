String nom = "ESP32";
String msg;


void setup() {
	Serial.begin(115200);
}

void loop() {
	readSerialPort();

	if (msg != ""){
	sendData();
	}
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
