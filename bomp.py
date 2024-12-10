from gameobject import GameObject
from random import choice, randint
from constants import LANES_X, LANES_Y, SCREEN_WIDTH, SCREEN_HEIGHT, BOMB_IMG

class Bomb(GameObject):
    def __init__(self):
        direction = choice(["down", "up", "left", "right"])
        if direction in ["down", "up"]:
            x = choice(LANES_X)
            y = 0 if direction == "down" else SCREEN_HEIGHT
        else:
            x = 0 if direction == "right" else SCREEN_WIDTH
            y = choice(LANES_Y)
        super(Bomb, self).__init__(x, y, BOMB_IMG)
        self.dx = (randint(0, 200) / 100) + 1 if direction in ["right", "left"] else 0
        self.dy = (randint(0, 200) / 100) + 1 if direction in ["down", "up"] else 0
        self.direction = direction

    def move(self):
        super().move()  # Call move() in the superclass
        if self.rect.y > SCREEN_HEIGHT or self.rect.y < -64 or self.rect.x > SCREEN_WIDTH or self.rect.x < -64:
            self.reset()

    def reset(self):
        self.direction = choice(["down", "up", "left", "right"])
        if self.direction in ["down", "up"]:
            self.rect.x = choice(LANES_X)
            self.rect.y = -64 if self.direction == "down" else SCREEN_HEIGHT + 64
        else:
            self.rect.x = -64 if self.direction == "right" else SCREEN_WIDTH + 64
            self.rect.y = choice(LANES_Y)
        self.dx = (randint(0, 200) / 100) + 1 if self.direction in ["right", "left"] else 0
        self.dy = (randint(0, 200) / 100) + 1 if self.direction in ["down", "up"] else 0
