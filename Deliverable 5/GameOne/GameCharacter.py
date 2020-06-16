import pygame
from GameObject import GameObject

class GameCharacter(GameObject):
    def __init__(self, sprs, dialogSprs, battleSprs, noises, dialogNoises, attacks, ownHitbox, name):
        super().__init__(sprs, noises, ownHitbox, name)\

        self.dialogSprites = dialogSprs
        self.battleSprites = battleSprs
        self.dialogNoises = dialogNoises
        self.attacks = attacks

    def interact(self, controller):
        print("SHOULDNTBEHERE Character Interact")
        pass

    def battle(self, controller):
        print("SHOULDNTBEHERE Character Battle")
        pass
