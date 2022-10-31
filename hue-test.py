#!/usr/bin/env python3

from phue import Bridge

def main():
    print("HUE Test")

    b = Bridge('192.168.1.7')

    # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
    b.connect()

    # Get the bridge state (This returns the full dictionary that you can explore)
    b.get_api()

    # Get a flat list of light objects
    lights = b.lights
    for l in lights:
        print(l.name)

    #b.set_light('Small lamp', 'on', True)
    #b.set_light('Small lamp', 'bri', 254)

    # Get a flat list of sensor objects
    sensors = b.sensors
    for s in sensors:
        print(s.name)


    print(f"GOT: {b.get_light('Ceiling 5')}")
    
#-----------------------------
if __name__ == "__main__":
    main()
    
