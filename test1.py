import serial
import time

# Ouvre le port srie  9600 bauds
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Commande gnrique de scan UHF (adapter si besoin)
# Exemple : BB 00 22 00 00 22 7E
scan_cmd = bytearray([0xBB, 0x00, 0x22, 0x00, 0x00, 0x22, 0x7E])

while True:
    print("Envoi de la commande de lecture...")
    ser.write(scan_cmd)
    
    # Attente de rponse
    time.sleep(0.5)
    
    # Lecture des donnes reues
    response = ser.read(64)  # essaie 64 ou plus selon la taille de rponse
    
    if response:
        print("Rponse brute :", response.hex())
    else:
        print("? Aucune rponse du lecteur RFID.")
