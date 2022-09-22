import paho.mqtt.client as mqtt
import time
from hal_stove2 import temperature_st2, temperature_st2_stON, humidity_st2, heater_st2
from definitions_stove2 import user, password, client_id, server, port


# Button functionality to turn on and off the heater
def message(client, userData, msg):
    vetor = msg.payload.decode().split(',')
    heater_st2('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')


# Start the connection
client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

# Subscribe
client.on_message = message
client.subscribe(f'v1/{user}/things/{client_id}/cmd/5')
client.loop_start()

# System behavior
while True:
    client.publish(f'v1/{user}/things/{client_id}/data/3', temperature_st2())
    client.publish(f'v1/{user}/things/{client_id}/data/4', humidity_st2())
    time.sleep(100)

# client.disconnect()
