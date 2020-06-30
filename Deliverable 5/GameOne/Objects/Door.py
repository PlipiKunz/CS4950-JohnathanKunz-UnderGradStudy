import pygame
import GameObject
from HitBox import HitBox


class Door(GameObject.GameObject):
    def __init__(self):
        sprs = [pygame.transform.scale(pygame.image.load('Images\\door.png'), (75,100))]

        noises = 0
        ownHitbox = HitBox([0,0], 75, 100)
        name = "door"

        facing = "D"

        super().__init__(sprs, noises, ownHitbox, name, facing)

    def drawSelf(self, x, y, controller):
        controller.screen.blit(self.ownSprites[0], (x, y))