from GameObject import GameObject
import pygame
from HitBox import HitBox
from battleObject import battleObject


class Cabinent(GameObject):
    def __init__(self):
        sprs = [pygame.transform.scale(pygame.image.load('Images\\cabinent.png'), (50,75))]

        noises = 0
        ownHitbox = HitBox([0,0], 50, 75)
        name = "cabinet"

        facing = "D"
        super().__init__(sprs, noises, ownHitbox, name, facing)
        self.fought = 0

    def drawSelf(self, x, y, controller):
        controller.screen.blit(self.ownSprites[0], (x,y))

    def interact(self, controller):
        print(self.fought)
        if(self.fought==0):
            textContent = "The file cabinet attacks!!"
            controller.displayTextBox(textContent)


            bo = battleObject(self.ownSprites, [], 10, [""])
            controller.changeToBattleRoom(bo,"A File Cabinent Approaches", 0)
            self.fought += 1
        else:
            controller.displayTextBox("You have already defeated this enemy ")

