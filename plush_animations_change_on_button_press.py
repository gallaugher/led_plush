# Code for "Shroomie" the Magic Mushroom Plush
# or any other plush you want to use
# This code was written to work with an Adafruit Feather RP2040
# but can be easily modified with any other board
# For full build details see: https://github.com/gallaugher/plush
# Step-by-step YouTube build guide & parts list at the link above.

import board, time, neopixel, digitalio
from adafruit_debouncer import Debouncer
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.sequence import AnimateOnce
from adafruit_led_animation.sequence import AnimationSequence

from adafruit_led_animation.color import (
    AMBER, #(255, 100, 0)
    AQUA, # (50, 255, 255)
    BLACK, #OFF (0, 0, 0)
    BLUE, # (0, 0, 255)
    CYAN, # (0, 255, 255)
    GOLD, # (255, 222, 30)
    GREEN, # (0, 255, 0)
    JADE, # (0, 255, 40)
    MAGENTA, #(255, 0, 20)
    OLD_LACE, # (253, 245, 230)
    ORANGE, # (255, 40, 0)
    PINK, # (242, 90, 255)
    PURPLE, # (180, 0, 255)
    RED, # (255, 0, 0)
    TEAL, # (0, 255, 120)
    WHITE, # (255, 255, 255)
    YELLOW, # (255, 150, 0)
    RAINBOW # a list of colors to cycle through
    # RAINBOW is RED, ORANGE, YELLOW, GREEN, BLUE, and PURPLE ((255, 0, 0), (255, 40, 0), (255, 150, 0), (0, 255, 0), (0, 0, 255), (180, 0, 255))
)

INDIGO = (63, 0, 255)
VIOLET = (127, 0, 255)

# Set up button
button_input = digitalio.DigitalInOut(board.D11)
button_input.switch_to_input(pull=digitalio.Pull.UP)
button = Debouncer(button_input)

strip_pin = board.D6
strip_num_of_lights = 20
strip = neopixel.NeoPixel(strip_pin, strip_num_of_lights, brightness=0.5, auto_write=False)

chase_strip = Chase(strip, speed=0.1, color=WHITE, size=1, spacing=1)
comet_strip = Comet(strip, speed=0.05, color=RED, tail_length=int(strip_num_of_lights/4), bounce=True)
pulse_strip = Pulse(strip, speed=0.05, color=WHITE, period=2)
sparkle_strip = Sparkle(strip, speed=0.05, color=AMBER)
sparkle_pulse_strip = SparklePulse(strip, speed=0.05, period=5, color=WHITE)
rainbow_strip = Rainbow(strip, speed=0.05, period=2)
rainbow_chase_strip = RainbowChase(strip, speed=0.01, size=5, spacing=0, step=20)

# 9 animations:
# 0 = all
# 1 through 7 = chase_strip through rainbow_chase_strip as defined above
# 8 = animations stop

TOTAL_ANIMATIONS = 7
animation = 0

animations_strip = AnimationSequence(
    chase_strip, comet_strip, pulse_strip, sparkle_pulse_strip, rainbow_strip, rainbow_chase_strip, advance_interval=5, auto_clear=True
)

def run_animations():
    if animation == 0:
        print("Animations {}".format(animation))
        print("chase_strip")
        #chase_strip = Chase(strip, speed=0.1, color=WHITE, size=1, spacing=1)
        chase_strip = Chase(strip, speed=0.1, color=WHITE, size=1, spacing=1)
        animations = AnimateOnce(chase_strip)
        while animations.animate():
            check_button()
    elif animation == 1:
        print("Animations {}".format(animation))
        animations = AnimateOnce(comet_strip)
        while animations.animate():
            check_button()
    elif animation == 2:
        print("Animations {}".format(animation))
        print("pulse_strip")
        animations = AnimateOnce(pulse_strip)
        while animations.animate():
            check_button()
    elif animation == 3:
        print("Animations {}".format(animation))
        print("sparkle_pulse_strip")
        animations = AnimateOnce(sparkle_pulse_strip)
        while animations.animate():
            check_button()
    elif animation == 4:
        print("Animations {}".format(animation))
        print("rainbow_strip")
        animations = AnimateOnce(rainbow_strip)
        while animations.animate():
            check_button()
    elif animation == 5:
        print("Animations {}".format(animation))
        print("rainbow_chase_strip")
        animations = AnimateOnce(rainbow_chase_strip)
        while animations.animate():
            check_button()
    elif animation == 6:
        print("Animations {}".format(animation))
        #animations = AnimateOnce(chase_strip, comet_strip, pulse_strip, sparkle_pulse_strip, rainbow_strip, rainbow_chase_strip)
        while animations_strip.animate():
            check_button()

def check_button():
    global animation
    button.update() # checks a debounced button
    if button.fell: # if button is pressed
        animation += 1
        if animation >= TOTAL_ANIMATIONS:
            animation = 0
        print("BUTTON PRESSED! animation = {}".format(animation))

while True:
    run_animations()
