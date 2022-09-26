import random

currentTemp2 = 0
trigger2 = 0
temperature2 = 0
humidity2 = 0


def tempController2(temp2):
    globals()['currentTemp2'] = temp2
    return currentTemp2


def heater_st2(state: str):
    if state == 'on':
        print('Heater ON')
        globals()['trigger2'] = 1
    else:
        print('Heater OFF')
        globals()['trigger2'] = 0
    return state


def temperature_st2():
    if trigger2 == 1:
        if globals()['temperature2'] < 30:
            globals()['temperature2'] += 1
        elif globals()['temperature2'] > 30:
            globals()['temperature2'] -= 1
    elif trigger2 == 0:
        globals()['temperature2'] = random.randrange(0, 50)
    return temperature2


def humidity_st2():
    if trigger2 == 1:
        if globals()['humidity2'] < 70:
            globals()['humidity2'] += 1
        elif globals()['humidity2'] > 70:
            globals()['humidity2'] -= 1
    if trigger2 == 0:
        globals()['humidity2'] = random.randrange(0, 100)
    return humidity2
