/*
  This library is for the Aruino Nano on the Pibots.
  pibot_nano.cpp - Library for Pibot
  Created by Florian Zylla, June 21, 2019.
*/


#include "Arduino.h"
#include "pibot_nano_distance.h"
#include "pibot_nano_parameters.h"


distance_sensors::distance_sensors(){
  left=0;
  middle=0;
  right=0;
}

uint8_t distance_sensors::get_left(){
  return left;
}
uint8_t distance_sensors::get_middle(){
  return middle;
}
uint8_t distance_sensors::get_right(){
  return right;
}
 void distance_sensors::update(){
   if((millis()-last)>20){
        last=millis();
        switch(us_nr){
          case 0:
              left = get_distance(0);
          break;
          case 1:
              middle = get_distance(1);
          break;
          case 2:
              right = get_distance(2);
          break;
        }
        us_nr ++;
        if(us_nr>=4){
          us_nr=0;
        }
        
    }
 }

uint8_t get_distance(uint8_t sensor)
{
  uint8_t pin;
  switch(sensor){
    case 0:
        pin = US_L;
        break;
    case 1:
        pin = US_F;
        break;
    case 2:
        pin = US_R;
        break;
  }
  pinMode(pin,OUTPUT);
  digitalWrite(pin, LOW);
  delay(5);
  digitalWrite(pin, HIGH);
  delay(10);
  digitalWrite(pin, LOW);
  pinMode(pin,INPUT);
  uint32_t dauer = pulseIn(pin, HIGH,14600);
  uint16_t entfernung = (dauer/2) * 0.03432;
  if (entfernung >= 255 || entfernung <= 0)
      {
          entfernung=0;
      }
    return entfernung;
    
}