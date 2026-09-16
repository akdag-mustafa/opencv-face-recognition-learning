import cv2

kamera = cv2.VideoCapture(0)

if not kamera.isOpened():
    print("Kamera acilamadi.")
    exit()

while True:
    basarili, goruntu = kamera.read()

    if not basarili:
        print("Goruntu alinamadi.")
        break

    blurred_goruntu = cv2.blur(goruntu, (15, 15))

    cv2.imshow("Original", goruntu)
    cv2.imshow("Average Blur", blurred_goruntu)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()