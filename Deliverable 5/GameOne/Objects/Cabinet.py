from GameObject import GameObject
import pygame
from HitBox import HitBox


class Cabinent(GameObject):
    def __init__(self):
        sprs = [pygame.transform.scale(pygame.image.load('Images\\cabinent.png'), (50,75))]

        noises = 0
        ownHitbox = HitBox([0,0], 50, 75)
        name = "cabinet"

        facing = "D"

        super().__init__(sprs, noises, ownHitbox, name, facing)

    def drawSelf(self, x, y, controller):
        controller.screen.blit(self.ownSprites[0], (x,y))

    def interact(self, controller):
        textContent = "The file cabinet is empty"
        controller.displayTextBox(textContent)

