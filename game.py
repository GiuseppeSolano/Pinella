import pygame
from pygame.locals import *
import random
from engine import Engine

#https://kerenel.itch.io/pixelart-cards

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.engine = Engine("pinella")

        self.scr_w = 1080
        self.scr_h = 720
        
        self.screen = pygame.display.set_mode((self.scr_w,self.scr_h))
        self.player = 0

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pinella")
        self.load_resources()
        self.load_rects()

    def load_rects(self):
        card_w = 116
        card_h = 160
        self.rects = {
            "deck": pygame.Rect(10, self.scr_h//2-card_h//2 ,card_w,card_h),
            "player_hand": pygame.Rect(10, self.scr_h - card_h, self.scr_w - 20, self.scr_h)
        }

    def load_resources(self):

        background_sur = pygame.image.load("res/table.png")
        template = pygame.image.load("res/cards.png")

        card_w = 56
        card_h = 80

        self.res = {
            "background": background_sur,
            "back_red": template.subsurface(pygame.Rect(0,card_h*2,card_w,card_h)),
            "back_blue": template.subsurface(pygame.Rect(0,card_h*3,card_w,card_h))
        }

        for i in range(1,14):
            for j,n in ((0,"hearts"),(1,"spades"),(2,"diamonds"),(3,"clubs")):
                self.res[(i,n)] = template.subsurface(pygame.Rect(i*card_w,card_h*j,card_w,card_h))


    def event_handler(self):
        self.mx, self.my = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == QUIT:
                self.running = False

    def draw_card(self, info, x,y,w,h):
        if info not in self.res:
            tmp = pygame.transform.scale(self.res["empty_card"],(w,h))
            self.screen.blit(tmp, pygame.Rect(x,y, w,h))
            return
        
        tmp = pygame.transform.scale(self.res[info],(w,h))
        self.screen.blit(tmp, pygame.Rect(x,y, w,h))

    def draw_deck(self, color_deck, rect):
        if color_deck=="":
            return
        info = "back_" + color_deck
        tmp = pygame.transform.scale(self.res[info],(rect.w,rect.h))
        self.screen.blit(tmp, rect)


    def draw_hand(self, list_cards):
        num_cards = len(list_cards)
        if num_cards==0:
            return
        d
        initial_space = 10
        pass


    def render(self):
        self.screen.blit(self.res["background"], pygame.Rect(0,0,1080,720))

        deck_info = self.engine.get_deck()
        self.draw_deck(deck_info["back"],self.rects["deck"])

        pygame.display.flip()
        """
        self.draw_card((6,"hearts"),100,200,112,160)
        self.draw_deck(self.engine.deck.get_back(),0,0,112,160)
        pygame.display.flip()
        """

    def update(self):
        return

    def close_game(self):
        pygame.quit()
    

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()

            self.clock.tick(30)

        self.close_game()

g = Game()
g.run()
