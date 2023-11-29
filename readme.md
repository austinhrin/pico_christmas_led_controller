# Raspberry Pi Pico Christmas Light Controller

- proof of concept using salvaged IOR IRFP350 N channel mosfets
    - pin 1 gate
    - pin 2 drain
    - pin 3 source
- wiring the mosfets
    - connect gate pin to the PWM pin on the Pico
    -  connect drain pin to the color to control on your led strip
    - connect source pin to your power supply of choice
    - if using an external power supply than the one for the Pico connect a ground pin from the Pico to the ground of your power supply

## Useful links for this project
- https://learn.adafruit.com/rgb-led-strips/usage
- https://howchoo.com/pico/control-leds-with-the-raspberry-pi-pico/
- https://www.youtube.com/watch?v=qA6nqfzuF40