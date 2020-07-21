from GameObject import GameObject
import pygame
from HitBox import HitBox


class SecondCharac(GameObject):
    def __init__(self):
        sprs = [pygame.transform.scale(pygame.image.load('Images\\blueSquare.png'), (50,75))]

        noises = 0
        ownHitbox = HitBox([0,0], 50, 75)
        name = "testOtherChar"

        facing = "D"

        super().__init__(sprs, noises, ownHitbox, name, facing)

    def drawSelf(self, x, y, controller):
        controller.screen.blit(self.ownSprites[0], (x,y))

    def interact(self, controller):
        img = pygame.image.load('Images\\smile.jpg')
        textContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras blandit, neque nec semper faucibus, odio nisl convallis leo, non porttitor ipsum lorem non lorem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut non pellentesque est, ut convallis ligula. Sed aliquet, erat vel maximus dignissim"
        controller.displayTextBox(textContent, img)

