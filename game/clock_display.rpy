screen blinking_digital_clock():
    zorder 1000
    
    add Solid("#000000")
    
    text "02:00":
        font "Digiface Regular.ttf"
        size 300
        color "#00ff00"
        outlines [ (8, "#003300", 0, 0) ]
        xalign 0.5
        yalign 0.5
        at electronic_blink

transform electronic_blink:
    alpha 1.0
    0.9
    alpha 0.4
    0.2
    alpha 0.8 
    0.3
    alpha 1.0
    0.6
    repeat

label show_clock_for(duration=3.0):

    show screen blinking_digital_clock
    pause duration
    hide screen blinking_digital_clock
    return