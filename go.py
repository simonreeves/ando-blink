import blinkstick.blinkstick as bs


strip = bs.find_first()

led_count = 32

for i in range(0, led_count):
    
    # normalised
    # index_norm = i/32
    # strip.set_color(0, i, red=255*index_norm, blue=255*index_norm, green=255-(255*index_norm))

    strip.set_color(0, i, red=255, blue=100, green=255)

