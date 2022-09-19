import board
import digitalio 
import time
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT 
led.value = True
led.value = False 
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

