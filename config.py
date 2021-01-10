from random import randint

# screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# bird dimensions
BIRD_RADIUS = SCREEN_HEIGHT // 35
BIRD_POSITION_X = SCREEN_WIDTH * 0.3

# pipe dimensions
PIPE_GAP = SCREEN_HEIGHT * 0.3
PIPE_WIDTH = SCREEN_WIDTH * 0.15
BOTTOM_PIPE_HEIGHT = SCREEN_HEIGHT * randint(1, 6) / 10
TOP_PIPE_HEIGHT = SCREEN_HEIGHT - BOTTOM_PIPE_HEIGHT - PIPE_GAP

# physics
GRAVITY = 9
JUMP_HEIGHT = 100
PIPE_SPEED = 10


# colors
BLUE_SKY = (51, 153, 255)
YELLOW_BIRD = (255, 255, 51)
GREEN_PIPE = (0, 153, 0)
GREEN_GRASS = (176, 255, 17)
RED_SCORE = (255, 0, 0)

# bird direction
UP = 0
DOWN = 1

# images file
BIRD_IMG = "puffer-fish.png"
BG_CITY_IMG = "buildings.png"
SUN_IMG = "sun.png"