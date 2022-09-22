import random


def temperature_st2():
    return random.randrange(20, 40)


def temperature_st2_stON():
    temp = random.randrange(20, 40)
    temp = temp + 1
    return temp


def humidity_st2():
    return random.randrange(60, 80)


def heater_st2(state: str):
    if state == 'on':
        print('Heater ON')
    else:
        print('Heater OFF')
