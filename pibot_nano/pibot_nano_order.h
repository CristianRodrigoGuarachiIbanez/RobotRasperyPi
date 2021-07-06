#ifndef ORDER_H
#define ORDER_H

// Define the orders that can be sent and received
enum Order {
  START = 0,
  CONNECTED = 1,
  RECEIVED = 2,
  ERROR = 3,
  MOTORS = 4,
  VOLTAGE = 5,
  DISTANCES = 6,
  GET_ENCODERS = 7,
  RESET_ENCODERS  = 8,
  STATUS_LED = 9,
  BUZ = 10,
  GRIPPER = 11,
  GET_LINE_SENSORS = 12,
  COLOR = 13,
};

typedef enum Order Order;

#endif
