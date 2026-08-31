import pygame
import random
from engine import Engine

#https://kerenel.itch.io/pixelart-cards

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.engine = Engine("pinella")

        self.screen = pygame.display.set_mode((1080,720))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pinella")
        self.load_resources()


    def load_resources(self):
        card_w = 56
        card_h = 80
        background_sur = pygame.image.load("res/table.png")
        template = pygame.image.load("res/cards.png")

        self.res = {
            "background": background_sur,
            "back_red": template.subsurface(pygame.Rect(0,card_h*2,card_w,card_h)),
            "back_blue": template.subsurface(pygame.Rect(0,card_h*3,card_w,card_h))
        }
        for i in range(1,14):
            front = (i,"hearts")
            self.res[front] = template.subsurface(pygame.Rect(i*card_w,card_h*0,card_w,card_h))
        for i in range(1,14):
            front = (i,"spades")
            self.res[front] = template.subsurface(pygame.Rect(i*card_w,card_h*1,card_w,card_h))
        for i in range(1,14):
            front = (i,"diamonds")
            self.res[front] = template.subsurface(pygame.Rect(i*card_w,card_h*2,card_w,card_h))
        for i in range(1,14):
            front = (i,"clubs")
            self.res[front] = template.subsurface(pygame.Rect(i*card_w,card_h*3,card_w,card_h))
        for i in range(1,14):
            for j,n in {(0,"hearts"),(1,"spades"),(2,"diamonds"),(3,"diamonds")}:
                self.res[(i,n)] = template.subsurface(pygame.Rect(i*card_w,card_h*j,card_w,card_h))

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

    def draw_card(self, info, x,y,w,h):
        tmp = pygame.transform.scale(self.res[info],(w,h))
        self.screen.blit(tmp, pygame.Rect(x,y, w,h))

    def draw_deck(self, info, x,y,w,h):
        if info=="":
            return
        info = "back_" + info
        tmp = pygame.transform.scale(self.res[info],(w,h))
        self.screen.blit(tmp, pygame.Rect(x,y, w,h))

    def render(self):
        self.screen.blit(self.res["background"], pygame.Rect(0,0,1080,720))
        self.draw_card((1,"spades"),100,200,112,160)
        self.draw_deck(self.engine.deck.get_back(),0,0,112,160)
        pygame.display.flip()

    def close_game(self):
        pygame.quit()

    def run(self):
        while self.running:
            self.event_handler()
            self.render()

            self.clock.tick(30)

        self.close_game()

g = Game()
g.run()