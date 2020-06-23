import pygame

class HitBox:
    def __init__(self, upperLeft, width, height):
        # x, y
        self.upperLeft = upperLeft
        self.width = width
        self.height = height

    def hasCollidedCheck(self, otherHitbox, baseX, baseY):

        left1 = self.upperLeft[0] + baseX
        right1 = left1 + self.width
        top1 = self.upperLeft[1] + baseY
        bottom1 = top1 + self.height


        left2 = otherHitbox.upperLeft[0]
        right2 = left2 + otherHitbox.width
        top2 = otherHitbox.upperLeft[1]
        bottom2 = top2 + otherHitbox.height


        if((left1 <= left2 and left2 < right1) or (left1 <= right2 and right2 < right1)) and ((top1 <= top2 and top2 <= bottom1) or (top1 <= bottom2 and bottom2 <= bottom1)):
            return True

        return False