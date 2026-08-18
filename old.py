import pygame

class Game:
    def __init__(self, width=1080, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
    
    def input_handeler(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def run(self):
        while True:
            self.input_handeler()
            self.update()
            self.render()


Game().run()