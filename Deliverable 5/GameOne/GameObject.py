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
        print("SHOULDNTBEHERE interact gameObject" + self.name)
        pass

    def getWidth(self):
        pass

    def getHeight(self):
        pass
