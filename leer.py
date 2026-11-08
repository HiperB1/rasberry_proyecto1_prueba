import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
from time import sleep


lcd = CharLCD('PCF8574', 0x3F, cols=16, rows=2)   # cambia 0x27 si te salió 0x3f


lector = SimpleMFRC522()
try:
    lcd.clear()
    lcd.write_string('Hola Juan!')
    lcd.cursor_pos = (1, 0)        # (fila, columna) → segunda línea
    lcd.write_string('RFID listo')
    sleep(2)
    lcd.clear()
    lcd.write_string('Acerca tu tarjeta')
    sleep(2)
    uid, texto = lector.read()      # se bloquea hasta detectar una
    lcd.write_string(f"UID: {uid}")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Texto: {texto.strip()}")
    print(f"UID: {uid}")

finally:
    GPIO.cleanup()

