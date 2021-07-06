#include <Arduino.h>

#include "pibot_nano.h"
#include "pibot_nano_distance.h"
#include "Servo.h"

//#include "pibot_nano_order.h"
//#include "pibot_nano_serial.h"

distance_sensors distance;
Servo servo;

void setup()
{
  
  // Init Serial
  pibot_nano_init();
  servo.attach(SERVO);
  servo.write(0);
  
}
void loop()
{
  get_messages_from_serial();
  //if(check_bumpers()){
//      set_motors(0,0);
 //  }
 distance.update();
}
   //Serial
        void get_messages_from_serial()
        {
        if(Serial.available() > 0)
        {
            // The first byte received is the instruction
            Order order_received = read_order();
            switch(order_received)
            {
                case VOLTAGE:
                {
                    write_i16(get_battery_voltage());
                    break;
                }
                case STATUS_LED:
                {
                    int8_t state = read_i8();
                    if(state==0){
                        stat_led(0);
                    }
                    else{
                        stat_led(1);  
                    }
                    break;
                }
                case BUZ:
                {
                    
                    uint16_t freq = read_ui16();
                    uint16_t dur = read_ui16();
                    buzzer(freq,dur); 
                    break;
                }
                case MOTORS:
                {
                    int8_t left = read_i8();
                    int8_t right = read_i8();
                    set_motors(left,right); 
                    break;
                }
                case DISTANCES:
                {
                    write_ui8(distance.get_left());
                    write_ui8(distance.get_middle());
                    write_ui8(distance.get_right());
                    break;
                }
                case GET_ENCODERS:
                {
                    write_i16(get_encoder(0));
                    write_i16(get_encoder(1));
                    break;
                }
                case GET_LINE_SENSORS:
                {
                    write_i16(get_line_sensor(0));
                    write_i16(get_line_sensor(1));
                    write_i16(get_line_sensor(2));
                    break;
                }
                case RESET_ENCODERS:
                {
                    reset_encoders();
                    break;
                }
                case BUZZER:
                {
                    stat_led(1);
                    uint16_t freq = 2000;//read_ui16();
                    uint16_t dur = 2000;// read_ui16();
                    buzzer(freq,dur); 
                    break;
                }
                case GRIPPER:
                {
                    int8_t state = read_i8();
                    if(state==0){
                        servo.write(0);
                    }
                    else{
                        servo.write(90);  
                    }
                    break;
                }
                case COLOR:
                {
                    write_i16(get_color());
                    break;
                }
                
                // Unknown order
                /*default:
                write_order(ERROR);
                write_i16(404);
                return;
                */
            }
            //}
            
        }
        }
