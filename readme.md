# Raspberry Pi Pico Christmas Light Controller

- IRLB8721 N channel mosfets (full 24 volt output to led strips)
    - pin 1 gate, pin 2 drain, pin 3 source    
- wiring the mosfets
    - connect gate pin to the PWM pin on the Pico
    -  connect drain pin to the color to control on your led strip
    - connect source pin to your power supply of choice
    - if using an external power supply than the one for the Pico connect a ground pin from the Pico to the ground of your power supply

## Useful links for this project
- https://learn.adafruit.com/rgb-led-strips/usage
- https://howchoo.com/pico/control-leds-with-the-raspberry-pi-pico/
- https://www.youtube.com/watch?v=qA6nqfzuF40
- links about mosfet voltage drop
    - proof of concept using salvaged IOR IRFP350 N channel mosfets
        - only partial voltage was passed to led strips due to the mosfet not having a high enough voltage to operate
        - pin 1 gate, pin 2 drain, pin 3 source
    - https://electronics.stackexchange.com/questions/545038/voltage-drop-over-mosfet-controlled-by-microcontroller
    - https://electronics.stackexchange.com/questions/443623/driving-led-with-an-n-channel-mosfet