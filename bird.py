from config import *


class Bird:

    def __init__(self, position=SCREEN_HEIGHT * 0.4, direction=DOWN):
        self.position = position
        self.direction = direction

    def bird_down(self):
        # moves bird down when nothing is pressed
        self.position += GRAVITY

    def bird_up(self):
        # moves bird up when key is pressed
        self.position -= JUMP_HEIGHT

    def hit_ground_or_sky(self):
        if self.position >= SCREEN_HEIGHT or self.position <= 0:
            return True

    def reset_params(self):
        self.position = SCREEN_HEIGHT * 0.4
        self.direction = DOWN