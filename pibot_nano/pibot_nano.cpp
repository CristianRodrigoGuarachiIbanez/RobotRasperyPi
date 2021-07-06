/*
  This library is for the Aruino Nano on the Pibots.
  pibot_nano.cpp - Library for Pibot
  Created by Florian Zylla, June 21, 2019.
  Edited by Felix Kettner.
*/


#include "Arduino.h"
//#include "Servo.h"
#include "pibot_nano.h"
#include "pibot_nano_serial.h"
#include "pibot_nano_order.h"
#include "pibot_nano_parameters.h"

    //motors
    int8_t v_max=100; //max. speed limit changeable (0<=v_max<=127)
    
    void set_motors(int8_t left_speed, int8_t right_speed)
    {
        //turn off both canals
        analogWrite(R_speed,0);
        analogWrite(L_speed,0);
        digitalWrite(R_dir,LOW);
        digitalWrite(L_dir,LOW);

        //detect backward driving and set phase pin
        if(right_speed<0)
        {
            digitalWrite(R_dir,HIGH);
        }

        if(left_speed<0)
        {
            digitalWrite(L_dir,HIGH);
        }

        //make parameters positive
        if(left_speed<0)
        {
            left_speed=left_speed*-1;
        }

        if(right_speed<0)
        {
            right_speed=right_speed*-1;
        }

        //detect and change too high values
        if(left_speed>v_max)
        {
            left_speed=v_max;
        }
        if(right_speed>v_max)
        {
            right_speed=v_max;
        }

        //set speed
        analogWrite(R_speed,right_speed);
        analogWrite(L_speed,left_speed);

        return;
    }
        
    uint16_t get_battery_voltage(void)
    {
        return (analogRead(BAT)/1023.0)*10000;
    }
        
    volatile int16_t ticks_left=0;
    volatile int16_t ticks_right=0;

    void encoder_left()
    {
        if(digitalRead(L_OUT1)==digitalRead(L_OUT2))
            ticks_left++;
        else
            ticks_left--;
    }

    void encoder_right()
    {
        if(digitalRead(R_OUT1)==digitalRead(R_OUT2))
            ticks_right--;
        else
            ticks_right++;
    }

    int16_t get_encoder(uint8_t nr)
    {
        switch(nr){
            case 0:
                return ticks_left;
            break;
                case 1:
                return ticks_right;
            break;
        }
    }
    
    int16_t get_line_sensor(uint8_t nr)
    {
        switch(nr){
            case 0:
                return analogRead(LS_0);
                break;
            case 1:
                return analogRead(LS_1);
                break;
            case 2:
                return analogRead(LS_2);
                break;
        }
    }

    void reset_encoders(void)
    {
        ticks_left = 0;
        ticks_right = 0;
    }

    //buzzer
    void buzzer(uint16_t frequency, uint16_t duration)
    {
        tone(BUZZER,frequency,(uint32_t) duration);
    }

    //status led 
    void stat_led(boolean state)
    {
        digitalWrite(STAT_LED,state);
    }
    
    //colorsensor
    int16_t get_color(void)
    {
        return pulseIn(CS, LOW);
    }
    
    //init function
    void pibot_nano_init()
    {
        buzzer(3000,200);
        //turn off motors
        set_motors(0,0);
        pinMode(R_dir,  OUTPUT);
        pinMode(R_speed,OUTPUT);
        pinMode(L_dir,  OUTPUT);
        pinMode(L_speed,OUTPUT);
        pinMode(R_OUT1, INPUT);
        pinMode(R_OUT2, INPUT);
        pinMode(L_OUT1, INPUT);
        pinMode(L_OUT2, INPUT);
        pinMode(BAT,    INPUT);
        //pinMode(B_L,    INPUT_PULLUP);
        //pinMode(B_R,    INPUT_PULLUP);
        //pinMode(B_B,    INPUT_PULLUP);
        pinMode(STAT_LED, OUTPUT);
        pinMode(BUZZER, OUTPUT);
        pinMode(SERVO, OUTPUT);
        pinMode(LS_0, INPUT);
        pinMode(LS_1, INPUT);
        pinMode(LS_2, INPUT);
        pinMode(CS, INPUT);
        stat_led(1);
        //Serial.begin(9600);
        // Serial.println(get_battery_voltage());
        delay(100);
        attachInterrupt(digitalPinToInterrupt(L_OUT1),encoder_left,CHANGE);
        attachInterrupt(digitalPinToInterrupt(R_OUT1),encoder_right,CHANGE);
        stat_led(0);
        Serial.begin(SERIAL_BAUD);
        Serial.flush();
        boolean connection = false;
        while(!connection){
            if(Serial.available())
            {
                buzzer(6000,100);
                Order order_received = read_order();
                if(order_received == START)
                {
                connection = true;
                write_order(CONNECTED);
                
                }
            }
       }
    }

