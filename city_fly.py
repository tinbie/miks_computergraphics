import random
import numpy
import pyglet
from time import sleep

window = pyglet.window.Window(width=400,height=400,resizable=False,caption='Beispiel zu Transformationen')

def create_objects():
    pyglet.gl.glBegin(pyglet.gl.GL_QUADS)
    pyglet.gl.glVertex2f(100,100)
    pyglet.gl.glVertex2f(150,100)
    pyglet.gl.glVertex2f(150,150)
    pyglet.gl.glVertex2f(100,150)
    pyglet.gl.glVertex2f(200,200)
    pyglet.gl.glVertex2f(250,200)
    pyglet.gl.glVertex2f(250,250)
    pyglet.gl.glVertex2f(200,250)
    pyglet.gl.glEnd()

def move_up():
    global pos<
    pass

def movealong(delta):
    global new_pos
    new_pos = new_pos + delta/5

@window.event
def on_draw():
    pyglet.gl.glClearColor(*background_color)
    window.clear()
    pyglet.gl.glColor3f(*drawing_color1)
    
    pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
    pyglet.gl.glLoadIdentity()
    # set my new position
    pyglet.gl.glTranslatef( 0.0, -new_pos*10, 0.0)
    create_objects()

        
if __name__ == "__main__":  
    new_pos = 1.0

    background_color = (0, 0, 0, 1)
    drawing_color1 = (1, 1, 1)

    pyglet.clock.schedule(movealong)
    pyglet.app.run()
