from machine import Pin, ADC
from time import sleep
from machine import Pin, SoftI2C
import ssd1306
import framebuf
from time import sleep

# Initialize the I2C and SSD1306 display
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
oled_width = 128
oled_height = 64
w = ADC(Pin(35))
w.atten(ADC.ATTN_11DB)

image_water = bytearray([0x04,0x00,0x04,0x00,0x0c,0x00,0x0e,0x00,0x1e,0x00,0x1f,0x00,0x3f,0x80,0x3f,0x80,0x7e,0xc0,0x7f,0x40,0xff,0x60,0xff,0xe0,0x7f,0xc0,0x7f,0xc0,0x3f,0x80,0x0f,0x00])
image_arrow = bytearray([0x20,0x70,0xf8])
image_face = bytearray([0x00,0x00,0x00,0x00,0x00,0xc0,0x0c,0xe0,0x06,0xf0,0x03,0xd8,0x01,0xcc,0x00,0xc0,0x00,0x00,0x00,0x00,0x20,0x00,0x40,0x00,0x80,0x00,0x80,0x00,0x80,0x00,0x80,0x00,0x80,0x00,0x40,0x00,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0xc0,0x0c,0xe0,0x06,0xf0,0x03,0xd8,0x01,0xcc,0x00,0xc0,0x00,0x00,0x00,0x00])

water = framebuf.FrameBuffer(image_water, 11, 16, framebuf.MONO_HLSB)
arrow = framebuf.FrameBuffer(image_arrow, 5, 3, framebuf.MONO_HLSB)
face = framebuf.FrameBuffer(image_face, 14, 29, framebuf.MONO_HLSB)

display.blit(water, 8, 40)
display.blit(face, 104, 18)
display.blit(arrow, 2, 20)
display.text(f'001%', 1, 25, 1)
display.text('IT IS SO', 26, 34, 1)
display.text('FUCKING ', 26, 42, 1)
display.text('WET', 26, 50, 1)
display.rect(2, 2, 92, 16, 1)
display.fill_rect(4, 4, 88, 12, 1)
display.rect(96, 2, 30, 60, 1)
display.rect(2, 34, 23, 28, 1)
display.show()

while True:
    x = w.read()
    x = x/4095*100
    display.fill_rect(26, 34, 63, 24, 0)
    if x >= 92 :
        print(f"{x} SHIT IT IS SO FUCKING WET")
        display.text('IT IS SO', 26, 34, 1)
        display.text('FUCKING ', 26, 42, 1)
        display.text('WET >:3c', 26, 50, 1)
    elif x >= 80 :
        print(f"{x} ITS ALMOST WET")
        display.text('IT IS   ', 26, 34, 1)
        display.text('ALMOST  ', 26, 42, 1)
        display.text('WET  >:3', 26, 50, 1)
    elif x >= 50 :
        print(f"{x} ITS HALF WET")
        display.text('IT IS   ', 26, 34, 1)
        display.text('HALF WET', 26, 42, 1)
        display.text('     :3c', 26, 50, 1)
    elif x >= 15 :
        print(f"{x} ITS LITTLE WET")
        display.text('IT IS A ', 26, 34, 1)
        display.text('LITTLE  ', 26, 42, 1)
        display.text('WET.  :0', 26, 50, 1)
    elif x >= 0 :
        print(f"{x} ITS !WET")
        display.text("IT'S IS ", 26, 34, 1)
        display.text('NOT WET.', 26, 42, 1)
        display.text('      :(', 26, 50, 1)
    display.fill_rect(4, 4, 88, 12, 0)
    display.fill_rect(4, 4, int(88*(x/100)), 12, 1)
    display.fill_rect(1, 20, 94, 12, 0)
    display.blit(arrow, 2 + int(88*(x/100)), 20)
    print(f"{ 2 + int(88*(x/100))}")
    if 2 + int(88*(x/100)) >= 27 :
        if 2 + int(88*(x/100)) >= 65 :
            display.text(f'{x:06.2f}%', 39, 25, 1)
        else :
            display.text(f'{x:06.2f}%', -24 + int(88*(x/100)), 25, 1)
    else :
        display.text(f'{x:06.2f}%', 1, 25, 1)
    display.show()
    sleep(0.01)

