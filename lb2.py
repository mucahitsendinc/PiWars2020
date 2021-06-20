import PiWarsTurkiyeRobotKiti2019
import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG = 26
ECHO = 20
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()
solsay=0
sagsay=0

    
        
while True:
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    time.sleep(0.01)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
    if distance > 1 and distance < 400:
        print ("Karşı mesafe :",distance - 0.5,"cm")
    if distance > 15:
        motorlar.hizlariAyarla(300,300)
    elif distance < 15:
        motorlar.hizlariAyarla(0,0)
        if solsay==0 and sagsay==0:
            solsay=solsay+1
            motorlar.hizlariAyarla(-300,300)
            sleep(0.5)
        elif solsay>0:
            solsay=solsay+1
            motorlar.hizlariAyarla(-300,300)
            sleep(0.5)
        elif sagsay>0:
            sagsay=sagsay+1
            motorlar.hizlariAyarla(300,-300)
            sleep(0.5)
        if solsay>=5:
            solsay=0
        else:
            solsay=solsay+1
            sagsay=0
        if sagsay>=5:
            sagsay=0
        else:
            sagsay=sagsay+1
            solsay=0
            
        
    sleep(1)