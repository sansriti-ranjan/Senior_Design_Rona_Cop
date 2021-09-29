import xbox
import CarRun
import RPi.GPIO as GPIO
import time

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Instantiate the controller
controllerFlag = False
while controllerFlag == False:
    joy = xbox.Joystick()
    controllerFlag = joy.connected()

# Initialize the motor
CarRun.motor_init()

# Press back button to end driving session

while not joy.Back():
    leftstick_value = joy.leftX(0)
    if leftstick_value != 0:
        
        if leftstick_value < 0:
            CarRun.left(0.1)
        elif leftstick_value > 0:
            CarRun.right(0.1)
        else:
            CarRun.brake(0.1)
    else:
        if joy.rightTrigger() > 0.75:
            CarRun.run(0.1)
        elif joy.leftTrigger() > 0.75:
            CarRun.back(0.1)
        else:
            CarRun.brake(0.1)

