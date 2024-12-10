from gameobject import GameObject
from constants import LANES_X, LANES_Y, PLAYER_IMG

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(LANES_X[1], LANES_Y[1], PLAYER_IMG)
        self.dx = self.rect.x
        self.dy = self.rect.y
        self.pos_x = 1
        self.pos_y = 1

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(LANES_X) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(LANES_Y) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.rect.x += (self.dx - self.rect.x) * 0.25
        self.rect.y += (self.dy - self.rect.y) * 0.25

    def update_dx_dy(self):
        self.dx = LANES_X[self.pos_x]
        self.dy = LANES_Y[self.pos_y]
