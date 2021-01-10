import pygame
from pygame.locals import *
from config import *
import bird
import pipe


class Game:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._game_over = False
        self.score = 0

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self._display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE)
        self._running = True

        # set icon
        icon = pygame.image.load(BIRD_IMG)
        pygame.display.set_icon(icon)

        # bird object
        self.bird = bird.Bird()

        # images
        self.bird_image = pygame.image.load(BIRD_IMG)
        self.buildings_image = pygame.image.load(BG_CITY_IMG)
        self.sun_image = pygame.image.load(SUN_IMG)

        # clock
        self.clock = pygame.time.Clock()

        # pipe object
        self.pipe = pipe.Pipe()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.bird.direction = UP

            if event.key == K_RETURN and self._game_over is True:
                self.new_game()

    def collision(self):
        # bird in pipe x range
        if BIRD_POSITION_X <= self.pipe.x <= BIRD_POSITION_X + PIPE_WIDTH:
            if self.bird.position <= self.pipe.top_pipe_height or self.bird.position >= SCREEN_HEIGHT - self.pipe.bottom_pipe_height:
                self.game_over()

    def on_loop(self):
        self.clock.tick(30)  # set FPS

        # bird movement
        if self.bird.direction == DOWN:
            self.bird.bird_down()
        else:
            self.bird.bird_up()
        self.bird.direction = DOWN

        self.collision()

        # pipe movement
        self.pipe.move_pipe()
        if self.pipe.pipe_reached_end_of_screen():
            self.score += 1
            self.pipe.reset_pipe()
            self.pipe.change_pipe_dimensions()

        if self.bird.hit_ground_or_sky():
            self.game_over()

    def on_render(self):
        # draw sky
        self._display_surf.fill(BLUE_SKY)
        # draw grass
        pygame.draw.rect(self._display_surf, GREEN_GRASS,
                         [0, SCREEN_HEIGHT*0.8, SCREEN_WIDTH, SCREEN_HEIGHT*0.2])
        # draw sun
        self._display_surf.blit(self.sun_image, (30, 30))
        # draw buildings
        self._display_surf.blit(self.buildings_image, (0, SCREEN_HEIGHT*0.6))
        self._display_surf.blit(self.buildings_image, (SCREEN_WIDTH*0.25, SCREEN_HEIGHT*0.6))
        self._display_surf.blit(self.buildings_image, (SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.6))



        if not self._game_over:
            # draw bird
            self._display_surf.blit(self.bird_image, (BIRD_POSITION_X, self.bird.position))

            # draw bottom pipe
            pygame.draw.rect(self._display_surf, GREEN_PIPE,
                             [self.pipe.x - PIPE_WIDTH, SCREEN_HEIGHT - self.pipe.bottom_pipe_height, PIPE_WIDTH,
                              self.pipe.bottom_pipe_height])

            # draw top pipe
            pygame.draw.rect(self._display_surf, GREEN_PIPE,
                             [self.pipe.x - PIPE_WIDTH, 0, PIPE_WIDTH, self.pipe.top_pipe_height])

            # draw score
            self.draw_text("Score: " + str(self.score), "freesansbold.ttf", 32, SCREEN_WIDTH * 0.85,
                           SCREEN_HEIGHT * 0.05,
                           RED_SCORE, BLUE_SKY)



        # if game over
        else:
            self.draw_text("Score: " + str(self.score), "freesansbold.ttf", 64, SCREEN_WIDTH * 0.5,
                           SCREEN_HEIGHT * 0.45,
                           RED_SCORE, BLUE_SKY)
            self.draw_text("GAME OVER", "freesansbold.ttf", 72, SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.3,
                           RED_SCORE, BLUE_SKY)
            self.draw_text("Press ENTER to play again", "freesansbold.ttf", 40, SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.6,
                           RED_SCORE, BLUE_SKY)

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def new_game(self):
        # resetting stuff to play again
        self.pipe.reset_params()
        self.bird.reset_params()
        self.score = 0
        self._game_over = False

    def game_over(self):
        self.pipe.stop_pipe_movement()
        self._game_over = True

    def draw_text(self, text, font, size, x, y, fg_color, bg_color):
        font = pygame.font.Font(font, size)
        text_to_write = font.render(text, True, fg_color, bg_color)
        textRect = text_to_write.get_rect()
        textRect.center = (x, y)
        self._display_surf.blit(text_to_write, textRect)


if __name__ == "__main__":
    game = Game()
    game.on_execute()
