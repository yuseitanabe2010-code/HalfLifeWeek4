from machine import Pin, SPI
import st7789
import time
import sys
import select

spi = SPI(1, baudrate=30000000, sck=Pin(18), mosi=Pin(19))
display = st7789.ST7789(spi, 240, 240, reset=Pin(21), dc=Pin(20), cs=Pin(17))
display.init()
display.fill(0)

while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0.1)[0]:
        line = sys.stdin.readline().strip()
        if line:
            parts = line.split(',')
            display.fill(0)
            display.text(st7789.font_vga_8x16, "CPU Use: " + parts[0] + "%", 20, 30, st7789.WHITE)
            display.text(st7789.font_vga_8x16, "CPU Temp: " + parts[1] + " C", 20, 75, st7789.WHITE)
            display.text(st7789.font_vga_8x16, "GPU Use: " + parts[2] + "%", 20, 120, st7789.WHITE)
            display.text(st7789.font_vga_8x16, "GPU Temp: " + parts[3] + " C", 20, 165, st7789.WHITE)
            display.text(st7789.font_vga_8x16, "RAM Use: " + parts[4] + "%", 20, 210, st7789.WHITE)
            
    time.sleep(0.1)