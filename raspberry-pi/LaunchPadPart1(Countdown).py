import time
import board
import digitalio 

ledred=digitalio.DigitalInOut(board.GP16)
ledred.direction=digitalio.Direction.OUTPUT
ledblue=digitalio.DigitalInOut(board.GP15)
ledblue.direction=digitalio.Direction.OUTPUT

for a in range(10,0,-1):
        if a is not 0:
        ledblue.value=True 
        print (a)
        time.sleep(0.5)
        ledblue.value=False
        time.sleep(0.5)

    else: 
        print ("liftoff")
        ledred.value=False 
        print (a)
        time.sleep(0.5)
        ledred.value=True
        time.sleep(0.5)
    
    
    


   
    

