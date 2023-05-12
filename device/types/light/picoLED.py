from picozero import pico_temp_sensor, pico_led
from types.light.base import base

class picoLED(base):
    __all__ = ['request', '__init__']
    
    def __init__(self):
        super().__init__()
        
    def request(self, request: str) -> dict:
        data = {}
        if request == '/lighton?':
            if self.set_light(True):
                data['ack'] = 'Success'
            else:
                data['ack'] = 'Failed'
        elif request == '/lightoff?':
            if self.set_light(False):
                data['ack'] = 'Success'
            else:
                data['ack'] = 'Failed'
        elif request == '/state?':
            data['led'] = self.get_state()
            data['temp'] = self.get_temp()
        else:
            data['error'] = 'Invalid Request'
        return data
    
    def get_state(self) -> bool:
        return bool(pico_led.value)
    
    def set_light(self, state):
        if state:
            pico_led.on()
        else:
            pico_led.off()
        if state and self.get_state():
            return True
        else:
            return False
    
    def get_temp(self):
        return pico_temp_sensor.temp
    
    def toggle_light(self):
        return pico_led.toggle()