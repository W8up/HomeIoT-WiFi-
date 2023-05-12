import network
import socket
import json
from time import sleep
import machine
import types.light.picoLED as device #Type of device see /types
#Port to use
port = 80

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
        try:
            request = request.split()[1]
        except IndexError:
            pass
        data = device.request(request)
        client.send(json.dumps(data))
        client.close()
        
    
try:
    ip = connect()
    connection = open_socket(ip, port)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()