import RPi.GPIO as GPIO


in1 = 13
in2 = 19
en = 24

in3 = 20
in4 = 21
en2 = 23

GPIO.setmode(GPIO.BCM)

#motor 1

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.HIGH)  #directie fata
GPIO.output(in2,GPIO.LOW)   #
p1=GPIO.PWM(en,1000)

#motor 2

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.HIGH)  #directie fata
GPIO.output(in4,GPIO.LOW)   #
p2=GPIO.PWM(en2,1000)

p1.start(0)   #viteza 0 
p2.start(0)

def p(x):
    if x>=0:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    else:
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)

    p1.ChangeDutyCycle(abs(x))
    p2.ChangeDutyCycle(abs(x))