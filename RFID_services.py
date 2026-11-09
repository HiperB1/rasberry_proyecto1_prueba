import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
from time import sleep


def leer() -> {str, str}:
    lcd = CharLCD('PCF8574', 0x3F, cols=16, rows=2)   # cambia 0x27 si te salió 0x3f
    lector = SimpleMFRC522()
    try:
        print("Llamada recibida intentado leer...")
        sleep(2)
        uid, texto = lector.read()      # se bloquea hasta detectar una
        print(f"UID: {uid}")
        print(f"Texto: {texto.strip()}")
        return texto

    finally:
        GPIO.cleanup()


def escribir(texto) -> str:
    lcd = CharLCD('PCF8574', 0x3F, cols=16, rows=2)   # cambia 0x27 si te salió 0x3f
    lector = SimpleMFRC522()
    try:
        print(f"Llamada recibida escribiendo: {texto}")
        sleep(2)
        lector.write(texto)
        print(f"Texto guardado: {texto.strip()}")
        return texto
        
    finally:
        GPIO.cleanup()