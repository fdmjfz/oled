import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from gpiozero import CPUTemperature
import time
import psutil

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height),
        outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0

font = ImageFont.truetype('/home/fdmrpi/Documents/python/oled/font/OpenSans-Bold.ttf', 12, encoding='unic')

while True:
    draw.rectangle((0, 0, width, height),
            outline=0, fill=0)

    cpu_temp = CPUTemperature().temperature
    cpu_temp = round(cpu_temp, 1)
    cpu_use = psutil.cpu_percent()
    cpu_use = round(cpu_use, 1)
    ram_use = psutil.virtual_memory().percent
    ram_use = round(ram_use, 1)

    draw.text((x, top), "CPU Temp:  " + str(cpu_temp) + " ºC",
            font=font, fill=255)
    draw.text((x, top+16), "CPU Use:  " + str(cpu_use) + " %",
            font=font, fill=255)
    draw.text((x, top+32), "RAM Use:  " + str(ram_use) + " %",
            font=font, fill=255)

    disp.image(image)
    disp.display()
    time.sleep(1)
