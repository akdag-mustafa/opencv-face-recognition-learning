import cv2
# OpenCV kütüphanesini içe aktarır.
# Kamera açma, görüntü işleme, pencere gösterme gibi işlemleri bununla yapıyoruz.


cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
# Bilgisayarın kamerasını açar.
#
# 0:
# İlk kamerayı seç demektir. MacBook'un dahili kamerası genelde 0'dır.
#
# cv2.CAP_AVFOUNDATION:
# macOS'un kamera altyapısı olan AVFoundation'ı kullanmasını söyler.
#
# cap değişkeni artık kamerayı temsil eder.


while True:
    # Sonsuz döngü başlatır.
    # Kamera görüntüsü aslında sürekli alınan karelerden oluştuğu için
    # her kareyi tekrar tekrar okumamız gerekir.


    ret, frame = cap.read()
    # Kameradan bir adet görüntü karesi okur.
    #
    # ret:
    # Görüntü başarıyla alındıysa True olur.
    # Alınamadıysa False olur.
    #
    # frame:
    # Kameradan gelen gerçek renkli görüntüdür.
    # Aslında NumPy matrisi şeklinde tutulur.


    if not ret:
        # ret False ise kamera görüntüsü alınamamış demektir.

        break
        # while döngüsünü sonlandırır.


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Renkli görüntüyü gri tonlamalı görüntüye dönüştürür.
    #
    # frame:
    # Dönüştürülecek görüntü.
    #
    # cv2.COLOR_BGR2GRAY:
    # BGR renk düzeninden gri görüntüye dönüşüm yap demektir.
    #
    # OpenCV renkli görüntüleri genellikle:
    # B = Blue
    # G = Green
    # R = Red
    # şeklinde tutar.
    #
    # Gri görüntüde her piksel tek bir değere dönüşür:
    # 0   = siyah
    # 255 = beyaz


    blur = cv2.GaussianBlur(
        gray,
        (15, 15),
        0
    )
    # Görüntüye Gaussian Blur uygular.
    #
    # Amaç:
    # Görüntüdeki küçük detayları ve gürültüyü yumuşatmaktır.
    #
    # gray:
    # Bulanıklaştırılacak görüntü.
    #
    # (15, 15):
    # Kernel boyutudur.
    # Her piksel hesaplanırken çevresindeki 15x15 bölge dikkate alınır.
    #
    # Kernel boyutu genellikle tek sayı olmalıdır:
    # (3,3)
    # (5,5)
    # (15,15)
    #
    # Değer büyüdükçe görüntü daha fazla bulanıklaşır.
    #
    # Son parametre 0:
    # Gaussian dağılımının sigma değerini OpenCV otomatik hesaplasın demektir.


    cv2.imshow("Orijinal", frame)
    # Bir pencere açar ve frame görüntüsünü gösterir.
    #
    # "Orijinal":
    # Açılan pencerenin başlığıdır.
    #
    # frame:
    # Gösterilecek görüntüdür.


    cv2.imshow("Gri", gray)
    # Gri tonlamaya dönüştürdüğümüz görüntüyü ayrı bir pencerede gösterir.


    cv2.imshow("Gaussian Blur", blur)
    # Gaussian Blur uygulanmış görüntüyü ayrı pencerede gösterir.


    if cv2.waitKey(1) & 0xFF == ord("q"):
        # Klavyeden tuş girişini kontrol eder.
        #
        # cv2.waitKey(1):
        # Yaklaşık 1 milisaniye tuş girişini bekler.
        #
        # ord("q"):
        # q karakterinin sayısal ASCII/Unicode kodunu verir.
        #
        # Basılan tuş q ise koşul True olur.

        break
        # Döngüyü bitirir ve kamera programından çıkar.


cap.release()
# Kamerayı serbest bırakır.
# Program bittikten sonra kamera başka uygulamalar tarafından kullanılabilir.


cv2.destroyAllWindows()
# OpenCV tarafından açılan bütün pencereleri kapatır.