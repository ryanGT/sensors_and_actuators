# Note: you must run "sudo pigpiod" at a terminal before running this code.
# That command starts the pigpio daemon 
import time
import pigpio

led_pin = 17# this is BCM GPIO 17 or raspi physical pin 11
            # see this pinout:
            # https://ms-iot.github.io/content/images/PinMappings/RP2_Pinout.png

#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(led_pin, pigpio.OUTPUT)

# pi set frequency
pi.set_PWM_frequency(led_pin, 1000)#1000 Hz or 1kHz
pi.set_PWM_range(led_pin, 100)#range will go from 0-100

# fade in
for i in range(11):
    #i will go from 0-10
    pi.set_PWM_dutycycle(led_pin,i*10)
    time.sleep(0.5)

# fade out
for i in range(10,-1,-1):
    #i will go through the list [10,9,8,...,0]
    pi.set_PWM_dutycycle(led_pin,i*10)
    time.sleep(0.5)


#cleanup
pi.set_PWM_dutycycle(led_pin,0)
pi.set_mode(led_pin, pigpio.INPUT)

#disconnect
pi.stop()
