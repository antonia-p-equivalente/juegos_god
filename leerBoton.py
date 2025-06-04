import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def leer_boton():
    if ser.in_waiting > 0:
        linea = ser.readline().decode('utf-8').strip()
        return linea
    return None