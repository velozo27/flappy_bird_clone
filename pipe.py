from config import *


class Pipe:

    def __init__(self, x=SCREEN_WIDTH, on_screen=True, top_pipe_height=TOP_PIPE_HEIGHT,
                 bottom_pipe_height=BOTTOM_PIPE_HEIGHT):
        self.x = x
        self.on_screen = on_screen
        self.top_pipe_height = top_pipe_height
        self.bottom_pipe_height = bottom_pipe_height
        self.pipe_speed = 10

    def move_pipe(self):
        self.x -= self.pipe_speed

    def pipe_reached_end_of_screen(self):
        if self.x == 0:
            return True

    def reset_pipe(self):
        self.x = SCREEN_WIDTH  # pipe back to the left of the screen
        self.on_screen = False

    def change_pipe_dimensions(self):
        self.bottom_pipe_height = SCREEN_HEIGHT * randint(1, 6) / 10
        self.top_pipe_height = SCREEN_HEIGHT - self.bottom_pipe_height - PIPE_GAP

    def stop_pipe_movement(self):
        self.pipe_speed = 0

    def reset_params(self):
        self.pipe_speed = 10
        self.x = SCREEN_WIDTH
