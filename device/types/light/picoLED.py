from picozero import pico_temp_sensor, pico_led
from types.light.base import base

class picoLED(base):
    __all__ = ['request', 'get_light_state', 'set', 'toggle', 'get_temp', '__init__']
    
    def __init__(self, name):
        super().__init__(name)
        
    def request(self, request: str) -> dict:
        data = {}
        attributes = {}
        if request == '/on?':
            self.set(True)
        elif request == '/off?':
            self.set(False)
        elif request == '/temp?':
            #data['temp'] = self.get_temp()
            pass
        elif request == '/toggle?':
            self.toggle()
        data['state'] = self.get_light_state()
        attributes['friendly_name'] = self.friendly_name
        data['attributes'] = attributes
        return data
    
    def get_light_state(self) -> bool:
        return bool(pico_led.value)
    
    def set(self, state: bool):
        if state:
            pico_led.on()
        else:
            pico_led.off()
    
    def get_temp(self):
        return pico_temp_sensor.temp
    
    def toggle(self):
        return pico_led.toggle()