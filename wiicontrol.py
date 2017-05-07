#!/usr/bin/python


#when setting up change: the ips and the lirc config name

import os
import cwiid
import time
from phue import Bridge

# TODO cleanup
b = Bridge('BRIDGEIP')
os.environ['MPD_HOST'] = 'MPDIP'
b.connect()

button_delay = 0.4

print 'Press 1 + 2'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "again"
  wii=cwiid.Wiimote()
  

print 'Connect'


wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print 'bye'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  if (buttons & cwiid.BTN_LEFT):
    os.system('mpc prev')
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    os.system('mpc next')
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):       
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):    
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    b.set_light(1,'on', True)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    b.set_light(1,'on', False)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    os.system('mpc toggle')  #pizza3.conf is the name of my lirc config
    os.system('irsend SEND_ONCE pizza3.conf KEY_POWER')
    time.sleep(button_delay)            

  if (buttons & cwiid.BTN_B):
    os.system('irsend SEND_ONCE pizza3.conf KEY_F')
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    os.system('irsend SEND_ONCE pizza3.conf KEY_I')
    time.sleep(0.1) 
    os.system('irsend SEND_ONCE pizza3.conf KEY_I')
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
	os.system('mpc volume -10')
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    os.system('mpc volume +10')
    time.sleep(button_delay)
