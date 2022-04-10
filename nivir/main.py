import pygame, sys
from nivir.input import Input

class Nivir:
    def __init__(
        self,
        title: str = "Nivir!",
        width: int = 800,
        height: int = 600,
        bgcolor = 'black'
    ) -> None:
        pygame.init()

        self.title = title
        self.width = width
        self.height = height
        self.bgcolor = bgcolor

        self.running = True

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.input = Input()

        self.window.fill(self.bgcolor)

    def showObject(self, gameobject):
        self.window.blit(gameobject.gameobject, (gameobject.x, gameobject.y))
    
    def showSprite(self, sprite):
        self.window.blit(sprite.sprite, (sprite.x, sprite.y))

    def showText(self, text):
        self.window.blit(text.label, (text.x, text.y))
        
    def keep(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit(0)

        self.input.update()        

    def updateScreen(self, fps: int = 60):
        pygame.display.update()
        self.clock.tick(fps)
