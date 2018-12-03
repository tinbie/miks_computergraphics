import random
import numpy
import pyglet
from time import sleep

window = pyglet.window.Window(width=400,height=400,resizable=True,caption='Beispiel zu Transformationen')

def create_random_boxes(max_x, max_y, number):
    px_1 = random.randint(0, max_x)
    py_1 = random.randint(0, max_y)

def create_box(array_box):
    pyglet.gl.glBegin(pyglet.gl.GL_QUADS)
    pyglet.gl.glVertex2f(array_box[0][0],array_box[0][1])
    pyglet.gl.glVertex2f(array_box[1][0],array_box[1][1])
    pyglet.gl.glVertex2f(array_box[2][0],array_box[2][1])
    pyglet.gl.glVertex2f(array_box[3][0],array_box[3][1])
    pyglet.gl.glEnd()

def move_forward(box):
    fw = numpy.array([[0, -100*new_pos],[0, -100*new_pos],[0, -100*new_pos],[0, -100*new_pos]])
    new_object = fw + box
    return new_object

def movealong(delta):
    global new_pos
    new_pos = new_pos + delta/5
    #if(new_pos % 1 == 0):
    #    sleep(2)

@window.event
def on_draw():
    # set bg-color
    pyglet.gl.glClearColor(*background_color)
    window.clear()
    pyglet.gl.glColor3f(*drawing_color1)

    create_box(move_forward(box_one))
    create_box(move_forward(box_two))
    create_box(move_forward(box_three))
        
if __name__ == "__main__":  
    new_pos = 1.0
    # definition boxes
    box_one = numpy.array([[100, 100], [150, 100], [150, 150], [100, 150]])
    box_two = numpy.array([[200, 200], [250, 200], [250, 250], [200, 250]])
    box_three = numpy.array([[150, 500], [250, 500], [250, 600], [150, 600]])

    background_color = (0, 0, 0, 1)
    drawing_color1 = (1, 1, 1)

    pyglet.clock.schedule(movealong)
    pyglet.app.run()    
