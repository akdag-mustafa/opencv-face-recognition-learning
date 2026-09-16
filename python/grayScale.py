import cv2
import numpy as np  

def grayScaleAlgoritm(renkli_goruntu):
    yukseklik, genislik, kanal_sayisi = renkli_goruntu.shape
    # Görüntünün boyutlarını alır.
    grayImage = np.zeros((yukseklik, genislik),dtype= np.uint8)
    # Gri tonlamalı görüntü için boş bir matris oluşturur.

    for y in range(yukseklik):
        for x in range(genislik):
         # Her piksel için döngü başlatır.

            b, g, r = renkli_goruntu[y, x]
            # Pikselin BGR değerlerini alır.

            grayValue = int(0.299 * r + 0.587 * g + 0.114 * b)
            # Gri tonlamalı değeri hesaplar.
            # Bu formül, insan gözünün farklı renkleri algılama duyarlılığına dayanmaktadır.
            # Kırmızı (R) daha fazla ağırlık alır çünkü insan gözü kırmızıya daha duyarlıdır.

            grayImage[y, x] = grayValue
            # Hesaplanan gri değeri yeni görüntüye atar.
    return grayImage


kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    # Kameradan bir kare okur.

    if not ret:
        break
        # Eğer kare alınamazsa döngüyü sonlandırır.

    grayFrame = grayScaleAlgoritm(frame)
    # Kameradan alınan kareyi gri tonlamalı hale getirir.

    cv2.imshow("Gri Tonlamalı Görüntü", grayFrame)
    # Gri tonlamalı görüntüyü ekranda gösterir.

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # 'q' tuşuna basıldığında döngüyü sonlandırır.