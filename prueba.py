#################### TESTING NIVIR MAKING A ENDLESS RUNNER 2D #################################

from nivir import *

screen =  Nivir('Runner', 800, 400)

sky = Sprite('graphics/Sky.png', 0, 0)
ground = Sprite('graphics/ground.png', 0, 300)
snail = Sprite('graphics/snail/snail1.png', 600, 250)
text = Text('My game', None, 50, 'Green', 300, 50)

while screen.running:
    screen.keep()

    screen.showSprite(sky)
    screen.showSprite(ground)
    screen.showSprite(snail)
    screen.showText(text)

    snail.x -= 4

    if snail.x < -100: snail.x = 800

    screen.updateScreen(60)
