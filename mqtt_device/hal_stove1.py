import random
# import RPi.GPIO as GPIO
# import Adafruit_DHT as DHT
# GPIO.setmode(GPIO.BCM)  # Select BCM mode
# GPIO.setuo(17, GPIO.OUT)  # Select a pin as output


def temperature_st1():
    # Passing as parameters de model of the module and the pin in which is connected
    # It's going to read the humidity and temperature values from the module DHT11
    # humidity, temperature = DHT.read_retry(DHT.DHT11, 4)
    # return temperature  # Return the temperature read from the module DHT11
    return random.randrange(20, 40)


def humidity_st1():
    # Passing as parameters de model of the module and the pin in which is connected
    # It's going to read the humidity and temperature values from the module DHT11
    # humidity, temperature = DHT.read_retry(DHT.DHT11, 4)
    # return humidity     # Return the humidity read from the module DHT11
    return random.randrange(60, 80)


def heater_st1(state: str):
    if state == 'on':
        print('Heater ON')
        # GPIO.output(17, 1)  # Turn the heater ON
    else:
        print('Heater OFF')
        # GPIO.output(17, 0)  # Turn the heater OFF
