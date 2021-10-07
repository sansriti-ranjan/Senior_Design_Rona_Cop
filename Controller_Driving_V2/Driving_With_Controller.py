import xbox
import CarRun
import RPi.GPIO as GPIO
import time

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Instantiate the controller
joy = xbox.Joystick()

# Initialize the motor
CarRun.motor_init()
#CarRun.servo_init()

# Press back button to end driving session

while not joy.Back():
    # Getting PWM values for left and right side of ATV for steering
    #print("LeftX ", joy.leftX())
    if joy.leftX(0) == 0:
        LeftPWM = 60
        RightPWM = 60
    elif joy.leftX(0) < 0:
        LeftPWM = 60
        RightPWM = round(60 + ((joy.leftX(0) * 60)))
    elif joy.leftX(0) > 0:
        LeftPWM = round(60 - (joy.leftX(0) * 60))
        RightPWM = 60
    if joy.leftBumper() == 1:
        CarRun.spin_left(0.1)
    elif joy.rightBumper() == 1:
        CarRun.spin_right(0.1)
    elif joy.rightTrigger() > 0.75:
        CarRun.run(0.1, LeftPWM, RightPWM)
    elif joy.leftTrigger() > 0.75:
        CarRun.back(0.1, LeftPWM, RightPWM)
    else:
        CarRun.brake(0.1)
""""
    joyx = round(50 + ((joy.rightX(0) * 50)))
    joyy = round(50 + ((joy.rightY(0) * 50)))
    CarRun.Camera_LR(joyx)
    CarRun.Camera_UD(joyy)
"""
    
