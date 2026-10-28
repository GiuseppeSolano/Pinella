from os import minor

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
        self.num_cards_player = 0

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pinella")
        self.load_resources()
        self.load_rects()

    def load_rects(self):
        card_w = 116
        card_h = 160
        self.rects = {
            "deck":          pygame.Rect(10, self.scr_h//2-card_h//2 ,card_w,card_h),
            "player_hand":   pygame.Rect(10, self.scr_h - card_h -10, self.scr_w - 20, card_h),
            "opponent_hand": pygame.Rect(10, 10, self.scr_w - 20, card_h)
        }

    def load_resources(self):
        background_sur = pygame.image.load("res/table.png")
        template = pygame.image.load("res/cards.png")

        card_w = 56
        card_h = 80

        self.res = {
            "background":  background_sur,
            "back_red":    template.subsurface(pygame.Rect(0,card_h*2,card_w,card_h)),
            "back_blue":   template.subsurface(pygame.Rect(0,card_h*3,card_w,card_h)),
            "empty_card":  template.subsurface(pygame.Rect(0,       0,card_w,card_h)),
        }

        for i in range(1,14):
            for j,n in ((0,"hearts"),(1,"spades"),(2,"diamonds"),(3,"clubs")):
                self.res[(i,n)] = template.subsurface(pygame.Rect(i*card_w,card_h*j,card_w,card_h))

        self.res[(0,"hearts")]   = template.subsurface(pygame.Rect(0,card_h*4,card_w,card_h))
        self.res[(0,"diamonds")] = template.subsurface(pygame.Rect(0,card_h*4,card_w,card_h))
        self.res[(0,"spades")]   = template.subsurface(pygame.Rect(0,card_h*5,card_w,card_h))
        self.res[(0,"clubs")]    = template.subsurface(pygame.Rect(0,card_h*5,card_w,card_h))

    def check_collisions(self, mouse_pos):
        move = {}
        for k,rect in self.rects.items():
            if rect.collidepoint(mouse_pos):
                if k == "deck":
                    print("deck clicked")
                    move = {
                        "type": "draw"
                    }
                elif k == "player_hand":
                    print("hand clicked")
                    self.select_card(mouse_pos)
        if len(move)==0:
            return
        self.engine.apply_move(move)

    def select_card(self, mouse_pos):
        pass

            
    def event_handler(self):
        for e in pygame.event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.dict["button"]==1:
                    self.check_collisions(e.dict["pos"])
            if e.type == QUIT:
                self.running = False

    def draw_card(self, info, is_face_up, x,y,w,h):        
        if not is_face_up:
            back_color = "back_" + info["back"]
            if back_color not in self.res:
                tmp = pygame.transform.scale(self.res["empty_card"],(w,h))
                self.screen.blit(tmp, pygame.Rect(x,y, w,h))
                return

            tmp = pygame.transform.scale(self.res[back_color],(w,h))
            self.screen.blit(tmp, pygame.Rect(x,y, w,h))
            return
            
        info = (info["rank"],info["suit"])
        
        if info not in self.res:
            tmp = pygame.transform.scale(self.res["empty_card"],(w,h))
            self.screen.blit(tmp, pygame.Rect(x,y, w,h))
            return
        
        tmp = pygame.transform.scale(self.res[info],(w,h))
        self.screen.blit(tmp, pygame.Rect(x,y, w,h))
        return

    def draw_deck(self, info, rect):
        color_deck = info["back"]
        if color_deck=="":
            return
        info = "back_" + color_deck
        tmp = pygame.transform.scale(self.res[info],(rect.w,rect.h))
        self.screen.blit(tmp, rect)


    def draw_list_cards_large(self, is_face_up, list_cards, rect):
        num_cards = len(list_cards)
        self.num_cards_player = num_cards
        if num_cards==0:
            return
        
        card_w = 116
        card_h = rect.h
        rect_w = rect.w
        spacing = 10

        while(True):
            l = card_w*num_cards + spacing*(num_cards-1)
            if l < rect_w:
                break
            spacing -= 1
        x = rect.x + (rect_w - l)//2
        y = rect.y
        #print(l, rect.w, x)
        for i in range(num_cards):
            self.draw_card(list_cards[i],is_face_up, x,y,card_w,card_h)
            x += (spacing + card_w)



    def render(self):
        self.screen.blit(self.res["background"], pygame.Rect(0,0,1080,720))

        deck_info = self.engine.get_deck()
        self.draw_deck(deck_info,self.rects["deck"])

        """
        card = {
            "back": "red",
            "rank": 12,
            "suit": "diamonds"
        } 
        self.draw_card(card,True,200,200,112,160)
        """

        self.draw_list_cards_large(True, self.engine.get_player_hand(0),self.rects["player_hand"])
        self.draw_list_cards_large(False, self.engine.get_player_hand(1),self.rects["opponent_hand"])
        
        pygame.display.flip()
        

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
