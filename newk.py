import PiWarsTurkiyeRobotKiti2019
from time import sleep
joystik = PiWarsTurkiyeRobotKiti2019.Kumanda()  
joystik.dinlemeyeBasla()
motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  #motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  
m = 900
mod = 0

Rhiz = 0
Lhiz = 0

while True:
    Lsag, Lyukari = joystik.solVerileriOku() #Lsag = joystick sağ sola çevirilmesi
    Rsag, Ryukari = joystik.sagVerileriOku() #LYukari ise yukarı aşağı
    tuslar = joystik.butonlariOku()
    
    
    if (Lyukari>0 and Lsag>0) or (Lyukari<0 and Lsag<0):
        hizsol = Lyukari * m*-12   
    elif Lyukari==0 and (Lsag<0 or Lsag>0):
        hizsol = Lsag * m*-1       
    elif Lsag==0 and (Lyukari<0 or Lyukari>0):
        hizsol = Lyukari * m*-1
    else:
        hizsol=0
    
    if (Ryukari>0 and Rsag>0) or (Ryukari<0 and Rsag<0):
        hizsag = Ryukari * m*-12   
    elif Ryukari==0 and (Rsag<0 or Rsag>0):
        hizsag = Rsag * m*-1       
    elif Rsag==0 and (Ryukari<0 or Ryukari>0):
        hizsag = Ryukari * m*-1
    else:
        hizsag=0
    
    
     #Analog dışı tuşla
    motorlar.hizlariAyarla(round(hizsag),round(hizsol))
    print(hizsol,"--",hizsag)
    sleep(0.1)


