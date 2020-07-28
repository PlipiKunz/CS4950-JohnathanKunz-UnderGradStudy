import pygame
from GameObject import GameObject

class GameCharacter(GameObject):
    def __init__(self, sprs, dialogSprs, battleSprs, noises, dialogNoises, ownHitbox, name, battleObject):
        super().__init__(sprs, noises, ownHitbox, name)

        self.dialogSprites = dialogSprs
        self.battleSprites = battleSprs
        self.dialogNoises = dialogNoises
        self.battleObject = battleObject

