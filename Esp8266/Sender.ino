#ifndef UNIT_TEST
#include <Arduino.h>
#endif
#include <IRremoteESP8266.h>
#include <IRsend.h>
#define LED_BUILIT 2
#define IR_LED 4  // ESP8266 GPIO pin to use. Recommended: 4 (D2).

IRsend irsend(IR_LED);  // Set the GPIO to be used to sending the message.

void setup() {
  irsend.begin();
  Serial.begin(115200);
  pinMode(13,INPUT);
  pinMode(LED_BUILIT,OUTPUT);
}

void loop() {

irsend.sendNEC(33706159,32);
Serial.println(0x20250AF);
delay(1000);

}