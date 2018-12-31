import pygame

class Player2(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition, image):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.image = pygame.image.load(image)
        self.playerWidth = 23
        self.playerHeight = 37
        self.walkingLeft = False
        self.walkingRight = False
        self.velocity = 10


def UpdatePlayer2(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and self.xPosition > self.velocity:
        self.xPosition -= self.velocity
        self.walkingLeft = True
        self.walkingRight = False
    if keys[pygame.K_d] and self.xPosition < 900 - self.playerWidth - self.velocity:
        self.xPosition += self.velocity
        self.walkingLeft = False
        self.walkingRight = True
