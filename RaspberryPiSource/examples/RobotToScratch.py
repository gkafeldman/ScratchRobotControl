from array import array
import socket
import time
import Robot

#HOST='127.0.0.1'
HOST='10.0.0.3'
PORT=42001

LEFT_TRIM = 0
RIGHT_TRIM = 10

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

def sendScratchCommand(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n >> 24) & 0xFF))
    a.append(chr((n >> 16) & 0xFF))
    a.append(chr((n >> 8) & 0xFF))
    a.append(chr(n & 0xFF))
    scratchSocket.send(a.tostring() + cmd)

print("connecting...")

scratchSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected = False;

while not connected:
    try:
        scratchSocket.connect((HOST, PORT))
        connected = True;
    except Exception as e:
        print"error:", e
        time.sleep(1)

print("connected")

#scratchSocket.send("hello")

time.sleep(0.5)

while 1:
    time.sleep(0.01)
    data = scratchSocket.recv(1024)
    #if not data:break

    myData = data[15]
    
    print(myData)

    #print("waiting")

    #print(data == 'u')

    if myData == "f":
        robot.forward(50)
    elif myData == "b":
        robot.backward(50)
    elif myData == "l":
        robot.left(50)
    elif myData == "r":
        robot.right(50)
    else:
        robot.stop()
