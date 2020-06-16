import pygame

class HitBox:
    def __init__(self, upperLeft, lowerRight, centerLoc):
        # x, y
        self.upperLeft = upperLeft
        self.lowerRight = lowerRight
        self.centerLoc = centerLoc

    def getWidth(self):
        pass

    def getHeight(self):
        pass

    def hasCollidedCheck(self, otherHitbox):
        pass