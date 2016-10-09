# script to blink LED's two at a time for Bryce and Naz's bush outside during halloween

import time
#GPIOs that are available
#0,1,2,3,4,7,8,9,10,11,14,15,17,18,21,22,23,24,25,27
#Map

#Use the following GPIOs for LEDs
GPIO_redeyes1 = '0'
GPIO_redeyes2 = '1'
GPIO_greeneyes1 = '2'
GPIO_greeneyes2 = '3'
GPIO_blueeyes1 = '4'
GPIO_blueeyes2 = '7'
GPIO_redeyes1 = '8'
GPIO_redeyes2 = '9'
GPIO_greeneyes1 = '10'
GPIO_greeneyes2 = '11'
GPIO_blueeyes1 = '14'
GPIO_blueeyes2 = '15'
GPIO_redeyes1 = '17'
GPIO_redeyes2 = '18'
GPIO_greeneyes1 = '21'
GPIO_greeneyes2 = '22'
GPIO_blueeyes1 = '23'
GPIO_blueeyes2 = '24'
GPIO_blueeyes2 = '25'
GPIO_blueeyes2 = '27'


try:
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(GPIO_redeyes1))
    f.close()
except IOError as e:
    lol=0

#try:
#    f= open ('/sys/class/gpio/unexport','w')
#    f.write(str(GPIO_redeyes2)
#    f.close()
#except IOError as e:
#    lol=0

try:
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(GPIO_greeneyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.write(str(GPIO_blueeyes1))
    f.close()


#Export pin number
f= open ('/sys/class/gpio/export','w')
f.write(str(GPIO_redeyes1))
f.close()
#f= open ('/sys/class/gpio/export','w')
#f.write(str(GPIO_redeyes2))
#f.close()
f= open ('/sys/class/gpio/export','w')
f.write(str(GPIO_greeneyes1))
f.close()
#f= open ('/sys/class/gpio/export','w')
#f.write(str(GPIO_greeneyes2))
#f.close()
f= open ('/sys/class/gpio/export','w')
f.write(str(GPIO_blueeyes1))
f.close()
#f= open ('/sys/class/gpio/export','w')
#f.write(str(GPIO_blueeyes2))
#f.close()

#Define Pin Direction as Output for LED
path = '/sys/class/gpio/gpio' + GPIO_redeyes1 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
#path = '/sys/class/gpio/gpio' + GPIO_redeyes2 + '/direction'
#f= open (path,'w')
#f.write('out')
#f.close()
path = '/sys/class/gpio/gpio' + GPIO_greeneyes1 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
#path = '/sys/class/gpio/gpio' + GPIO_greeneyes2 + '/direction'
#f= open (path,'w')
#f.write('out')
#f.close()
path = '/sys/class/gpio/gpio' + GPIO_blueeyes1 + '/direction'
f= open (path,'w')
f.write('out')
f.close()
#path = '/sys/class/gpio/gpio' + GPIO_blueeyes2 + '/direction'
#f= open (path,'w')
#f.write('out')
#f.close()


while(1):
    path = '/sys/class/gpio/gpio' + GPIO_redeyes1 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(1)
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(0.5)

#    path = '/sys/class/gpio/gpio' + GPIO_redeyes2 + '/value'
#    f= open (path,'w')
#    f.write('1')
#    f.close()
#    time.sleep(1)
#    f= open (path,'w')
#    f.write('0')
#    f.close()
#    time.sleep(0.5)

    path = '/sys/class/gpio/gpio' + GPIO_greeneyes1 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(1)
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(0.5)

#    path = '/sys/class/gpio/gpio' + GPIO_greeneyes2 + '/value'
#    f= open (path,'w')
#    f.write('1')
#    f.close()
#    time.sleep(1)
#    f= open (path,'w')
#    f.write('0')
#    f.close()
#    time.sleep(0.5)

    path = '/sys/class/gpio/gpio' + GPIO_blueeyes1 + '/value'
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(1)
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(0.5)

#    path = '/sys/class/gpio/gpio' + GPIO_blueeyes2 + '/value'
#    f= open (path,'w')
#    f.write('1')
#    f.close()
#    time.sleep(1)
#    f= open (path,'w')
#    f.write('0')
#    f.close()
#    time.sleep(0.5)

#Unexport Pin
f= open ('/sys/class/gpio/unexport','w')
f.write(str(GPIO_redeyes1))
f.close()

#f= open ('/sys/class/gpio/unexport','w')
#f.write(str(GPIO_redeyes2))
#f.close()

f= open ('/sys/class/gpio/unexport','w')
f.write(str(GPIO_greeneyes1))
f.close()

#f= open ('/sys/class/gpio/unexport','w')
#f.write(str(GPIO_greeneyes2))
#f.close()

f= open ('/sys/class/gpio/unexport','w')
f.write(str(GPIO_blueeyes1))
f.close()

#f= open ('/sys/class/gpio/unexport','w')
#f.write(str(GPIO_blueeyes2))
#f.close()
