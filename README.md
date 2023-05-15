#How to setup pi pico w
    copy latest micro python firmware on to device available: https://micropython.org/download/rp2-pico-w/
    change ssid and password in creds.py
    find and change device type in main.py from /types

#Adding new types
    They must contain minimum:
        request()
        super of base for type
    should be added in __init__.py and __all__ for current dir

#Useful links
    #Home assistant
    https://www.home-assistant.io/integrations/http/
    https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things/
    https://developers.home-assistant.io/docs/api/rest/
