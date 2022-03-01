import serial
import time

ser = serial.Serial("COM6", 115200, timeout = 1)  # open serial port
time.sleep(2)  

print(ser.readline().decode("utf-8").rstrip())

# set home
ser.write(str("G28" + '\n').encode())

# put robot in different directions
gcodes = []

gcodes.append("G01 Z-320")

gcodes.append("G01 X-100 Y100 Z-320")
gcodes.append("G01 Z-350")
gcodes.append("G01 Z-320")
gcodes.append("G01 X-100 Y-100 Z-320")
gcodes.append("G01 Z-350")
gcodes.append("G01 Z-320")
gcodes.append("G01 X100 Y-100 Z-320")
gcodes.append("G01 Z-350")
gcodes.append("G01 Z-320")
gcodes.append("G01 X100 Y100 Z-320")
gcodes.append("G01 Z-350")
gcodes.append("G01 Z-320")


"""
gcodes.append('G01 Z-320')
gcodes.append('G01 X-100')
gcodes.append('G01 Z-350')

gcodes.append('G01 Z-320')
gcodes.append('G01 X100')
gcodes.append('G01 Z-350')

gcodes.append('G01 Z-320')
gcodes.append('G01 X100 Y100')
gcodes.append('G01 Z-350')

gcodes.append('G01 X-100 Y-100 Z-320')
gcodes.append('G01 Z-350')
"""
count = 0
count_max = 20

while count < count_max: 
    for gcode in gcodes:
        ser.write(str(gcode + '\n').encode())
        response = ser.readline().decode("utf-8").rstrip()
        print("Sent gcode: " + gcode + " - Robot answer: " + response)
    
    count = count + 1

ser.close()  # close port