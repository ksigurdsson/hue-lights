#!/usr/bin/env python3

import time

from phue import Bridge

def main():

    b = Bridge('192.168.1.7')

    # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
    b.connect()

    # Get the bridge state (This returns the full dictionary that you can explore)
    b.get_api()

    #lights = ['Ceiling 5', 'Ceiling 6']
    lights = [
        'Front Flood 1',
        'Front Flood 2',
        'Porch',
        'Gate Left Top',
        'Gate Left Bottom',
        'Gate Right Top',
        'Gate Right Bottom'
    ]

    colours = {
        "orange": {"hue": 4819,
                   "sat": 254},
        "purple": {"hue": 53212,
                   "sat": 254},
        "green":  {"hue": 25600,
                   "sat": 254}}

    command = {
        "on" : True,
        "bri": 254,
        "hue": colours["orange"]["hue"],
        "sat": colours["orange"]["sat"],
        "transitiontime": 50
    }

    try:
        print("Running...press Ctrl-C to interrupt")
        
        while True:
    
            for colour in colours:
                command["bri"] = 254
                command["hue"] = colours[colour]['hue']
                command["sat"] = colours[colour]['sat']
                b.set_light(lights, command)

                time.sleep(13)

                command["bri"] = 10
                b.set_light(lights, command)
                time.sleep(6)

    except KeyboardInterrupt:
        pass

    # Reset the lights back to white and turn off when finished
    command["on"] = False
    command["bri"] = 254
    command["hue"] = 15335
    command["sat"] = 121
    command["transitiontime"] = 0
    
    b.set_light(lights, command)

    #print(f"GOT: {b.get_light('Ceiling 5')}")


    
#-----------------------------
if __name__ == "__main__":
    main()
    
