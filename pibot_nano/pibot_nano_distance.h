 #ifndef pibot_nano_distance_h
#define pibot_nano_distance_h
class distance_sensors
{
 public:
 distance_sensors();
 
 uint8_t get_left();
 uint8_t get_middle();
 uint8_t get_right();
 void update();
 private:
 uint8_t left;
 uint8_t middle;
 uint8_t right;
 uint8_t us_nr;
 long   last;

};
uint8_t get_distance(uint8_t sensor);
#endif
