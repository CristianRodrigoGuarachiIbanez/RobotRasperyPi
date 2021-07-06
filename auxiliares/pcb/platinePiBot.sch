EESchema Schematic File Version 4
LIBS:platinePiBot-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R_Pack04_SIP RN1
U 1 1 5EF900A9
P 6800 3800
F 0 "RN1" V 6758 4005 50  0000 L CNN
F 1 "220" V 6849 4005 50  0000 L CNN
F 2 "Resistor_THT:R_Array_SIP8" V 7475 3800 50  0001 C CNN
F 3 "http://www.vishay.com/docs/31509/csc.pdf" H 6800 3800 50  0001 C CNN
	1    6800 3800
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x06_Male J1
U 1 1 5EF9ACD5
P 1600 2600
F 0 "J1" H 1706 2978 50  0000 C CNN
F 1 "mot_r" H 1706 2887 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 1600 2600 50  0001 C CNN
F 3 "~" H 1600 2600 50  0001 C CNN
	1    1600 2600
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x06_Male J3
U 1 1 5EF9AD66
P 1750 5500
F 0 "J3" H 1856 5878 50  0000 C CNN
F 1 "mot_l" H 1856 5787 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 1750 5500 50  0001 C CNN
F 3 "~" H 1750 5500 50  0001 C CNN
	1    1750 5500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Female J2
U 1 1 5EF9AE33
P 1800 4000
F 0 "J2" H 1694 3575 50  0000 C CNN
F 1 "us_front" H 1694 3666 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 1800 4000 50  0001 C CNN
F 3 "~" H 1800 4000 50  0001 C CNN
	1    1800 4000
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x04_Male J6
U 1 1 5EF9B092
P 2600 5700
F 0 "J6" H 2706 5978 50  0000 C CNN
F 1 "us_left" H 2706 5887 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 2600 5700 50  0001 C CNN
F 3 "~" H 2600 5700 50  0001 C CNN
	1    2600 5700
	1    0    0    1   
$EndComp
$Comp
L Connector:Conn_01x04_Male J4
U 1 1 5EF9B139
P 2550 2600
F 0 "J4" H 2656 2878 50  0000 C CNN
F 1 "us_right" H 2656 2787 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 2550 2600 50  0001 C CNN
F 3 "~" H 2550 2600 50  0001 C CNN
	1    2550 2600
	1    0    0    1   
$EndComp
$Comp
L Connector:Conn_01x07_Female J5
U 1 1 5EF9B20A
P 2600 3900
F 0 "J5" H 2494 3375 50  0000 C CNN
F 1 "motor_driver" H 2494 3466 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical" H 2600 3900 50  0001 C CNN
F 3 "~" H 2600 3900 50  0001 C CNN
	1    2600 3900
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x07_Female J9
U 1 1 5EF9B2D3
P 2950 3900
F 0 "J9" H 2977 3926 50  0000 L CNN
F 1 "Mot_driver_rear" H 2977 3835 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical" H 2950 3900 50  0001 C CNN
F 3 "~" H 2950 3900 50  0001 C CNN
	1    2950 3900
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x02_Male J7
U 1 1 5EF9B3AE
P 2900 2750
F 0 "J7" H 3006 2928 50  0000 C CNN
F 1 "led_front_right" H 3006 2837 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2900 2750 50  0001 C CNN
F 3 "~" H 2900 2750 50  0001 C CNN
	1    2900 2750
	1    0    0    1   
$EndComp
$Comp
L Connector:Conn_01x02_Male J8
U 1 1 5EF9B414
P 3000 5750
F 0 "J8" H 3106 5928 50  0000 C CNN
F 1 "led_front_left" H 3106 5837 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 3000 5750 50  0001 C CNN
F 3 "~" H 3000 5750 50  0001 C CNN
	1    3000 5750
	1    0    0    1   
$EndComp
$Comp
L Device:CP_Small C1
U 1 1 5EF9B676
P 3100 1650
F 0 "C1" H 3012 1604 50  0000 R CNN
F 1 "10µF" H 3012 1695 50  0000 R CNN
F 2 "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm" H 3100 1650 50  0001 C CNN
F 3 "~" H 3100 1650 50  0001 C CNN
	1    3100 1650
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x15_Female J10
U 1 1 5EF9B764
P 3900 3950
F 0 "J10" H 3794 3025 50  0000 C CNN
F 1 "arduino_nano" H 3794 3116 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x15_P2.54mm_Vertical" H 3900 3950 50  0001 C CNN
F 3 "~" H 3900 3950 50  0001 C CNN
	1    3900 3950
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x15_Female J12
U 1 1 5EF9B80A
P 4600 3950
F 0 "J12" H 4627 3976 50  0000 L CNN
F 1 "Nano_rear" H 4627 3885 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x15_P2.54mm_Vertical" H 4600 3950 50  0001 C CNN
F 3 "~" H 4600 3950 50  0001 C CNN
	1    4600 3950
	1    0    0    1   
$EndComp
$Comp
L Device:R R7
U 1 1 5EF9E552
P 5250 5100
F 0 "R7" H 5320 5146 50  0000 L CNN
F 1 "100" H 5320 5055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical" V 5180 5100 50  0001 C CNN
F 3 "~" H 5250 5100 50  0001 C CNN
	1    5250 5100
	1    0    0    -1  
$EndComp
$Comp
L Device:Buzzer BZ1
U 1 1 5EF9E63C
P 4850 5100
F 0 "BZ1" H 5003 5129 50  0000 L CNN
F 1 "buzzer" H 5003 5038 50  0000 L CNN
F 2 "Buzzer_Beeper:Buzzer_12x9.5RM7.6" V 4825 5200 50  0001 C CNN
F 3 "~" V 4825 5200 50  0001 C CNN
	1    4850 5100
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x20_Odd_Even J15
U 1 1 5EF9EA74
P 5650 1100
F 0 "J15" V 5746 2079 50  0000 L CNN
F 1 "raspberry_pi" V 5655 2079 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 5650 1100 50  0001 C CNN
F 3 "~" H 5650 1100 50  0001 C CNN
	1    5650 1100
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x04_Female J14
U 1 1 5EFA1113
P 5400 3800
F 0 "J14" H 5427 3776 50  0000 L CNN
F 1 "LCD" H 5427 3685 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 5400 3800 50  0001 C CNN
F 3 "~" H 5400 3800 50  0001 C CNN
	1    5400 3800
	1    0    0    1   
$EndComp
Wire Wire Line
	4750 1300 4750 1650
Wire Wire Line
	4750 3800 5200 3800
Wire Wire Line
	4750 800  4450 800 
Wire Wire Line
	2250 2700 1800 2700
Wire Wire Line
	2250 2700 2250 3050
Wire Wire Line
	2250 3800 2000 3800
Wire Wire Line
	2750 800  2750 1750
Wire Wire Line
	2750 800  2250 800 
Wire Wire Line
	2250 800  2250 2700
Connection ~ 2750 800 
Connection ~ 2250 2700
Wire Wire Line
	4850 800  4750 800 
Connection ~ 4750 800 
Wire Wire Line
	1950 5600 2250 5600
Wire Wire Line
	2250 5600 2250 5100
Connection ~ 2250 3800
Wire Wire Line
	2800 5500 2800 4700
Wire Wire Line
	2800 4700 2250 4700
Connection ~ 2250 4700
Wire Wire Line
	2250 4700 2250 3800
Wire Wire Line
	2800 4700 3300 4700
Wire Wire Line
	3300 4700 3300 4100
Wire Wire Line
	3300 4100 3150 4100
Connection ~ 2800 4700
Wire Wire Line
	3300 4100 3300 3600
Wire Wire Line
	3300 3600 3150 3600
Connection ~ 3300 4100
Wire Wire Line
	4400 3550 4300 3550
Wire Wire Line
	4300 3550 4300 3050
Wire Wire Line
	4300 3050 2250 3050
Connection ~ 2250 3050
Wire Wire Line
	2250 3050 2250 3800
Wire Wire Line
	3100 1750 2750 1750
Connection ~ 2750 1750
Wire Wire Line
	2750 1750 2750 2400
Wire Wire Line
	4950 800  4950 700 
Wire Wire Line
	4950 700  3100 700 
Wire Wire Line
	3100 700  3100 1500
Wire Wire Line
	4850 1300 4850 3600
Wire Wire Line
	4850 3600 5200 3600
Wire Wire Line
	4950 1300 4950 3700
Wire Wire Line
	4950 3700 5200 3700
Wire Wire Line
	5050 1300 5050 1600
Wire Wire Line
	5050 1600 3650 1600
Wire Wire Line
	3650 2950 4250 2950
Wire Wire Line
	4250 2950 4250 3450
Wire Wire Line
	4250 3450 4400 3450
Wire Wire Line
	4250 3450 4100 3450
Connection ~ 4250 3450
Wire Wire Line
	5150 1300 5150 1500
Wire Wire Line
	5150 1500 5100 1500
Connection ~ 3100 1500
Wire Wire Line
	3100 1500 3100 1550
Wire Wire Line
	5550 1300 5550 1650
Wire Wire Line
	5550 1650 4750 1650
Connection ~ 4750 1650
Wire Wire Line
	4750 1650 4750 3800
Wire Wire Line
	5950 1300 5950 1500
Wire Wire Line
	5950 1500 5150 1500
Connection ~ 5150 1500
$Comp
L Device:R_Pack04_SIP RN2
U 1 1 5EFAD301
P 7450 3800
F 0 "RN2" V 8175 3782 50  0000 C CNN
F 1 "330" V 8084 3782 50  0000 C CNN
F 2 "Resistor_THT:R_Array_SIP8" V 8125 3800 50  0001 C CNN
F 3 "http://www.vishay.com/docs/31509/csc.pdf" H 7450 3800 50  0001 C CNN
	1    7450 3800
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R9
U 1 1 5EFAD43B
P 6750 2650
F 0 "R9" H 6820 2696 50  0000 L CNN
F 1 "680" H 6820 2605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical" V 6680 2650 50  0001 C CNN
F 3 "~" H 6750 2650 50  0001 C CNN
	1    6750 2650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R10
U 1 1 5EFAD49F
P 7300 2650
F 0 "R10" H 7370 2696 50  0000 L CNN
F 1 "680" H 7370 2605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical" V 7230 2650 50  0001 C CNN
F 3 "~" H 7300 2650 50  0001 C CNN
	1    7300 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	6050 1300 6050 4200
Wire Wire Line
	6050 4200 6600 4200
$Comp
L Device:LED_Dual_ACA D4
U 1 1 5EFAFD43
P 9250 3400
F 0 "D4" H 9250 3825 50  0000 C CNN
F 1 "led_right" H 9250 3734 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm-3" H 9250 3400 50  0001 C CNN
F 3 "~" H 9250 3400 50  0001 C CNN
	1    9250 3400
	1    0    0    -1  
$EndComp
$Comp
L Device:LED_Dual_ACA D5
U 1 1 5EFAFE15
P 9250 4050
F 0 "D5" H 9250 4475 50  0000 C CNN
F 1 "led_mid" H 9250 4384 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm-3" H 9250 4050 50  0001 C CNN
F 3 "~" H 9250 4050 50  0001 C CNN
	1    9250 4050
	1    0    0    -1  
$EndComp
$Comp
L Device:LED_Dual_ACA D6
U 1 1 5EFAFE85
P 9250 4650
F 0 "D6" H 9250 5075 50  0000 C CNN
F 1 "led_left" H 9250 4984 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm-3" H 9250 4650 50  0001 C CNN
F 3 "~" H 9250 4650 50  0001 C CNN
	1    9250 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 4300 6550 4300
Wire Wire Line
	6550 4300 6550 5000
Wire Wire Line
	6550 5000 9850 5000
Wire Wire Line
	9850 5000 9850 4550
Wire Wire Line
	9850 4550 9550 4550
Wire Wire Line
	8950 4650 8350 4650
Wire Wire Line
	8350 1500 6950 1500
Wire Wire Line
	8350 1500 8350 3400
Connection ~ 5950 1500
Wire Wire Line
	8950 4050 8350 4050
Connection ~ 8350 4050
Wire Wire Line
	8350 4050 8350 4650
Wire Wire Line
	8950 3400 8350 3400
Connection ~ 8350 3400
Wire Wire Line
	8350 3400 8350 4050
Wire Wire Line
	9550 4750 9700 4750
Wire Wire Line
	9700 4750 9700 4900
Wire Wire Line
	7900 4900 7900 4000
Wire Wire Line
	7900 4000 7650 4000
Wire Wire Line
	7650 3900 7850 3900
Wire Wire Line
	7850 3900 7850 1900
Wire Wire Line
	7850 1900 6450 1900
Wire Wire Line
	6450 1900 6450 1300
Wire Wire Line
	6150 1300 6150 1750
Wire Wire Line
	6150 1750 7950 1750
Wire Wire Line
	7950 1750 7950 3600
Wire Wire Line
	7950 3600 7650 3600
Wire Wire Line
	9700 4900 7900 4900
Wire Wire Line
	9550 4150 9650 4150
Wire Wire Line
	9650 4150 9650 4400
Wire Wire Line
	9650 4400 7950 4400
Wire Wire Line
	7950 4400 7950 3700
Wire Wire Line
	7950 3700 7650 3700
Wire Wire Line
	6600 4000 6400 4000
Wire Wire Line
	6400 4000 6400 5050
Wire Wire Line
	6400 5050 10050 5050
Wire Wire Line
	10050 5050 10050 3950
Wire Wire Line
	10050 3950 9550 3950
Wire Wire Line
	6250 1300 6250 3900
Wire Wire Line
	6250 3900 6600 3900
Wire Wire Line
	6350 1300 6350 3700
Wire Wire Line
	6350 3700 6600 3700
Wire Wire Line
	9550 3300 9650 3300
Wire Wire Line
	9650 3300 9650 3000
Wire Wire Line
	9650 3000 6450 3000
Wire Wire Line
	6450 3000 6450 3600
Wire Wire Line
	6450 3600 6600 3600
Wire Wire Line
	7650 3400 8100 3400
Wire Wire Line
	8100 3400 8100 3700
Wire Wire Line
	8100 3700 9550 3700
Wire Wire Line
	9550 3700 9550 3500
Wire Wire Line
	7650 3300 7750 3300
Wire Wire Line
	7750 3300 7750 650 
Wire Wire Line
	7750 650  6450 650 
Wire Wire Line
	6450 650  6450 800 
Wire Wire Line
	6650 1300 6650 1500
Connection ~ 6650 1500
Wire Wire Line
	6650 1500 6600 1500
Wire Wire Line
	6550 1300 6550 3300
Wire Wire Line
	6550 3300 6600 3300
Wire Wire Line
	6600 3400 5200 3400
Wire Wire Line
	5200 3400 5200 2650
Wire Wire Line
	5200 2650 3100 2650
Wire Wire Line
	3100 2750 3400 2750
Wire Wire Line
	3400 2750 3400 2550
Connection ~ 3400 1500
Wire Wire Line
	3400 1500 3100 1500
Wire Wire Line
	5050 800  5050 600 
Wire Wire Line
	5050 600  4000 600 
Wire Wire Line
	4200 3350 4100 3350
Connection ~ 3400 2250
Wire Wire Line
	3400 2250 3400 1500
Wire Wire Line
	4000 600  4000 1750
Wire Wire Line
	5150 800  5150 550 
Wire Wire Line
	5150 550  3750 550 
Wire Wire Line
	3750 550  3750 2050
Connection ~ 3400 2750
Wire Wire Line
	5450 2150 4100 2150
Wire Wire Line
	4100 2150 4100 3250
Wire Wire Line
	5650 800  5650 700 
Wire Wire Line
	5650 700  4950 700 
Connection ~ 4950 700 
Wire Wire Line
	5750 800  5750 600 
Wire Wire Line
	5750 600  7700 600 
Wire Wire Line
	7700 600  7700 4200
Wire Wire Line
	7700 4200 7650 4200
Wire Wire Line
	7650 4300 7650 5650
Wire Wire Line
	7650 5650 3200 5650
Wire Wire Line
	3200 5750 3400 5750
Wire Wire Line
	3400 5750 3400 5350
Wire Wire Line
	10200 4650 9750 4650
Wire Wire Line
	9750 4650 9750 550 
Wire Wire Line
	9750 550  6050 550 
Wire Wire Line
	6050 550  6050 800 
Wire Wire Line
	10600 4650 10850 4650
Wire Wire Line
	10850 1500 9550 1500
Connection ~ 8350 1500
Wire Wire Line
	6150 800  6150 700 
Wire Wire Line
	6150 700  5650 700 
Connection ~ 5650 700 
Wire Wire Line
	6250 800  6250 700 
Wire Wire Line
	6250 700  9850 700 
Wire Wire Line
	9850 700  9850 4050
Wire Wire Line
	9850 4050 10200 4050
Wire Wire Line
	10600 4050 10850 4050
Connection ~ 10850 4050
Wire Wire Line
	6350 800  6350 650 
Wire Wire Line
	6350 650  6150 650 
Wire Wire Line
	6150 650  6150 700 
Connection ~ 6150 700 
Wire Wire Line
	6550 800  6550 750 
Wire Wire Line
	6550 750  10200 750 
Wire Wire Line
	10200 750  10200 3300
Wire Wire Line
	10600 3300 10850 3300
Connection ~ 10850 3300
Wire Wire Line
	10850 3300 10850 2250
Wire Wire Line
	4100 4350 2350 4350
Wire Wire Line
	2350 4350 2350 5400
Wire Wire Line
	2350 5400 1950 5400
Wire Wire Line
	2200 5300 2200 6000
Wire Wire Line
	2200 6000 3400 6000
Wire Wire Line
	3400 6000 3400 5800
Connection ~ 3400 5750
Wire Wire Line
	2000 4100 2400 4100
Wire Wire Line
	2400 4100 2400 3250
Wire Wire Line
	2400 3250 3400 3250
Connection ~ 3400 3250
Wire Wire Line
	3400 3250 3400 3000
Wire Wire Line
	1800 2400 2400 2400
Connection ~ 3400 2900
Wire Wire Line
	4100 4250 2500 4250
Wire Wire Line
	2500 4250 2500 2500
Wire Wire Line
	2500 2500 1800 2500
Wire Wire Line
	4100 4150 3600 4150
Wire Wire Line
	3600 4150 3600 3900
Wire Wire Line
	3600 3900 3150 3900
Wire Wire Line
	4100 4050 3500 4050
Wire Wire Line
	3500 4050 3500 4000
Wire Wire Line
	3500 4000 3150 4000
Wire Wire Line
	4100 3950 3650 3950
Wire Wire Line
	3650 3950 3650 3800
Wire Wire Line
	3650 3800 3150 3800
Wire Wire Line
	4100 3850 3700 3850
Wire Wire Line
	3700 3850 3700 3700
Wire Wire Line
	3700 3700 3150 3700
Wire Wire Line
	4100 3750 4200 3750
Wire Wire Line
	4200 3750 4200 4850
Wire Wire Line
	4200 4850 2450 4850
Wire Wire Line
	2450 4850 2450 5500
Wire Wire Line
	2450 5500 1950 5500
Wire Wire Line
	4100 3650 3500 3650
Wire Wire Line
	3500 3650 3500 3100
Wire Wire Line
	3500 3100 2350 3100
Wire Wire Line
	2350 3100 2350 2600
Wire Wire Line
	2350 2600 1800 2600
Wire Wire Line
	4100 3550 3400 3550
Connection ~ 3400 3550
Wire Wire Line
	3400 3550 3400 3250
$Comp
L Connector:Conn_01x02_Male J11
U 1 1 5F05E470
P 4150 5050
F 0 "J11" H 4256 5228 50  0000 C CNN
F 1 "buzzer_jumper" H 4256 5137 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 4150 5050 50  0001 C CNN
F 3 "~" H 4150 5050 50  0001 C CNN
	1    4150 5050
	1    0    0    -1  
$EndComp
Wire Wire Line
	4400 4350 4350 4350
Wire Wire Line
	4350 4350 4350 5050
Wire Wire Line
	4350 5150 4600 5150
Wire Wire Line
	4600 5150 4750 5000
Wire Wire Line
	4600 4900 5250 4900
Wire Wire Line
	5250 4900 5250 4950
Wire Wire Line
	5250 5250 5250 5350
Wire Wire Line
	5250 5350 3400 5350
Connection ~ 3400 5350
Wire Wire Line
	3400 5350 3400 4750
Wire Wire Line
	4400 4250 4300 4250
Wire Wire Line
	4300 4250 4300 5700
Wire Wire Line
	4300 5700 2800 5700
Wire Wire Line
	2800 5800 3400 5800
Connection ~ 3400 5800
Wire Wire Line
	3400 5800 3400 5750
Wire Wire Line
	4400 4150 4250 4150
Wire Wire Line
	4250 4150 4250 4300
Wire Wire Line
	4250 4300 2100 4300
Wire Wire Line
	2100 4300 2100 3900
Wire Wire Line
	2100 3900 2000 3900
Wire Wire Line
	2000 3900 2000 4000
Connection ~ 2000 3900
Wire Wire Line
	2800 5600 2800 5700
Connection ~ 2800 5700
Wire Wire Line
	2750 2500 2750 2600
Wire Wire Line
	2750 2600 2850 2600
Wire Wire Line
	2850 2600 2850 3400
Wire Wire Line
	2850 3400 3750 3400
Wire Wire Line
	3750 3400 3750 4000
Wire Wire Line
	3750 4000 4300 4000
Wire Wire Line
	4300 4000 4300 4050
Wire Wire Line
	4300 4050 4400 4050
Connection ~ 2750 2600
Wire Wire Line
	2750 2700 2750 3000
Wire Wire Line
	2750 3000 3400 3000
Connection ~ 3400 3000
Wire Wire Line
	3400 3000 3400 2900
Wire Wire Line
	4400 3650 4800 3650
Wire Wire Line
	4800 3650 4800 2450
Wire Wire Line
	4800 2450 5450 2450
Wire Wire Line
	5150 2350 5150 4750
Wire Wire Line
	5150 4750 4700 4750
Connection ~ 3400 4750
Wire Wire Line
	3400 4750 3400 4500
Wire Wire Line
	5450 2900 5850 2900
Wire Wire Line
	5850 2900 5850 2150
Wire Wire Line
	5850 2150 10600 2150
Wire Wire Line
	10950 2250 10850 2250
Connection ~ 10850 2250
Wire Wire Line
	10850 2250 10850 1500
Wire Wire Line
	4400 3350 4700 3350
Wire Wire Line
	4700 3350 4700 4750
Connection ~ 4700 4750
Wire Wire Line
	4700 4750 3400 4750
Wire Wire Line
	3150 4200 3150 4500
Wire Wire Line
	3150 4500 3400 4500
Connection ~ 3400 4500
Wire Wire Line
	3400 4500 3400 3550
Wire Wire Line
	2800 4200 3150 4200
$Comp
L Device:D_Schottky D3
U 1 1 5F26EA3F
P 8500 2500
F 0 "D3" V 8546 2421 50  0000 R CNN
F 1 "STPS2H100" V 8455 2421 50  0000 R CNN
F 2 "Diode_THT:D_A-405_P7.62mm_Horizontal" H 8500 2500 50  0001 C CNN
F 3 "~" H 8500 2500 50  0001 C CNN
	1    8500 2500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2800 4100 2950 4100
Wire Wire Line
	2950 4100 2950 3150
Wire Wire Line
	2950 3150 8150 3150
Wire Wire Line
	8150 3150 8150 2350
Wire Wire Line
	8150 2350 8500 2350
$Comp
L Switch:SW_SPDT_MSM SW1
U 1 1 5F2837E7
P 9300 1150
F 0 "SW1" V 9254 1298 50  0000 L CNN
F 1 "sw_not_mot" V 9345 1298 50  0000 L CNN
F 2 "Button_Switch_THT:switch_tht_3pos" H 9300 1150 50  0001 C CNN
F 3 "" H 9300 1150 50  0001 C CNN
	1    9300 1150
	0    1    1    0   
$EndComp
Wire Wire Line
	8500 2350 8500 2100
Wire Wire Line
	9400 2100 9400 1350
Connection ~ 8500 2350
Wire Wire Line
	9300 950  10600 950 
Wire Wire Line
	10600 950  10600 2150
Connection ~ 10600 2150
Wire Wire Line
	10600 2150 10950 2150
$Comp
L Device:LED D2
U 1 1 5F2ACE91
P 7300 2250
F 0 "D2" V 7338 2133 50  0000 R CNN
F 1 "LED_power_rear" V 7247 2133 50  0000 R CNN
F 2 "LED_THT:LED_D3.0mm" H 7300 2250 50  0001 C CNN
F 3 "~" H 7300 2250 50  0001 C CNN
	1    7300 2250
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D1
U 1 1 5F2ACFAB
P 6750 2200
F 0 "D1" V 6788 2083 50  0000 R CNN
F 1 "LED_Power_front" V 6697 2083 50  0000 R CNN
F 2 "LED_THT:LED_D3.0mm" H 6750 2200 50  0001 C CNN
F 3 "~" H 6750 2200 50  0001 C CNN
	1    6750 2200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8500 2100 7300 2100
Connection ~ 8500 2100
Wire Wire Line
	8500 2100 9400 2100
$Comp
L Regulator_Linear:KA78M05_TO252 U1
U 1 1 5F2EC536
P 10250 1400
F 0 "U1" H 10250 1642 50  0000 C CNN
F 1 "DCDC_converter" H 10250 1551 50  0000 C CNN
F 2 "Converter_DCDC:Converter_DCDC_RECOM_R-78E-0.5_THT" H 10250 1625 50  0001 C CIN
F 3 "http://www.fairchildsemi.com/ds/LM/LM78M05.pdf" H 10250 1350 50  0001 C CNN
	1    10250 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	9200 1400 9950 1400
Wire Wire Line
	9200 1350 9200 1400
Wire Wire Line
	9200 2650 8500 2650
$Comp
L Device:CP_Small C2
U 1 1 5F32CC6B
P 6950 1750
F 0 "C2" H 6862 1704 50  0000 R CNN
F 1 "10µF" H 6862 1795 50  0000 R CNN
F 2 "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm" H 6950 1750 50  0001 C CNN
F 3 "~" H 6950 1750 50  0001 C CNN
	1    6950 1750
	-1   0    0    1   
$EndComp
Wire Wire Line
	8500 2650 7500 2650
Wire Wire Line
	6950 2650 6950 1850
Connection ~ 8500 2650
Wire Wire Line
	6950 1650 6950 1500
Connection ~ 6950 1500
Wire Wire Line
	6950 1500 6650 1500
Wire Wire Line
	6750 2050 7500 2050
Wire Wire Line
	7500 2050 7500 2650
Connection ~ 7500 2650
Wire Wire Line
	7500 2650 6950 2650
Wire Wire Line
	7300 2400 7300 2500
Wire Wire Line
	6750 2350 6750 2500
Wire Wire Line
	7300 2800 6750 2800
Wire Wire Line
	6750 2800 6600 2800
Wire Wire Line
	6600 2800 6600 1500
Connection ~ 6750 2800
Connection ~ 6600 1500
Wire Wire Line
	6600 1500 5950 1500
Wire Wire Line
	10250 1700 9550 1700
Wire Wire Line
	9550 1700 9550 1500
Connection ~ 9550 1500
Wire Wire Line
	9550 1500 8400 1500
$Comp
L Device:D_Schottky D7
U 1 1 5F4C2E30
P 10250 5900
F 0 "D7" H 10250 6116 50  0000 C CNN
F 1 "1N5818" H 10250 6025 50  0000 C CNN
F 2 "Diode_THT:D_A-405_P7.62mm_Horizontal" H 10250 5900 50  0001 C CNN
F 3 "~" H 10250 5900 50  0001 C CNN
	1    10250 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	10550 1400 10550 3000
Wire Wire Line
	10550 3000 11000 3000
Wire Wire Line
	11000 3000 11000 5900
Wire Wire Line
	11000 5900 10400 5900
$Comp
L Connector:Conn_01x02_Male J13
U 1 1 5F4DB183
P 5250 6400
F 0 "J13" H 5356 6578 50  0000 C CNN
F 1 "power_for_pi" H 5356 6487 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 5250 6400 50  0001 C CNN
F 3 "~" H 5250 6400 50  0001 C CNN
	1    5250 6400
	1    0    0    1   
$EndComp
Wire Wire Line
	10100 5900 9400 5900
Wire Wire Line
	5450 5900 5450 6300
Wire Wire Line
	5450 6400 5650 6400
Wire Wire Line
	10850 6400 10850 5700
$Comp
L Switch:SW_SPDT_MSM SW2
U 1 1 5F556CA2
P 9400 5500
F 0 "SW2" V 9446 5312 50  0000 R CNN
F 1 "sw_netz_akku" V 9355 5312 50  0000 R CNN
F 2 "Button_Switch_THT:switch_tht_3pos" H 9400 5500 50  0001 C CNN
F 3 "" H 9400 5500 50  0001 C CNN
	1    9400 5500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9400 5700 9400 5900
Connection ~ 9400 5900
Wire Wire Line
	9400 5900 5450 5900
Wire Wire Line
	9300 5300 9300 5200
Wire Wire Line
	9300 5200 10600 5200
Wire Wire Line
	10600 5200 10600 5400
Wire Wire Line
	10600 5700 10850 5700
$Comp
L Connector:Conn_01x05_Female J16
U 1 1 5F65267D
P 8450 5650
F 0 "J16" V 8297 5898 50  0000 L CNN
F 1 "power_breakout" V 8388 5898 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x05_P2.54mm_Vertical" H 8450 5650 50  0001 C CNN
F 3 "~" H 8450 5650 50  0001 C CNN
	1    8450 5650
	0    1    1    0   
$EndComp
Wire Wire Line
	8650 5450 8900 5450
Wire Wire Line
	8900 5450 8900 6400
Connection ~ 8900 6400
Wire Wire Line
	8900 6400 10850 6400
Wire Wire Line
	5200 3900 5100 3900
Wire Wire Line
	5100 3900 5100 1500
Connection ~ 5100 1500
Wire Wire Line
	5100 1500 4400 1500
Wire Wire Line
	1800 2900 2150 2900
Wire Wire Line
	2150 2900 2150 3700
Wire Wire Line
	2150 3700 2800 3700
Wire Wire Line
	1800 2800 2450 2800
Wire Wire Line
	2450 2800 2450 3800
Wire Wire Line
	2450 3800 2800 3800
Wire Wire Line
	1950 5700 2550 5700
Wire Wire Line
	2550 5700 2550 4000
Wire Wire Line
	2550 4000 2800 4000
Wire Wire Line
	2150 5800 2150 4200
Wire Wire Line
	2150 4200 2300 4200
Wire Wire Line
	2300 4200 2300 3900
Wire Wire Line
	2300 3900 2800 3900
NoConn ~ 4400 4450
$Comp
L Connector:Conn_01x03_Male J18
U 1 1 5F12A6EE
P 3700 6600
F 0 "J18" H 3806 6878 50  0000 C CNN
F 1 "gripper" H 3806 6787 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 3700 6600 50  0001 C CNN
F 3 "~" H 3700 6600 50  0001 C CNN
	1    3700 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 5100 4050 5100
Wire Wire Line
	4600 4900 4750 5200
Connection ~ 2250 5100
Wire Wire Line
	2250 5100 2250 4700
Wire Wire Line
	3900 6500 5650 6500
Wire Wire Line
	5650 6500 5650 6400
Connection ~ 5650 6400
Wire Wire Line
	5650 6400 8900 6400
Wire Wire Line
	4100 4450 4150 4450
Wire Wire Line
	4150 4450 4150 6600
Wire Wire Line
	4150 6600 3900 6600
$Comp
L Connector:Conn_01x05_Male J17
U 1 1 5F18BEFF
P 3200 1100
F 0 "J17" H 3306 1478 50  0000 C CNN
F 1 "colorsensor" H 3306 1387 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 3200 1100 50  0001 C CNN
F 3 "~" H 3200 1100 50  0001 C CNN
	1    3200 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 1000 3500 800 
Connection ~ 3500 800 
Wire Wire Line
	3500 800  2750 800 
Connection ~ 3650 1500
Wire Wire Line
	3650 1500 3400 1500
Wire Wire Line
	5250 1300 5250 1400
Wire Wire Line
	5250 1400 3800 1400
Wire Wire Line
	3800 1400 3800 1100
Wire Wire Line
	3800 1100 3400 1100
Wire Wire Line
	5350 1300 5350 1450
Wire Wire Line
	5350 1450 3700 1450
Wire Wire Line
	3700 1450 3700 1200
Wire Wire Line
	3700 1200 3400 1200
Wire Wire Line
	4100 4550 3550 4550
$Comp
L Connector:Conn_01x05_Male J19
U 1 1 5F2355DC
P 4100 1100
F 0 "J19" H 4206 1478 50  0000 C CNN
F 1 "linesensor" H 4206 1387 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 4100 1100 50  0001 C CNN
F 3 "~" H 4100 1100 50  0001 C CNN
	1    4100 1100
	1    0    0    1   
$EndComp
Wire Wire Line
	4450 1200 4450 800 
Connection ~ 4450 800 
Wire Wire Line
	4450 800  3500 800 
Connection ~ 4400 1500
Wire Wire Line
	4400 1500 3650 1500
Wire Wire Line
	4400 3850 4650 3850
Wire Wire Line
	4650 1000 4300 1000
Wire Wire Line
	4400 3950 4350 3950
Wire Wire Line
	4400 3750 4550 3750
Wire Wire Line
	10850 3300 10850 4050
Wire Wire Line
	10850 4050 10850 4650
$Comp
L Switch:SW_Push SW3
U 1 1 5F36C1AE
P 10400 4050
F 0 "SW3" V 10354 4198 50  0000 L CNN
F 1 "button_mid" V 10445 4198 50  0000 L CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 10400 4250 50  0001 C CNN
F 3 "" H 10400 4250 50  0001 C CNN
	1    10400 4050
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW4
U 1 1 5F36C232
P 10400 4650
F 0 "SW4" H 10400 4935 50  0000 C CNN
F 1 "button_left" H 10400 4844 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 10400 4850 50  0001 C CNN
F 3 "" H 10400 4850 50  0001 C CNN
	1    10400 4650
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW5
U 1 1 5F36C312
P 10400 3300
F 0 "SW5" H 10400 3585 50  0000 C CNN
F 1 "button_right" H 10400 3494 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 10400 3500 50  0001 C CNN
F 3 "" H 10400 3500 50  0001 C CNN
	1    10400 3300
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H1
U 1 1 5F39893D
P 2100 1500
F 0 "H1" H 2200 1546 50  0000 L CNN
F 1 "MountingHole_front_right" H 2200 1455 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 2100 1500 50  0001 C CNN
F 3 "~" H 2100 1500 50  0001 C CNN
	1    2100 1500
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 5F398C07
P 2200 6500
F 0 "H2" H 2300 6546 50  0000 L CNN
F 1 "MountingHole_front_left" H 2300 6455 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 2200 6500 50  0001 C CNN
F 3 "~" H 2200 6500 50  0001 C CNN
	1    2200 6500
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H5
U 1 1 5F398EAD
P 9550 6500
F 0 "H5" H 9650 6546 50  0000 L CNN
F 1 "MountingHole_front_left" H 9650 6455 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 9550 6500 50  0001 C CNN
F 3 "~" H 9550 6500 50  0001 C CNN
	1    9550 6500
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H6
U 1 1 5F3998A0
P 10950 1200
F 0 "H6" H 11050 1246 50  0000 L CNN
F 1 "CableHole_back_right" H 11050 1155 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 10950 1200 50  0001 C CNN
F 3 "~" H 10950 1200 50  0001 C CNN
	1    10950 1200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H7
U 1 1 5F399D63
P 10950 1450
F 0 "H7" H 11050 1496 50  0000 L CNN
F 1 "CableHole_back_right" H 11050 1405 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 10950 1450 50  0001 C CNN
F 3 "~" H 10950 1450 50  0001 C CNN
	1    10950 1450
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H8
U 1 1 5F399DE1
P 11100 4600
F 0 "H8" H 11200 4646 50  0000 L CNN
F 1 "CableHole_back_left" H 11200 4555 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 11100 4600 50  0001 C CNN
F 3 "~" H 11100 4600 50  0001 C CNN
	1    11100 4600
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H9
U 1 1 5F39A0B2
P 11100 4800
F 0 "H9" H 11200 4846 50  0000 L CNN
F 1 "CableHole_back_left" H 11200 4755 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 11100 4800 50  0001 C CNN
F 3 "~" H 11100 4800 50  0001 C CNN
	1    11100 4800
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 5F39A13C
P 8150 6700
F 0 "H4" H 8250 6746 50  0000 L CNN
F 1 "CableHole_side_rear" H 8250 6655 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 8150 6700 50  0001 C CNN
F 3 "~" H 8150 6700 50  0001 C CNN
	1    8150 6700
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 5F39A49E
P 7900 6700
F 0 "H3" H 8000 6746 50  0000 L CNN
F 1 "CableHole_side_front" H 8000 6655 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.5mm" H 7900 6700 50  0001 C CNN
F 3 "~" H 7900 6700 50  0001 C CNN
	1    7900 6700
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 2900 3400 2900
Wire Wire Line
	2400 2400 2400 2900
Wire Wire Line
	2150 5800 1950 5800
Wire Wire Line
	2200 5300 1950 5300
Connection ~ 3150 4200
Wire Wire Line
	5450 1750 4000 1750
Connection ~ 4000 1750
Wire Wire Line
	4200 1850 5450 1850
Wire Wire Line
	5450 2050 3750 2050
Wire Wire Line
	3750 2050 3750 2450
Connection ~ 3750 2050
Wire Wire Line
	4200 1850 4200 3350
Wire Wire Line
	4650 1000 4650 3850
$Comp
L Device:R_Pack04_SIP RN4
U 1 1 5F72F7A8
P 5650 2250
F 0 "RN4" V 5700 2455 50  0000 L CNN
F 1 "5,6k" V 5609 2455 50  0000 L CNN
F 2 "Resistor_THT:R_Array_SIP8" V 6325 2250 50  0001 C CNN
F 3 "http://www.vishay.com/docs/31509/csc.pdf" H 5650 2250 50  0001 C CNN
	1    5650 2250
	0    1    -1   0   
$EndComp
Wire Wire Line
	5450 2450 5450 2650
Connection ~ 5450 2450
Wire Wire Line
	5150 2350 5450 2350
Wire Wire Line
	5450 2900 5450 2750
$Comp
L Device:R_Pack03_SIP RN3
U 1 1 5F9DB9CB
P 3050 2250
F 0 "RN3" V 3675 2232 50  0000 C CNN
F 1 "10k" V 3584 2232 50  0000 C CNN
F 2 "Resistor_THT:R_Array_SIP6" V 3625 2250 50  0001 C CNN
F 3 "http://www.vishay.com/docs/31509/csc.pdf" H 3050 2250 50  0001 C CNN
	1    3050 2250
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3750 2450 3250 2450
Wire Wire Line
	3250 2550 3400 2550
Wire Wire Line
	3400 2550 3400 2250
Connection ~ 3400 2550
Wire Wire Line
	3400 2750 3400 2900
Wire Wire Line
	3400 2250 3250 2250
Wire Wire Line
	4000 2150 3250 2150
Wire Wire Line
	4000 1750 4000 2150
Wire Wire Line
	3650 1950 3250 1950
Wire Wire Line
	3650 1950 3650 2950
Wire Wire Line
	3250 1850 3650 1850
Wire Wire Line
	3650 1600 3650 1850
$Comp
L Switch:SW_Push SW6
U 1 1 5FDAD58D
P 8200 1150
F 0 "SW6" H 8200 1435 50  0000 C CNN
F 1 "button_menu" H 8200 1344 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 8200 1350 50  0001 C CNN
F 3 "" H 8200 1350 50  0001 C CNN
	1    8200 1150
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 800  8000 800 
Wire Wire Line
	8000 800  8000 1150
Wire Wire Line
	8400 1150 8400 1500
Wire Wire Line
	8400 1500 8350 1500
Connection ~ 8400 1500
Wire Wire Line
	9500 5300 9500 5150
Wire Wire Line
	9500 5150 8250 5150
Wire Wire Line
	8250 5150 8250 5450
$Comp
L Connector:Conn_01x02_Male J20
U 1 1 5FF6EA5E
P 10800 5500
F 0 "J20" H 10772 5380 50  0000 R CNN
F 1 "powerbank" H 10772 5471 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 10800 5500 50  0001 C CNN
F 3 "~" H 10800 5500 50  0001 C CNN
	1    10800 5500
	-1   0    0    1   
$EndComp
Connection ~ 10850 5700
Connection ~ 10850 4650
Wire Wire Line
	10850 4650 10850 5700
$Comp
L Connector:Conn_01x02_Male J21
U 1 1 5FF977A1
P 11150 2250
F 0 "J21" H 11123 2130 50  0000 R CNN
F 1 "9V" H 11123 2221 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 11150 2250 50  0001 C CNN
F 3 "~" H 11150 2250 50  0001 C CNN
	1    11150 2250
	-1   0    0    1   
$EndComp
Wire Wire Line
	10600 5500 10600 5700
Wire Wire Line
	3550 1300 3400 1300
Wire Wire Line
	3550 4550 3550 1300
Wire Wire Line
	4550 1100 4550 3750
Wire Wire Line
	4550 1100 4300 1100
Wire Wire Line
	3650 900  3650 1500
Wire Wire Line
	3500 1000 3400 1000
Wire Wire Line
	3650 900  3400 900 
Wire Wire Line
	4050 6700 3900 6700
Wire Wire Line
	4050 5100 4050 6700
Wire Wire Line
	4350 900  4350 3950
Wire Wire Line
	4350 900  4300 900 
Wire Wire Line
	4400 1300 4400 1500
Wire Wire Line
	4300 1300 4400 1300
Wire Wire Line
	4450 1200 4300 1200
Connection ~ 9200 1400
Wire Wire Line
	9200 1400 9200 2650
$EndSCHEMATC
