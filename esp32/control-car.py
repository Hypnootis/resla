import serial

ser = serial.Serial("/dev/ttyUSB0", 115200)

input_value = ser.readline()


