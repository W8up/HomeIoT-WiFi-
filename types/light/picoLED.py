from picozero import pico_temp_sensor, pico_led

__all__ = ['request']

def request(request: str) -> dict:
    data = {}
    if request == '/lighton?':
        pico_led.on()
        if pico_led.value == 1:
            data['ack'] = 'Success'
        else:
            data['ack'] = 'Failed'
    elif request == '/lightoff?':
        pico_led.off()
        if pico_led.value == 0:
            data['ack'] = 'Success'
        else:
            data['ack'] = 'Failed'
    elif request == '/state?':
        data['led'] = pico_led.value
        data['temp'] = pico_temp_sensor.temp
    else:
        data['error'] = 'Invalid Request'
    return data