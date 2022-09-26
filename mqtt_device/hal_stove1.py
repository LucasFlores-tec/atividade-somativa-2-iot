import random
# import RPi.GPIO as GPIO
# import Adafruit_DHT as DHT
# GPIO.setmode(GPIO.BCM)  # Select BCM mode
# GPIO.setuo(17, GPIO.OUT)  # Select a pin as output

currentTemp1 = 0
trigger1 = 0
temperature1 = 0
humidity1 = 0


def tempController1(temp1):
    globals()['currentTemp1'] = temp1
    return currentTemp1


def heater_st1(state: str):
    if state == 'on':
        print('Heater ON')
        globals()['trigger1'] = 1
        # GPIO.output(17, 1)  # Turn the heater ON
    else:
        print('Heater OFF')
        globals()['trigger1'] = 0
        # GPIO.output(17, 0)  # Turn the heater OFF
    return state


def temperature_st1():
    # Passing as parameters de model of the module and the pin in which is connected
    # It's going to read the humidity and temperature values from the module DHT11
    # humidity, temperature = DHT.read_retry(DHT.DHT11, 4)
    # return temperature  # Return the temperature read from the module DHT11
    if trigger1 == 1:
        if globals()['temperature1'] < 28:
            globals()['temperature1'] += 1
        elif globals()['temperature1'] > 32:
            globals()['temperature1'] -= 1
    elif trigger1 == 0:
        globals()['temperature1'] = random.randrange(0, 50)
    return temperature1


def humidity_st1():
    # Passing as parameters de model of the module and the pin in which is connected
    # It's going to read the humidity and temperature values from the module DHT11
    # humidity, temperature = DHT.read_retry(DHT.DHT11, 4)
    # return humidity     # Return the humidity read from the module DHT11
    if trigger1 == 1:
        if globals()['humidity1'] < 68:
            globals()['humidity1'] += 1
        elif globals()['humidity1'] > 72:
            globals()['humidity1'] -= 1
    if trigger1 == 0:
        globals()['humidity1'] = random.randrange(0, 100)
    return humidity1
