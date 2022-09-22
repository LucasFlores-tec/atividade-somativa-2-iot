import paho.mqtt.client as mqtt
import time
from hal_stove1 import temperature_st1, humidity_st1, heater_st1
from definitions_stove1 import user, password, client_id, server, port


# Button functionality to turn on and off the heater
def message(client, userData, msg):
    vetor = msg.payload.decode().split(',')
    heater_st1('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')


# Start the connection
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

# Subscribe
client.on_message = message
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop_start()

# System behavior
times = 0
while times <= 10:
    client.publish(f'v1/{user}/things/{client_id}/data/0', temperature_st1())
    client.publish(f'v1/{user}/things/{client_id}/data/1', humidity_st1())
    time.sleep(5)
    times += 1

client.disconnect()
