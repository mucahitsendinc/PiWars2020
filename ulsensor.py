import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
from time import sleep
import PiWarsTurkiyeRobotKiti2019
joystik = PiWarsTurkiyeRobotKiti2019.Kumanda()  
joystik.dinlemeyeBasla()
#Disable warnings (optional)
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
motorlar.hizlariAyarla(300, 300)
def olc():
    GPIO.output(TRIG, False)
    print ("Olculuyor...")
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
        print ("Mesafe:",distance - 0.5,"cm")
        if distance <= 6:
            motorlar.hizlariAyarla(0, 0)
            a=0
            while a==0:
                Lsag, Lyukari = joystik.solVerileriOku() #Lsag = joystick sağ sola çevirilmesi
                Rsag, Ryukari = joystik.sagVerileriOku() #LYukari ise yukarı aşağı
                tuslar = joystik.butonlariOku()
                if Lsag==1 or Lyukari==1 or Rsag==1 or Ryukari==1 or Lsag==-1 or Lyukari==-1 or Rsag==-1 or Ryukari==-1:
                    print("baştan başlıyor.")
                    a=1
                else:
                    print("tuş bekleniyor")
            olc()
        elif distance > 6 and distance < 10:
            sleep(0.03)
            motorlar.hizlariAyarla(100, 100)
            olc()
        elif distance > 10 and distance < 20:
            sleep(0.05)
            motorlar.hizlariAyarla(200, 200)
            olc()
        elif distance > 20 and distance < 30:
            motorlar.hizlariAyarla(300, 300)
            olc()
        elif distance > 30 and distance < 40:
            sleep(0.09)
            motorlar.hizlariAyarla(300, 300)
            olc()
        elif distance > 40 and distance < 50:
            sleep(0.11)
            motorlar.hizlariAyarla(300, 300)
            olc()
        elif distance > 50 and distance < 300:
            sleep(0.5)
            motorlar.hizlariAyarla(300, 300)
            olc()
        else:
            print ("Menzil asildi")
            olc()
olc()