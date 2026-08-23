import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.running = True

        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("Pinella")
        self.load_resources()

    def load_resources(self):
        background_sur = pygame.image.load("res/table.png")
        self.res = {
            "background": background_sur
        }

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.screen.blit(self.res["background"], pygame.Rect(0,0,1080,720))
        pygame.display.flip()

    def close_game(self):
        pygame.quit()

    def loop(self):
        while self.running:
            self.event_handler()
            self.render()

        self.close_game()

g = Game()
g.loop()