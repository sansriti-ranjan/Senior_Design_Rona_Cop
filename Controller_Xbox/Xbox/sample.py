from __future__ import print_function
import xbox

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)

# Instantiate the controller
joy = xbox.Joystick()

# Show various axis and button states until Back button is pressed
print("Xbox controller sample: Press Back button to exit")
while not joy.Back():
    # Not shown but can be used: joy.Back, joy.Start, joy.Guide(?Not 100% sure about this one)
    # Show connection status
    show("Connected:")
    showIf(joy.connected(), "Y", "N")
    # Analog sticks
    show("  Left X/Y:", fmtFloat(joy.leftX()), "/", fmtFloat(joy.leftY()))
    show("  Right X/Y:", fmtFloat(joy.rightX()), "/", fmtFloat(joy.rightY()))
    # Triggers
    show("  RightTrg:", fmtFloat(joy.rightTrigger()))
    show("  LeftTrg:", fmtFloat(joy.leftTrigger()))
    # A/B/X/Y buttons
    show("  Buttons:")
    showIf(joy.A(), "A")
    showIf(joy.B(), "B")
    showIf(joy.X(), "X")
    showIf(joy.Y(), "Y")
    # Dpad U/D/L/R
    show("  Dpad:")
    showIf(joy.dpadUp(),    "U")
    showIf(joy.dpadDown(),  "D")
    showIf(joy.dpadLeft(),  "L")
    showIf(joy.dpadRight(), "R")
    # Bumpers
    show("  Bumpers:")
    showIf(joy.leftBumper(), "L")
    showIf(joy.rightBumper(), "R")
    # Move cursor back to start of line
    show(chr(13))
# Close out when done
joy.close()
