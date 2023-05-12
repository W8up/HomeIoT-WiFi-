#Basic home IoT system based off the Pi pico w

#How to setup
    copy latest micro python firmware on to device available: https://micropython.org/download/rp2-pico-w/
    change ssid and password in creds.py
    find and change device type in main form /types

#Adding new types
    They must contain minimum:
        request()
        super of base for type
    should be added in __init__.py and __all__ for current dir