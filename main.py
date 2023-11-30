from machine import Pin, PWM
from time import sleep

# color mode options
# alternating_green_fade will alternate between both strips fading green
color_mode = "alternating_green_fade"

# turn on the onboard led
#led = Pin(25, Pin.OUT)
#led.toggle()
#print("hello is this thing on???")

#cool_white = PWM(Pin(0))
#blue = PWM(Pin(1))
#red = PWM(Pin(2))
strip1_green = PWM(Pin(3))
strip2_green = PWM(Pin(15))
#warm_white = PWM(Pin(4))

#cool_white.freq(500)
#blue.freq(10000)
#red.freq(500)
strip1_green.freq(1000)
strip2_green.freq(1000)
#warm_white.freq(500)

# make it fade
fade_sleep = 0.0001 #0.0001
count_steps = 1
duty_range = 65025

while True:
    if color_mode == "alternating_green_fade"
        for duty in range(0, duty_range, count_steps):
            # fade in
            strip1_green.duty_u16(duty)
            # fade out
            reverse_duty = duty_range - duty
            strip2_green.duty_u16(reverse_duty)
            sleep(fade_sleep)
        for duty in range(duty_range, 0, -count_steps):
            # fade out
            strip1_green.duty_u16(duty)
            # fade in
            reverse_duty = duty_range - duty
            strip2_green.duty_u16(reverse_duty)
            sleep(fade_sleep)
