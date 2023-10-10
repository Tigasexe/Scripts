#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include "DHT.h"

LiquidCrystal_I2C lcd(0x27, 20, 4);

#define DHTPIN1 3
#define DHTPIN2 4
#define DHTPIN3 5

#define DHTTYPE DHT11   // DHT 11

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
DHT dht3(DHTPIN3, DHTTYPE);

void setup() {
  dht1.begin();
  dht2.begin();
  dht3.begin();
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
}

void loop(){
  float h1 = dht1.readHumidity();
  float h2 = dht2.readHumidity();
  float h3 = dht3.readHumidity();

  lcd.setCursor (1,0);
  lcd.print ("Umidade plantinhas");
  delay(100);

  lcd.setCursor (0,1);
  lcd.print ("________");
  delay(100);
  
  lcd.setCursor (0,2);
  lcd.print ("plant1 plant2 plant3");
  delay(100);

  lcd.setCursor (1,3);
  lcd.print (h1);
  lcd.print ("%");

  lcd.setCursor (8,3);
  lcd.print (h2);
  lcd.print ("%");

  lcd.setCursor (15,3);
  lcd.print (h3);
  lcd.print ("%");
  delay(100);
}