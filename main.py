def on_gesture_eight_g():
    basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        """)
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_forever():
    pass
basic.forever(on_forever)
