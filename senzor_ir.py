import board
import busio
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15 import ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Inițializare senzor IR
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.mode = Mode.SINGLE
canal = AnalogIn(ads, ADS.P0)

def citeste_valoare_ir():
    try:
        valoare = canal.value
        voltaj = canal.voltage
    except OSError:
        valoare = -1
        voltaj = 0.0
    return valoare, voltaj

def clasifica_material_ir(valoare):
    if valoare < 3100:
        return "Carton"
    elif 3100 <= valoare < 10000:
        return "Plastic"
    elif 10000 < valoare <= 16000:
        return "Sticla"
    else:
        return "Nimic in fata senzorului"