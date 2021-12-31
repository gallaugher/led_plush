# Test code that simply lights up a strand of 20 LEDs
import board, neopixel

strand_pin = board.D6 # assumes you've wired LED signal pin to D6
strand_num_of_leds = 20 # assumes your strand has 20 LEDs
# 50% brightness, or 0.5 should be plenty of bright & save battery
strand = neopixel.NeoPixel(strand_pin, strand_num_of_leds, brightness = 0.5, auto_write = True)

strand.fill((255, 255, 255)) # White

while True:
    pass
