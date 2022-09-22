import random

temperature = random.randrange(20, 40)


def temperature_st2():
    return temperature


def temperature_st2_stON():
    return temperature + 1


def humidity_st2():
    return random.randrange(60, 80)


def heater_st2(state: str):
    if state == 'on':
        print('Heater ON')
    else:
        print('Heater OFF')
