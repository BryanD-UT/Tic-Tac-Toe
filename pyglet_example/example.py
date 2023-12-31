import pyglet
from pyglet.window import mouse
from pyglet.gui import PushButton as PB
window = pyglet.window.Window()
# label = pyglet.text.Label('Hello, world',
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')

#batch = pyglet.graphics.Batch()
image = pyglet.image.load('../RESOURCES/images/grid.jpeg')
X = pyglet.image.load('../RESOURCES/images/red_x.png')
Y = pyglet.image.load('../RESOURCES/images/black_o.png')

scale_factor = 0.25

# scaled_width = int(image.width * scale_factor)
# scaled_height = int(image.height * scale_factor)
# scaled_image = image.get_transform(resize=(scaled_width, scaled_height))

scaled_width = int(X.width * scale_factor)
scaled_height = int(X.height * scale_factor)
scaled_X = X.get_transform(resize=(scaled_width, scaled_height))

scaled_Y = int(Y.width * scale_factor)
scaled_Y = int(Y.height * scale_factor)
scaled_Y = Y.get_transform(resize=(scaled_width, scaled_height))


@window.event
def on_draw():
    window.clear()
    #label.draw()
    #image.blit(0,0)
    X.blit(100,100)

@window.event
def on_mouse_press(x, y, button, modifiers):
    sound = pyglet.media.load('../RESOURCES/sounds/button.mp3', streaming = False)
    if button == mouse.LEFT:

        print('The left mouse button was pressed.')
        sound.play()

pyglet.app.run()