from machine import Pin, PWM, time_pulse_us
from neopixel import NeoPixel
import time
import random

#pins
switch=Pin(4, Pin.IN, Pin.PULL_UP)
buzzer=PWM(Pin(15))
trig=Pin(12, Pin.OUT)
echo=Pin(13, Pin.IN)

dataPin=5
pixels=10
np=NeoPixel(Pin(dataPin),pixels)

#distance
def get_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    duration=time_pulse_us(echo,1)
    distance=(duration*0.0343)/2
    return distance

#game
while True:
    if switch.value()==0:
        time.sleep(0.5)
        
        #clear leds
        for i in range(pixels):
            np[i]=(0,0,0)
        np.write()
        
        #random target
        target=random.randint(0,pixels-1)
        
        #show target
        np[target]=(0,0,100)
        np.write()
        
        time.sleep(7) #???????
        
        #player distance
        distance=get_distance()
        print(distance)#try again?
        
        #convert distance
        zone=int(distance/2) #every 5cm
        
        if zone==target:
            for i in range(pixels):
                np[i]=(0,100,0) #success
            np.write()
            
            buzzer.freq(1000)
            buzzer.duty_u16(20000)
            time.sleep(0.5)
            buzzer.duty_u16(0)
            
        else:
            for i in range(pixels):
                np[i]=(100,0,0) #fail
            np.write()
            
            buzzer.freq(500)
            buzzer.duty_u16(20000)
            time.sleep(0.5)
            buzzer.duty_u16(0)
            
        time.sleep(2)
        
        

