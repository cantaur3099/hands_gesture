import serial      
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com6',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print (incoming)
    
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'],  0.2)

    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  
 
    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right') 

    if 'Vup' in incoming: 
        pyautogui.hotkey('ctrl', 'up')
          
    if 'Vdown' in incoming: 
        pyautogui.hotkey('ctrl',' down ' )
        
    if 'MUTE' in incoming: 
        pyautogui.hotkey('ctrl','         volumemute ' )
        
        
#    if 'Play/Pause' in incoming:
#        pyautogui.typewrite(['space'],  0.2)
#
#    if 'Page Up' in incoming:
#        pyautogui.hotkey('ctrl', 'pageup')  
# 
#    if 'Page Down' in incoming:
#        pyautogui.hotkey('ctrl', 'pagedown') 
#
#    if 'Vup' in incoming: 
#        pyautogui.hotkey('ctrl', 'volumeup')
#          
#    if 'Vdown' in incoming: 
#        pyautogui.hotkey('ctrl','volumedown' )
#        
#    if 'Refresh' in incoming: 
#        pyautogui.hotkey('browserrefresh' )    
#        
        
   
incoming   = "";