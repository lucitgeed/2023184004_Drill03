from pico2d import *

open_canvas()

grass = load_image('grass.png')
char = load_image('character.png')


grass.draw_now(400, 30)
char.draw_now(400, 90)


while(True):

    for i in range(0, 200):
        clear_canvas_now()
        grass.draw_now(400, 30)
        char.draw_now(400 + i, 90)
        i = i + 2

    for i in range(0, 200):
        clear_canvas_now()
        grass.draw_now(400, 30)
        char.draw_now(400 + 200, 90 + i)
        i = i+2

    for i in range(0,400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        char.draw_now(400 + 200 - i, 90 + 200)
        i = i+2

    for i in range(0, 200):
        clear_canvas_now()
        grass.draw_now(400, 30)
        char.draw_now(400 + 200 - 400, 90 + 200 - i)
        i = i + 2

    for i in range(0, 200):
        clear_canvas_now()
        grass.draw_now(400, 30)
        char.draw_now(400 + 200 - 400 + i, 90)
        i = i + 2


    delay(2)



    for x in range(0, 50):
            clear_canvas_now()
            grass.draw_now(400, 30)
            char.draw_now(400 + x, 90 + x)
            x = x + 2

    for x in range(0, 50):
            clear_canvas_now()
            grass.draw_now(400, 30)
            char.draw_now(400 + 50 - x, 90 + 50 + x)
            x = x + 2


    for x in range(0, 50):
            clear_canvas_now()
            grass.draw_now(400, 30)
            char.draw_now(400 - x, 90 + 50 + 50 - x)
            x = x + 2


    for x in range(0, 50):
            clear_canvas_now()
            grass.draw_now(400, 30)
            char.draw_now(400 - 50 + x, 90 + 50 - x)
            x = x + 2

    delay(2)



close_canvas()
