import serial
import time

ser = serial.Serial("COM6", 115200, timeout = 1)  # open serial port

time.sleep(2)

print(ser.readline().decode("utf-8").rstrip())

# set home
ser.write(str("G28" + '\n').encode())
ser.write(str("G01 F300" + '\n').encode())

# put robot in different directions
gcodes = []

gcodes.append("G01 Z-300")

gcodes.append("G01 X-100 Y100 Z-280")
gcodes.append("G01 Z-300")
gcodes.append("G01 Z-280")

gcodes.append("G01 X-100 Y-100 Z-280")
gcodes.append("G01 Z-300")
gcodes.append("G01 Z-280")

gcodes.append("G01 X100 Y-100 Z-280")
gcodes.append("G01 Z-300")
gcodes.append("G01 Z-280")

gcodes.append("G01 X100 Y100 Z-280")
gcodes.append("G01 Z-300")
gcodes.append("G01 Z-280")

count = 0
count_max = 99

while count < count_max: 
    for gcode in gcodes:
        ser.write(str(gcode + '\n').encode())
        response = ""
        while response == "":
            response = ser.readline().decode("utf-8").rstrip()
            if "Ok" in response: break

        print("Sent gcode: " + gcode + " - Robot answer: " + response)
    
    count = count + 1

ser.close()  # close port