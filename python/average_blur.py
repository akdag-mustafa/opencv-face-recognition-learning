import cv2
import numpy as np


def kendi_blur_algoritmamiz(goruntu, kernel_boyutu):
    if kernel_boyutu % 2 == 0:
        raise ValueError("Kernel boyutu tek sayı olmalıdır.")

    yukseklik, genislik, kanal_sayisi = goruntu.shape
q
    bulanmis_goruntu = np.zeros_like(goruntu)

    kenar_bosluk = kernel_boyutu // 2

    kenarlari_genisletilmis_goruntu = np.pad(
        goruntu,
        (
            (kenar_bosluk, kenar_bosluk),
            (kenar_bosluk, kenar_bosluk),
            (0, 0)
        ),
        mode="edge"
    )

    for y in range(yukseklik):
        for x in range(genislik):
            bolge = kenarlari_genisletilmis_goruntu[
                y:y + kernel_boyutu,
                x:x + kernel_boyutu
            ]

            ortalama_renk = np.mean(
                bolge,
                axis=(0, 1)
            )

            bulanmis_goruntu[y, x] = ortalama_renk

    return bulanmis_goruntu


kamera = cv2.VideoCapture(0)

kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

if not kamera.isOpened():
    print("Kamera acilamadi.")
    exit()

while True:
    basarili, goruntu = kamera.read()

    if not basarili:
        print("Goruntu alinamadi.")
        break

    blurred_goruntu = kendi_blur_algoritmamiz(
        goruntu,
        5
    )

    cv2.imshow("Original", goruntu)
    cv2.imshow("Manual Python Blur", blurred_goruntu)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()