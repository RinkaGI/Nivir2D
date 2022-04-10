import pygame, sys

class Sprite:
    def __init__(
        self,
        image: str,
        x = 0,
        y = 0 
    ) -> None:
        self.image = image
        self.x = x
        self.y = y

        self.sprite = pygame.image.load(self.image)
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.width = self.getWidth()
        self.height = self.getHeight()

    def getWidth(self):
        return self.sprite.get_width()
    
    def getHeight(self):
        return self.sprite.get_height()

    def getRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def collide(self, otherObject):
        if type(otherObject) != list:
            return self.rect.colliderect(otherObject)
        elif type(otherObject) == list:
            return self.rect.collidelistall(otherObject)
        else:
            print('Nivir: that is not a game object!')