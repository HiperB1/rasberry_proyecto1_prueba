from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

lector = SimpleMFRC522()
try:
    print("Acerca una tarjeta...")
    texto = input("Introduce el texto a guardar en la tarjeta: ")
    lector.write(texto)
    print(f"Texto guardado: {texto.strip()}")
finally:
    GPIO.cleanup()