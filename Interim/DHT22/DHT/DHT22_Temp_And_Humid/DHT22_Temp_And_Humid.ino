#include <ESP8266WiFi.h>
#include <Wire.h>
//#include <LiquidCrystal_I2C.h>
#include "DHT.h"
#define DHTTYPE DHT22
#define LED D5
#define LED_E D3
//LiquidCrystal_I2C lcd(0x27, 20, 4);
const int EMERGENCY_TEMP = 30;

String apiKey = "WVS008D7H1T3EW43";


const char* ssid = "Untrusted Network";
const char* password = "RJ45@RJ45";

const char* server = "api.thingspeak.com";


const int DHTPin = 2;
DHT dht(DHTPin, DHTTYPE);

WiFiClient client;



void setup() {
  pinMode(LED_E, OUTPUT);

//  lcd.begin();
 // lcd.backlight();


  Serial.begin(9600);
  delay(500);
  dht.begin();
  delay(500);

  WiFi.begin(ssid, password);
  Serial.println("");

  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);


  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");

    digitalWrite(LED, LOW);
    delay(250);
    digitalWrite(LED, HIGH);
    delay(250);

  }

  digitalWrite(LED, HIGH);

  Serial.println("");
  Serial.print("Successfully connected to : ");
  Serial.println(ssid);
}

void loop() {

  float h = dht.readHumidity();
  float t = dht.readTemperature();



  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  if (t > EMERGENCY_TEMP) {
    
    digitalWrite(LED_E, HIGH);

  }
  else {
    
    digitalWrite(LED_E, LOW);

  }

  if (client.connect(server, 80))  {
    String postStr = apiKey;
    postStr += "&field1=";
    postStr += String(t);
    postStr += "&field2=";
    postStr += String(h);
    postStr += "\r\n\r\n";

    client.print("POST /update HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n");
    client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
    client.print("Content-Type: application/x-www-form-urlencoded\n");
    client.print("Content-Length: ");
    client.print(postStr.length());
    client.print("\n\n");
    client.print(postStr);



    Serial.print("Temperature: ");
    Serial.print(t);
    Serial.print(" degrees Celcius, Humidity: ");
    Serial.print(h);
    Serial.println("%. Send to Thingspeak.");


   // lcd.setCursor(0, 0);
   // lcd.print("Temp: ");
   // lcd.setCursor(6, 0);
   // lcd.print(t);
   // lcd.setCursor(11, 0);
   // lcd.print(" C");
   // lcd.setCursor(0, 1);
   // lcd.print("Humid: ");
   // lcd.setCursor(6, 1);
   // lcd.print(h);
   // lcd.setCursor(11, 1);
   // lcd.print(" %");



  }
  client.stop();
  Serial.println("Waiting...");

  digitalWrite(LED, LOW);
  delay(250);
  digitalWrite(LED, HIGH);

  delay(2000);

}
