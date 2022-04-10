import pygame

class GameObject:
    def __init__(
        self,
        x = 0,
        y = 0,
        width: int = 100,
        height: int = 100,
        color = 'white'
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.gameobject = pygame.Surface((self.width, self.height))
        self.gameobject.fill(self.color)

    def collide(self, otherObject):
        if type(otherObject) != list:
            return self.rect.colliderect(otherObject)
        elif type(otherObject) == list:
            return self.rect.collidelistall(otherObject)
        else:
            print('Nivir: that is not a game object!')