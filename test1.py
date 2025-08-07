import cv2

cap = cv2.VideoCapture(0)  # 0 pour /dev/video0
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
cap.set(cv2.CAP_PROP_EXPOSURE, -5)
# Définir la résolution si nécessaire
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ret, frame = cap.read()
if ret:
    cv2.imwrite('photo.jpg', frame)
    print("Photo prise avec succès.")
else:
    print("Erreur lors de la capture.")

cap.release()
