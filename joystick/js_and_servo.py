import machine
import time
import math
657083
hPin=27
vPin=26
hJoy= machine.ADC(hPin)
vJoy= machine.ADC(vPin)
servoPin = 15
servo = machine.PWM(machine.Pin(servoPin))
servo.freq(50)
servo.duty_u16(0)

while True:
    hVal=hJoy.read_u16()
    #print(hVal)
    hCal=(hVal - 400) * (45 - 0) // (65535 - 400) + 0
    pwmVal = 36.41 * hCal + 1638
    #servo.duty_u16(int(pwmVal))
    #print(f'pre={hVal}, post={hCal}')
    #vVal=vJoy.read_u16()
    
    #hCal=int(-.00306*hVal+100.766)
    #vCal=int(.00306*vVal-100.766)
    
    #deg=math.atan2(vCal,hCal)*360/2/math.pi
    #if hCal==0:
    #    hCal=1
    #if deg<0:
    #    deg=deg+360
    
    #mag=math.sqrt(hCal**2+vCal**2)
    #if mag<=4:
    #    hCal=0
    #    vCal=0
    
    print(f'{hVal},{hCal}')
    time.sleep_ms(50)