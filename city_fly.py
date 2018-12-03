import random
import numpy
import pyglet

global end_prog
end_prog = False

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
    fw = numpy.array([[0, 100*new_pos],[0, 100*new_pos],[0, 100*new_pos],[0, 100*new_pos]])
    new_object = fw + box
    return new_object

def movealong(delta):
    global new_pos
    new_pos = new_pos + delta/5
    if(new_pos > 2):
        new_pos = new_pos - 2 
        end_prog = True
        

if __name__ == "__main__":  
    new_pos = 1.0
    # definition boxes
    box_one = numpy.array([[100, 100], [150, 100], [150, 150], [100, 150]])
    box_two = numpy.array([[200, 200], [250, 200], [250, 250], [200, 250]])

    background_color = (0, 0, 0, 1)
    drawing_color1 = (1, 1, 1)
    
    window = pyglet.window.Window(width=400,height=400,resizable=True,caption='Beispiel zu Transformationen')

    while end_prog == False:
        @window.event
        def on_draw():
            # set bg-color
            pyglet.gl.glClearColor(*background_color)
            window.clear()

            pyglet.gl.glColor3f(*drawing_color1)
            moved_box_1 = move_forward(box_one)
            moved_box_2 = move_forward(box_two)
            create_box(moved_box_1)
            create_box(moved_box_2)
    
        pyglet.clock.schedule(movealong)
        pyglet.app.run()
    
