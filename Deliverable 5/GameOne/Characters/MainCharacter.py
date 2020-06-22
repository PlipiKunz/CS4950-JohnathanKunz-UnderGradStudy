from GameObject import GameObject
import pygame


class MainCharacter(GameObject):
    def __init__(self):
        sprs = [pygame.transform.scale(pygame.image.load('Images\\blueSquare.png'), (100,100))]

        noises = 0
        ownHitbox = 0;
        name = "main Character"

        super().__init__(sprs, noises, ownHitbox, name)

    def drawSelf(self, x, y, controller):
        controller.screen.blit(self.ownSprites[0], (x,y))

    def interact(self, controller):
        print("How does it make sense to interact with the main character?")