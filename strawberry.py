from gameobject import GameObject
from random import choice, randint
from constants import LANES_Y, SCREEN_WIDTH, STRAWBERRY_IMG

class Strawberry(GameObject):
    def __init__(self):
        y = choice(LANES_Y)
        super(Strawberry, self).__init__(0, y, STRAWBERRY_IMG)
        self.dx = (randint(0, 200) / 100) + 1
        self.direction = choice(["right", "left"])

    def move(self):
        super().move()  # Call move() in the superclass
        if self.rect.x > SCREEN_WIDTH or self.rect.x < -64:
            self.reset()

    def reset(self):
        self.rect.x = -64 if self.direction == "right" else SCREEN_WIDTH + 64
        self.rect.y = choice(LANES_Y)
        self.direction = choice(["right", "left"])
