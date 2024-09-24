from pico2d import *


open_canvas()



grass = load_image('grass.png')
char = load_image('character.png')


def run_rectangle():
    print("ractangle")
    pass






def run_circle():
    print("circle")

    r = 300
    x = r * cos(theta)
    y = r* sin(theta)
    

    clear_canvas_now()
    char.draw_now(x, y)
    delay(0.1)

    

    
    pass
    



while True:
    run_rectangle()
    run_circle()

    break



close_canvas()
