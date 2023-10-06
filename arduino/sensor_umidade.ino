#include <Wire.h>
#include <LiquidCrystal_l2C.h>
#include "DHT.h"
LiquidCrystal_l2C lcd(0x27, 20, 4);
#define DHTPIN 2 // Digital pin conenected to the DHT sensor
#define DHTTYPE DHT11 // DHT11 
DHT dht(DHTPIN, DHTTYPE);

void setup(){
    dht.begin();
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();
}

void loop(){
    float h = dht.readHumidity();

    lcd.serCursor(0,0);
    lcd.print("Umidade:");
    lcd.print(h);
    lcd.print("%");
    delay(100);
    
    if(h <= 50.0){
        lcd.setCursor(0,1);
        lcd.print("Precisa de água :|");
    } if(h >= 51.0){
        lcd.setCursor(0,1);
        lcd.print("Boa Umidade :)");
    }    
}