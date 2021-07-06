/*
  pibot_nano.h - Library for Arduino Nano on Pibot by Roboschool .
  Created by Florian Zylla, June 21, 2019.
  Edited by Felix Kettner.

*/
#ifndef pibot_nano_h
#define pibot_nano_h

#include "Arduino.h"
#include "pibot_nano_serial.h"
#include "pibot_nano_order.h"
#include "pibot_nano_parameters.h"

void pibot_nano_init();
uint16_t get_battery_voltage(void);
void set_motors(int8_t left_speed, int8_t right_speed);
void encoder_left();
void encoder_right();
int16_t get_encoder(uint8_t nr);
int16_t get_line_sensor(uint8_t nr);
void reset_encoders(void);
void buzzer(uint16_t frequency, uint16_t duration);
void stat_led(boolean state);
int16_t get_color(void);

#endif

