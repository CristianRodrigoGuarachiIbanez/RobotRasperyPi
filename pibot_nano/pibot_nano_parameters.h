#ifndef pibot_nano_parameters_h
#define pibot_nano_parameters_h

//serial communication
    #define SERIAL_BAUD  115200  // Baudrate

//motordriver 
    // motordriver will be used in Phase/Enable Mode (Mode PIN is HIGH)
    #define R_dir 4   //right motor direction
    #define R_speed 5   //right motor speed
    #define L_dir 7    //motor direction 
    #define L_speed 6   //left motor speed
        
//encoders
    #define R_OUT1 2    //right first sensor starts interupt
    #define R_OUT2 8    //right second sensor
    #define L_OUT1 3    //left first sensor starts interrupt
    #define L_OUT2 9    //left second sensor 

// ultrasonic sensors
    #define US_F  16    // front sensor (equal to A2)
    #define US_L  15    // left sensor (equal to A1)
    #define US_R  17    // right sensor (equal to A3)

    // Normally you need to two pins to use the HC-SR04 ultrasonic sensor.
    // The trigger pin is used to start the measurement and save the start time
    // and the echo pin is used to stop the time after the end of the measurement.
    // Because these operations happen one after an other it is possible to do both 
    // tasks with the same pin.
    // Instead of ultrasonic sensors it is also possible to use sharp infrared sensors.
    // To start the measurment they just need to be connected to the a 5 V source with
    // their corresponding cables. The have one output pin which puts out an analog voltage 
    // between 0 and 5 V which is nonlinear related to distance. 
    // Both sharps and ultrasonic sensors have differend advantages and disadvantages. 
    // To make the robot compatible you could use the connetced pins of the HC-SR04 sensors 
    // to attach some sharp sensors. To get the distance values you need to get their out
    // put voltage using the analogRead(pin)-function and calulated that voltage to a distance 
    // using the corresponding function provided in the datasheet of your sharp sensor.
    
// bumpers - DEPRECATED
    // #define B_L 11      // left bumper
    // #define B_R 10      // right bumper
    // #define B_B 12      // back bumper
    // The bumpers of the pibot are build out of 3 end-stop-switches.
    // Every end-stop-switch has 3 pins: C Common; NO Normally Open;
    // NC Normally Closed
    // The Common Pin is connected to ground and the NO-pin is conneted to the
    // corresponding signal pin. If the bumper is pushed the signal level switches 
    // to ground. For any other case its undefined. To avoid that problem, the signal 
    // line of that bumper needs to have a stable 5 V level. To achive that we need
    // to initalise the pin with its Pull-Up-Resistor by using pinMode(pin,INPUT_PULLUP)

// servo
    #define SERVO 10

// status led
    #define STAT_LED 13
    // many common arduino boards have an onboard smd led connected to pin 13
    // That led could be use to show some information about the state of the 
    // programm running on the microcontroller.

// battery voltage measurement 
    #define BAT   A7
    // By using the analogRead()-function you will get a value between 
    // 0 and 1023. 
    // The analog pins of the arduino will be damaged if they are attached
    // to a voltage bigger than 5 V (in normal 5V operation).
    // The battery is a 9 V block. To avoid any damageds a voltage dividor is 
    // used to cut down the battery voltage to its half. Because of the fact that 
    // the maximal input voltage of a pin is 5 V and due to the voltage dividor 
    // you are able to connect a source with up to 10 V. 
    // Using the rule of three (for german readers: Dreisatz) you could easily 
    // calculate the battery voltage: 1023 -> 10 V; 0 -> 0 V; x -> (x/1023)*10 V

// buzzer 
    #define BUZZER 14 //driven by tone(PIN,Frequency,Duration)-Command 
    // equal to A0

// i2c connection to the IMU
    // A4 (equal to 18) is SDA (Serial Data)
    // A5 (equal to 19) is SCL (Serial Clock)

// linsesensor
    #define LS_0 A4 //left IR-Reflectance-Sensor
    #define LS_1 A5 //middle IR-Reflectance-Sensor
    #define LS_2 A6 //right IR-Reflectance-Sensor
    
// colorsensor
    #define CS 11

// If DEBUG is set to true, the arduino will send back all the received messages
    #define DEBUG false

#endif
