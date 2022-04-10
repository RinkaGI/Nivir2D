import pygame, sys

class Text:
    def __init__(
        self,
        text: str,
        font: str = "Arial",
        fontSize = 30,
        color = 'white',
        x = 0,
        y = 0
    ) -> None:
        self.text = text
        self.file = font
        self.fontSize = fontSize
        self.color = color
        self.x = x
        self.y = y

        if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'win32':
            self.font = pygame.font.SysFont(self.file, self.fontSize)

        self.label = self.font.render(self.text, True, self.color)