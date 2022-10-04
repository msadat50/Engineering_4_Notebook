#type: ignore
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import board
import busio
import adafruit_mpu6050
import digitalio 

displayio.release_displays() 
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP12)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

ledred=digitalio.DigitalInOut(board.GP3)
ledred.direction=digitalio.Direction.OUTPUT

while True:
    # create the display group
    splash = displayio.Group()

    # add title block to display group
    title = "ANGULAR VELOCITY"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)    

    title = f"x {mpu.gyro[0]} rad/s"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=15)
    splash.append(text_area)  
    if mpu.acceleration[0] > 9:
        ledred.value=True 
        print ( mpu.acceleration[0])
        ledred.value=False 

    title = f"Y {mpu.gyro[1]} rad/s"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=25)
    splash.append(text_area) 
    if mpu.acceleration[1] < -9:
        ledred.value=True 
        print ( mpu.acceleration[0])
        ledred.value=False

    title = f"z {mpu.gyro[2]} rad/s"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=35)
    splash.append(text_area)
    if mpu.acceleration[2] > 9:
        ledred.value=True 
        print ( mpu.acceleration[0])
        ledred.value=False
    # you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
    # Don't forget to round the angular velocity values to three decimal places

    # send display group to screen
    display.show(splash)