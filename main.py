from machine import Pin, PWM
from time import sleep

# color mode options
# alternating_green_fade will alternate between both strips fading green
# alternating_green_red_fade will alternate green/red on each strip back and forth fading
# flash_red_green_fade will keep both the strips the same color (red/green) instead of alternating and will fade between them
color_mode = "flash_red_green_fade"

# turn on the onboard led
#led = Pin(25, Pin.OUT)
#led.toggle()
#print("hello is this thing on???")

strip1_green = PWM(Pin(2))
strip1_red = PWM(Pin(3))
#strip1_blue = PWM(Pin(3))

strip2_green = PWM(Pin(10))
strip2_red = PWM(Pin(11))
#strip2_blue = PWM(Pin(12))

freq = 1000
start_freq = 100
strip1_green.freq(start_freq)
strip1_red.freq(start_freq)
#strip1_blue.freq(start_freq)

strip2_green.freq(start_freq)
strip2_red.freq(start_freq)
#strip2_blue.freq(start_freq)

start_duty = 0
strip1_green.duty_u16(start_duty)
strip1_red.duty_u16(start_duty)
#strip1_blue.duty_u16(start_duty)
strip2_green.duty_u16(start_duty)
strip2_red.duty_u16(start_duty)
#strip2_blue.duty_u16(start_duty)

# make it fade
fade_sleep = 0.0001 #0.0001
count_steps = 1  
duty_range = 65025
duty_min = 5000

while True:
    if color_mode == "alternating_green_fade":
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
    if color_mode == "alternating_green_red_fade":
        #strip1_red.freq(100)
        strip1_red.duty_u16(0)
        strip1_green.freq(freq)
        strip2_green.freq(freq)
        print("loop 1")
        for duty in range(0, duty_range, count_steps):
            # fade in
            strip1_green.duty_u16(duty)
            # fade out
            reverse_duty = duty_range - duty
            strip2_green.duty_u16(reverse_duty)
            sleep(fade_sleep)
        strip2_green.freq(100)
        strip2_red.freq(freq)
        print("loop 2")
        for duty in range(duty_range, 0, -count_steps):
            # fade out
            strip1_green.duty_u16(duty)
            # fade in
            reverse_duty = duty_range - duty
            strip2_red.duty_u16(reverse_duty)
            sleep(fade_sleep)
        strip1_green.freq(100)
        strip1_red.freq(freq)
        print("loop 3")
        for duty in range(0, duty_range, count_steps):
            # fade in
            strip1_red.duty_u16(duty)
            # fade out
            reverse_duty = duty_range - duty
            strip2_red.duty_u16(reverse_duty)
            sleep(fade_sleep)
        strip2_green.freq(freq)
        print("loop 4")
        for duty in range(duty_range, 0, -count_steps):
            # fade out
            strip1_red.duty_u16(duty)
            # fade in
            reverse_duty = duty_range - duty
            strip2_green.duty_u16(reverse_duty)
            sleep(fade_sleep)
        strip1_red.freq(100)
    if color_mode == "flash_red_green_fade":
        # red
        for duty in range(duty_min, duty_range, count_steps):
            # fade in
            strip1_red.duty_u16(duty)
            strip2_red.duty_u16(duty)
        for duty in range(duty_range, duty_min, -count_steps):
            # fade out
            strip1_red.duty_u16(duty)
            strip2_red.duty_u16(duty)
        strip1_red.duty_u16(0)
        strip2_red.duty_u16(0)
        # green
        for duty in range(duty_min, duty_range, count_steps):
            # fade in
            strip1_green.duty_u16(duty)
            strip2_green.duty_u16(duty)
        for duty in range(duty_range, duty_min, -count_steps):
            # fade out
            strip1_green.duty_u16(duty)
            strip2_green.duty_u16(duty)
        strip1_green.duty_u16(0)
        strip2_green.duty_u16(0)