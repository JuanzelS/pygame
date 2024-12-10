from gameobject import GameObject
from random import choice, randint
from constants import LANES_X, SCREEN_HEIGHT, APPLE_IMG

class Apple(GameObject):
    def __init__(self):
        x = choice(LANES_X)
        super(Apple, self).__init__(x, 0, APPLE_IMG)
        self.dy = (randint(0, 200) / 100) + 1
        self.direction = choice(["down", "up"])

    def move(self):
        super().move()  # Call move() in the superclass
        if self.rect.y > SCREEN_HEIGHT or self.rect.y < -64:
            self.reset()

    def reset(self):
        self.rect.x = choice(LANES_X)
        self.rect.y = -64 if self.direction == "down" else SCREEN_HEIGHT + 64
        self.direction = choice(["down", "up"])
