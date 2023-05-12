import network
import socket
import json
from time import sleep
from lib.picozero import pico_temp_sensor, pico_led
import machine

ssid = 'ssid'
password = 'password'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip  

def open_socket(ip, port):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection
    
def serve(connection):
    #Start a web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        data = {}
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            if pico_led.value == 1:
                data['ack'] = 'Success'
            else:
                data['ack'] = 'Failed'
        if request == '/lightoff?':
            pico_led.off()
            if pico_led.value == 0:
                data['ack'] = 'Success'
            else:
                data['ack'] = 'Failed'
        if request == '/state?':
            data['led'] = pico_led.value
            data['temp'] = pico_temp_sensor.temp
        else:
            data['error'] = 'Invalid Request'
        client.send(json.dumps(data))
        client.close()
        
    
try:
    ip = connect()
    connection = open_socket(ip, 80)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()