 # TEST2
import serial
import time

def parse_tag(frame):
    if frame[1] == 0x02 and frame[2] == 0x22:  # Notification de tag detecte
        epc_len = frame[4] - 5  # PL - RSSI(1) - PC(2) - CRC(2)
        epc = frame[8:8 + epc_len]
        epc_hex = ''.join(f'{b:02X}' for b in epc)
        print(f"Tag detecte : {epc_hex}")
    elif frame[2] == 0xFF:
        print("Aucun tag detecte ou erreur")

def main():
    # Ouvre le port serie USB (modifie si necessaire)
    try:
        ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=0.5)
    except serial.SerialException:
        print("Erreur : port serie non detecte. Verifie le branchement.")
        return

    # Commande Single Inventory : BB 00 22 00 00 22 7E
    inventory_cmd = bytearray([0xBB, 0x00, 0x22, 0x00, 0x00, 0x22, 0x7E])

    print("Lecture RFID en cours... (CTRL+C pour arreter)\n")

    try:
        while True:
            ser.write(inventory_cmd)
            time.sleep(0.01)
            response = ser.read(64)
            if len(response) >= 8 and response[0] == 0xBB and response[-1] == 0x7E:
                parse_tag(response)
    except KeyboardInterrupt:
        print("\nArret du script.")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
