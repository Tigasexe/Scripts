#define sensor A0

void setup(){
    pinMode(sensor, INPUT);
    Serial.begin(9600);
}

void loop(){
    Serial.print("Sensor:");
    Serial.println(analogRead(sensor));
    delay(1000);
}