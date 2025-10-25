#include <Arduino.h>
#include "HX711.h"
#include "DHT.h"
#define DHTTYPE DHT22
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#define LED D5
// Set the LCD address to 0x27 for a 16 chars and 2 line display
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
WiFiUDP udp;
LiquidCrystal_I2C lcd(0x27, 16, 2);
const int DESIRED_TEMP = 30;
const char* ssid = "HUAWEI Y7 2019";
const char* password = "Visal1234";
const char* udpServerIP = "192.168.43.28";  // Replace with the IP address of the receiving server
const int udpServerPort = 8888;

const int DHTPin = 2;
DHT dht(DHTPin, DHTTYPE);

const int LOADCELL_DOUT_PIN = 12;
const int LOADCELL_SCK_PIN = 13;

HX711 scale;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.print("Connected. IP address: ");
  Serial.println(WiFi.localIP());

  // Initialize UDP
  udp.begin(udpServerPort);
  // delay(500);
  dht.begin();

  lcd.begin();

  // Turn on the blacklight and print a message.
  lcd.backlight();
  pinMode(LED, OUTPUT);

  Serial.println("Initializing the scale");

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);

  Serial.println("Before setting up the scale:");
  Serial.print("read: \t\t");
  Serial.println(scale.read());
  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));
  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);


  scale.set_scale(-440);
  scale.tare();

  Serial.println("After setting up the scale:");

  Serial.print("read: \t\t");
  Serial.println(scale.read());
  Serial.print("get value: \t\t");
  Serial.println(scale.get_value(5));
  Serial.print("get units: \t\t");
  Serial.println(scale.get_units(5), 1);
  Serial.println("Readings:");
}

void loop() {

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  if (t < DESIRED_TEMP) {

    digitalWrite(LED, LOW);

  }
  else {

    digitalWrite(LED, HIGH);

  }

  //Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" , ");
  Serial.print(h);
  Serial.print(" ,");

  Serial.print("\t");
  Serial.print(scale.get_units(), 1);
  Serial.println("g");

  String dataToSend = String(t) + "," + String(h) + "," + String(scale.get_units(), 1);

  // Send the data
  udp.beginPacket(udpServerIP, udpServerPort);
  udp.print(dataToSend);
  udp.endPacket();

  lcd.setCursor(0, 0);
  lcd.print("Weight: ");
  lcd.print(scale.get_units(), 1);
  lcd.setCursor(0, 1);
  lcd.print(t);
  lcd.setCursor(5, 1);
  lcd.print("C");
  lcd.setCursor(8, 1);
  lcd.print(h);
  lcd.setCursor(13, 1);
  lcd.print("%");


  scale.power_down();
  delay(5000);
  scale.power_up();
  lcd.setCursor(0, 0);
  lcd.print("                ");
}
