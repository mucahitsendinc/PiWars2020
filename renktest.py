import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.cluster.vq import vq, kmeans
import io
import time
import time as t
import picamera
from numpy import uint8
from PIL import Image
stream=io.BytesIO()
#Pi kamera ile goruntu alimi gerceklestirilir.
with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(7)
    camera.capture(stream,'jpeg')
data=np.fromstring(stream.getvalue(),uint8)
image=cv2.imdecode(data,1)
#renklerin hsv renk uzayinda alt ve ust degerleri girilir.
red_lower = np.array([0, 100,100],np.uint8)
red_upper = np.array([10, 255, 255],np.uint8)
purple_lower = np.array([130, 100,100],np.uint8)
purple_upper = np.array([155, 255,255],np.uint8)
orange_lower = np.array([10, 100,100],np.uint8)
orange_upper = np.array([25, 255, 255],np.uint8)
green_lower = np.array([40, 100, 100],np.uint8)
green_upper = np.array([80, 255, 255],np.uint8)  
blue_lower=np.array([100,100,100],np.uint8)
blue_upper=np.array([130,255,255],np.uint8)
yellow_lower=np.array([25,100,100],np.uint8)
yellow_upper=np.array([39,255,255],np.uint8)
blur=cv2.GaussianBlur(image,(5,5),0)#gauss bulanikligi gerceklestirilir.
hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)# renk uzayi donusumu gerceklestirilir.
#renkleri belirtilen sinirlar icinde ayirt etme islemi uygulanir.
red=cv2.inRange(hsv, red_lower, red_upper)
green=cv2.inRange(hsv, green_lower, green_upper)
blue=cv2.inRange(hsv,blue_lower,blue_upper)
yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
orange=cv2.inRange(hsv,orange_lower,orange_upper)
purple=cv2.inRange(hsv,purple_lower,purple_upper)
#Morfolojik donusumler uygulanir.
red=cv2.erode(red,None,iterations=2)
red=cv2.dilate(red,None,iterations=2)
green=cv2.erode(green,None,iterations=2)
green=cv2.dilate(green,None,iterations=2)
blue=cv2.erode(blue,None,iterations=2)
blue=cv2.dilate(blue,None,iterations=2)
yellow=cv2.erode(yellow,None,iterations=2)
yellow=cv2.dilate(yellow,None,iterations=2)
orange=cv2.erode(orange,None,iterations=2)
orange=cv2.dilate(orange,None,iterations=2)
purple=cv2.erode(purple,None,iterations=2)
purple=cv2.dilate(purple,None,iterations=2)
#Kirmizi renk icin konturlama islemi yapilir.
_,cntr,_=cv2.findContours(red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i,c in enumerate(cntr):
    if cv2.contourArea(c)<1000:
  continue
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),0)
    cv2.putText(image,"Kirmizi",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
#Turuncu renk icin konturlama islemi yapilir.
_,cntr,_=cv2.findContours(orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i,c in enumerate(cntr):
    if cv2.contourArea(c)<1000:
  continue
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),0)
    cv2.putText(image,"TURUNCU",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
#Mor renk icin konturlama islemi yapilir.
_,cntr,_=cv2.findContours(purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i,c in enumerate(cntr):
    if cv2.contourArea(c)<1000:
  continue
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),0)
    cv2.putText(image,"MOR",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
#Yesil renk icin konturlama islemi yapilir.
_,cntr,_=cv2.findContours(green, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for i,c in enumerate(cntr):
    if cv2.contourArea(c)<1000:
  continue
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),0)
    cv2.putText(image,"Yesil",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
#Mavi renk icin konturlama islemi yapilir.
_,cntr,_=cv2.findContours(blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for i,c in enumerate(cntr):
    if cv2.contourArea(c)<1000:
  continue
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),0)
    cv2.putText(image,"Mavi",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
#Sari renk icin konturlama islemi yapilir.
_,cntr,_=cv2.findContours(yellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
for i,c in enumerate(cntr):
    if cv2.contourArea(c)<1000:
  continue
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),0)
    cv2.putText(image,"Sari",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0))
cv2.imshow("frame",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Goruntunun h,s,v histogramlari cizdirilir.
img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
hsv_image = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
hue, sat, val = hsv_image[:,:,0], hsv_image[:,:,1], hsv_image[:,:,2]
plt.figure(figsize=(10,8))
plt.subplot(311)                           
plt.subplots_adjust(hspace=.5)
plt.title("H")
plt.hist(np.ndarray.flatten(hue), bins=180)
plt.subplot(312)                             
plt.title("S")
plt.hist(np.ndarray.flatten(sat), bins=128)
plt.subplot(313)                             
plt.title("V")
plt.hist(np.ndarray.flatten(val), bins=128) 
plt.show()
def do_cluster(hsv_image, K):
    #goruntuden yukseklik, genislik ve kanal sayisi elde edilir.
    h,w,c = hsv_image.shape
    #goruntu matrisini (h * w) x c matrisine donusturerek kumeleme icin veri hazirlar
    cluster_data = hsv_image.reshape( (h*w,c) )
    # baslangic suresini tespit eder.
    t0 = t.time()
    #kumeleme yapar.
    codebook, distortion = kmeans(np.array(cluster_data[:,0], dtype=np.float), K)
    #son sureyi tespit eder.
    t1 = t.time()
    print "KUMELEME %0.5f SANIYE SURDU" % (t1-t0)
    #toplam pikseli hesaplar.
    tot_pixels = h*w
    #kumeleri olusturur.
    data, dist = vq(cluster_data[:,0], codebook)
    #her kume icin eleman sayisini hesaplar
    weights = [len(data[data == i]) for i in range(0,K)]
    #kumeleri siralar.
    color_rank = np.column_stack((weights, codebook))
    color_rank = color_rank[np.argsort(color_rank[:,0])]
    #yeni bos resim olusturur.
    new_image =  np.array([0,0,255], dtype=np.uint8) * np.ones( (500, 500, 3), dtype=np.uint8)
    img_height = new_image.shape[0]
    img_width  = new_image.shape[1]
    #her kume icin
    for i,c in enumerate(color_rank[::-1]):
        #kume baskinligini alir.
        weight = c[0]
        #dagilimin yuksekligi ve genisligi hesaplanir
        height = int(weight/float(tot_pixels) *img_height )
        width = img_width/len(color_rank)
        #konumu hesaplanir.
        x_pos = i*width
        color = np.array( [0,128,200], dtype=np.uint8)
        for j in range(len(c[1:])):
            color[j] = c[j+1]
        #yeni resmi olusturur.
        new_image[ img_height-height:img_height, x_pos:x_pos+width] = [color[0], color[1], color[2]]
        return new_image
plt.subplot(121),plt.imshow(img),plt.title("alinan goruntu")
new_image = do_cluster(hsv_image,6)#kac kume olusturulacagi belirlenir.Kume sayisi arttikca hiz azalir, hassasiyet artar.
new_image = cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)
plt.subplot(122),plt.imshow(new_image),plt.title("dominant renkler")
plt.show()