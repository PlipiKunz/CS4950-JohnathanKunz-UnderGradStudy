import pygame


class GameObject:
    def __init__(self, sprs, noises, ownHitbox, name, facing):
        self.ownSprites = sprs
        self.noises = noises
        self.HitBox = ownHitbox
        self.name = name

        # facing can be U, D, L, R
        self.facing = facing

    def drawSelf(self, x, y, controller):
        print("SHOULDNTBEHERE drawSelf gameObject" + self.name)
        pass

    def interact(self, controller):
        controller.displayTextBox(self.name)
        pass

    def getWidth(self):
        return self.HitBox.width

    def getHeight(self):
        return self.HitBox.height
