from gpiozero import Servo


myGPIO=18
myCorrection=0
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

def srv(x):
    servo.value=x