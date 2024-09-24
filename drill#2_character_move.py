from pico2d import *
import math

open_canvas()



grass = load_image('grass.png')
char = load_image('character.png')



def run_top():
    print("top")
    pass

def run_right():
    print("right")
    pass

def run_bottom():
    print("bottom")
    pass

def run_left():
    print("left")
    pass


def run_rectangle():
    print("ractangle")

    run_top()
    run_right()
    run_bottom()
    run_left()

    
    pass






def run_circle():
    print("circle")

    r, cx, cy = 300, 800 // 2, 600 // 2
    
    for degree in range(0, 360, 3):

        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        clear_canvas_now()
        char.draw_now(x, y)
        delay(0.1)

    pass
    



while True:
    run_rectangle()
    # run_circle()

    break



close_canvas()
