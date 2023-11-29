from machine import Pin, PWM
from time import sleep

# turn on the onboard led
#led = Pin(25, Pin.OUT)
#led.toggle()
#print("hello is this thing on???")

#cool_white = PWM(Pin(0))
#blue = PWM(Pin(1))
#red = PWM(Pin(2))
strip1_green = PWM(Pin(3))
#strip2_green = PWM(Pin(3))
#warm_white = PWM(Pin(4))

#cool_white.freq(500)
#blue.freq(10000)
#red.freq(500)
strip1_green.freq(1000)
#strip2_green.freq(1000)
#warm_white.freq(500)

# make it fade
fade_sleep = 0.0001 #0.0001
count_steps = 2
duty_range = 65025

while True:
    for duty in range(0, duty_range, count_steps):
        strip1_green.duty_u16(duty)
        #reverse_duty = duty_range - duty
        #strip2_green.duty_u16(duty)
        sleep(fade_sleep)
    for duty in range(duty_range, 0, -count_steps):
        strip1_green.duty_u16(duty)
        #reverse_duty = duty_range + duty
        #strip2_green.duty_u16(duty)
        sleep(fade_sleep)
