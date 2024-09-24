from pico2d import *
import math

open_canvas()



grass = load_image('grass.png')
char = load_image('character.png')


def draw_char(x, y):
        clear_canvas_now()
        char.draw_now(x, y)
        delay(0.01)
        pass

    
def run_top():
    print("top")
    for x in range(0, 800, 10):
        draw_char(800 - x, 550)
    pass

def run_right():
    print("right")
    for y in range(0, 600, 10):
        draw_char(790, y)
    pass

def run_bottom(a):
    print("bottom")
    for x in range(a, 800, 10):
        draw_char(x, 50)
    pass

def run_left():
    print("left")
    for y in range(0, 600, 10):
        draw_char(10, 600 - y)
    pass




def run_diagonal():
    print("dig")

    for i in range(0, 600, 2):
        x = 800 - i
        y = 600 - i

        draw_char(x, y)
    pass





def run_rectangle():
    print("ractangle")

    #run_right()
    #run_top()
    #run_left()
    run_bottom(0)
   
    pass




def run_circle():
    print("circle")

    r, cx, cy = 300, 800 // 2, 600 // 2
    
    for degree in range(0, 360, 3):

        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        
        draw_char(x, y)
        pass


def run_triangle():
    print("tri")

#    run_right()
#    run_diagonal()
    run_bottom(200)

    
    pass





while True:
    run_rectangle()
#    run_circle()
    run_triangle()


    break



close_canvas()
