import PiWarsTurkiyeRobotKiti2019
import RPi.GPIO as GPIO
from time import sleep
import time
rota=0
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output


TRIG = 26
ECHO = 20

print ("HC-SR04 mesafe sensoru")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()

eksen=0
sayacsag=0
sayacsol=0
yon=0
def engelkontrol():
  engelim=0
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
        return 0
    elif distance < 15:
        return 1
  else:
    engelim=1


sol=0
sag=0

while True:
    
   
    a=engelkontrol()
    if yon==1:
        sag=-480
        sol=480
        sayacsag=sayacsag+1
        sayacsol=0
    else:
        sol=-480
        sag=480
        sayacsol=sayacsol+1
        sayacsag=0
    print(a,"--",sayacsag,"---",sayacsol)
    if a==0:
        motorlar.hizlariAyarla(sol,sag)
    else:
        motorlar.hizlariAyarla(480,480)
    if sayacsag>=3:
        yon=1
    if sayacsol>=3:
        yon=0
    
    motorlar.hizlariAyarla(0,0)
    sleep(1)
    
    