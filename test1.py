import cv2
import time

# Ouvrir la camera (index 0 = /dev/video0)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Regler la resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Desactiver l'auto-exposition (mode manuel)
# 1.0 = auto, 0.25 = manuel sous OpenCV/V4L2
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)

# Definir une exposition manuelle adaptee
# Valeur a ajuster selon la luminosite et le driver
cap.set(cv2.CAP_PROP_EXPOSURE, 100)  # plus haut = plus lumineux

# Laisser le temps au capteur de s'adapter
time.sleep(2)

# Capturer une image
ret, frame = cap.read()
if ret:
    cv2.imwrite("photo.jpg", frame)
    print("Photo prise avec succes")
else:
    print("Erreur lors de la capture")

cap.release()
