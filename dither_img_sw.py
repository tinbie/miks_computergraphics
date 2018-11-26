import pyglet
import numpy
import sys

def load_img_into_array(path):
    global img_height
    global img_width

    img = pyglet.image.load(path)
    imgdata = img.get_image_data()
    img_width = imgdata.width
    img_height = imgdata.height
    img_array = numpy.full((img_height, img_width, 3), 0)
    px_str = imgdata.get_data('RGB', img_width*3)

    i=0
    for row in range(0, img_height):
        for column in range(0, img_width):
            img_array[row][column][0] = ord(px_str[i])
            img_array[row][column][1] = ord(px_str[i+1])
            img_array[row][column][2] = ord(px_str[i+2])
            i=i+3
    return img_array

def convert_rgb_sw(img_array):
    new_image_array = numpy.full((img_height, img_width), 0)
    for row in range(0, img_height):
        for column in range(0, img_width):
             new_image_array[row][column] = (img_array[row][column][0]+img_array[row][column][1]+img_array[row][column][2])//3
    return new_image_array

def dither_img(img_array, dither_array):
    new_image_array = numpy.full((img_height, img_width), 0)
    for row in range(0, img_height, 3):
        for column in range(0, img_width, 3):
            for dither_row in range (0, 3):
                for dither_column in range (0, 3):
                    if (img_array[row][column]//25)-1 > dither_array[dither_row][dither_column]:
                        new_image_array[row][column]=255
    return new_image_array
    
#####################################START

if __name__ == '__main__':
    img_path = sys.argv[1]
    img_array = load_img_into_array(img_path)
    dither_array = numpy.array([[0,7,3],[6,5,2],[4,1,8]])

    ord_array = convert_rgb_sw(img_array)
    dithered_img_array = dither_img(ord_array, dither_array)

    dithered_img_array.shape = -1
    img_data = (pyglet.gl.GLubyte * dithered_img_array.size)(*dithered_img_array.astype('uint8'))
    rendered_img = pyglet.image.ImageData(img_width,img_height,"I",img_data,pitch=img_width)
    myspr = pyglet.sprite.Sprite(rendered_img)

    window = pyglet.window.Window(width=400,height=400,resizable=True,caption='Beispiel zum Anzeigen von Images')
    
    @window.event
    def on_draw():
       window.clear()
       #myspr.update(x=0, y=0, rotation=None, scale=0.25, scale_x=None, scale_y=None)
       myspr.draw()
    
    pyglet.app.run()
