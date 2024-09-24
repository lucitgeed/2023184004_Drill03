from pico2d import *
import math

open_canvas()



grass = load_image('grass.png')
char = load_image('character.png')


def run_rectangle():
    print("ractangle")
    pass






def run_circle():
    print("circle")

    r = 300
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    

    clear_canvas_now()
    char.draw_now(x, y)
    delay(0.1)

    

    
    pass
    



while True:
    run_rectangle()
    run_circle()

    break



close_canvas()
