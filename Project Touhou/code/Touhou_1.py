
from typing import Any
import sys, os
import random as rm
from numpy import size
import pygame as Pg
from pygame.locals import *


Black =         (  0,   0,   0)
Gray =          (128, 128, 128)
White =         (255, 255, 255)
Green =         (  0, 255,   0)
Blue =          (  0,   0, 255)
Blue_Space =    (  0,   0,  10)
Red =           (255,   0,   0)
Color =         ( 50,   5,   0)        

class Game:
    
    def __init__(self):
        Pg.init()
        Pg.mixer.init()
        # Tamaño de la ventana
        self.ancho = 800
        self.alto = 500
        self.size_min = (self.ancho, self.alto)          
        self.VN = Pg.display.set_mode(self.size_min)     
        self.clock = Pg.time.Clock()
        self.run = True
        self.FPS = 60
        self.life = 3
        self.cont = 3
        self.score = 0
        self.best_score = 0

        self.Frame_0 = Pg.image.load("Project Touhou/Sprites/Reimu_Hakurei/Reimu_frame_1.png").convert()           # Standart
        self.Frame_0.set_colorkey(Black)
        self.Frame_1 = Pg.image.load("Project Touhou/Sprites/Reimu_Hakurei/Reimu_Hakurei_Frame_1.png").convert()   # Forward
        self.Frame_1.set_colorkey(Black)
        self.Frame_2 = Pg.image.load("Project Touhou/Sprites/Reimu_Hakurei/Reimu_Hakurei_Frame_2.png").convert()   # Right
        self.Frame_2.set_colorkey(Black)
        self.Frame_3 = Pg.image.load("Project Touhou/Sprites/Reimu_Hakurei/Reimu_Hakurei_Frame_3.png").convert()   # Left
        self.Frame_3.set_colorkey(Black)
        self.found = Pg.image.load("Project Touhou/found/found_1.png").convert()
        Pg.display.set_icon(self.Frame_0)
        
    def Draw_text(self, surface, text, size, x, y):
        font = Pg.font.SysFont("serif", size)
        text_surface = font.render(text, True,White)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    def new_game(self):
        self.pounts = 0
        self.level = 1

    def draw(self):
        self.VN.blit(self.found, [230,0])
        self.Draw_text(self.VN, f"puntos: {str(self.pounts)}", 15 , 630, 20)
        self.Draw_text(self.VN, f"niveles: {str(self.level)}", 10 , 630, 40)

    # def check_event(self):
    #     for event in Pg.event.get():
    #         if event.type == Pg.QUIT:
    #             Pg.quit()
    #             sys.exit()

    
GM = Game()



class Player(Pg.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = [GM.Frame_0, GM.Frame_1, GM.Frame_2, GM.Frame_3]
        self.rects = []
        for s in self.image:
            self.rect = s.get_rect()
            self.rect.centerx = GM.ancho // 2
            self.rect.centery = GM.alto - 50
            self.rect.x -= self.rect.width // 2  # Ajuste para alinear en el centro
            self.rect.y -= self.rect.height // 2  # Ajuste para alinear en el centro
            self.rects.append(self.rect)

        self.current_sprite = 0
        self.rect = self.rects[self.current_sprite]
        self.pos_x = GM.ancho //2
        self.pos_y = GM.alto - 50
        self.velocidad = 5
        self.attemps = 10
        self.puede_moverse = True
        
        if self.velocidad > 5:
            self.velocidad = 5
    def mover_arriba(self):
        if self.puede_moverse == True:
            self.pos_y -= self.velocidad
    def mover_abajo(self):
        if self.puede_moverse == True:
            self.pos_y += self.velocidad
    def mover_izquierda(self):
        if self.puede_moverse == True:
            self.pos_x -= self.velocidad
    def mover_derecha(self):
        if self.puede_moverse == True:
            self.pos_x += self.velocidad
    def mover_diagona_xp_yp(self):
        if self.puede_moverse == True:
            self.pos_x += self.velocidad 
            self.pos_y += self.velocidad 
    def mover_diagona_xn_yp(self):
        if self.puede_moverse == True:
            self.pos_x -= self.velocidad
            self.pos_y += self.velocidad
    def mover_diagona_xp_yn(self):
        if self.puede_moverse == True:
            self.pos_x += self.velocidad
            self.pos_y -= self.velocidad 
    def mover_diagona_xn_yn(self):
        if self.puede_moverse == True:
            self.pos_x -= self.velocidad
            self.pos_y -= self.velocidad
    def update_sprite(self, keys):
        
        self.rect = self.rects[self.current_sprite]
        if self.pos_x > 543:
            self.pos_x = 543
        if self.pos_x < 235:
            self.pos_x = 235
        if self.pos_y > 460:
            self.pos_y = 460
        if self.pos_y < 0:
            self.pos_y = 0
        if keys[K_LSHIFT]:
            self.velocidad = 2.5
        else: 
             self.velocidad = 5
        if keys[K_a]:
            if keys[K_a] and keys[K_w]:
                self.mover_diagona_xn_yn() 
            elif keys[K_a] and keys[K_s]:
                self.mover_diagona_xn_yp()
                self.current_sprite = 0 
            else:
                self.mover_izquierda()
                self.current_sprite = 3
        elif keys[K_d]:
            if keys[K_d] and keys[K_w]:
                self.mover_diagona_xp_yn()
                self.current_sprite = 1  
            elif keys[K_d] and keys[K_s]:
                self.mover_diagona_xp_yp()                    # Right
            else:
                self.mover_derecha()
                self.current_sprite = 2
        elif keys[K_w]:
                if keys[K_a] and keys[K_w]:
                    pass
                elif keys[K_d] and keys[K_w]:
                    pass
                else:
                    self.mover_arriba()
                    self.current_sprite = 1                                     # Forward
        elif keys[K_s]:
            if keys[K_a] and keys[K_s]:
                 pass
            elif keys[K_d] and keys[K_s]:
                pass
            else:
                self.mover_abajo()
                self.current_sprite = 0
            
        if not keys[K_a] or not keys[K_d] or not keys[K_w] or not keys[K_s]:
            self.current_sprite = 0

        
    def shoot(self):
        bullet = Player_Bullets(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

player = Player()
class Boss(Pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Pg.image.load("Project Touhou/Sprites/Enemy/sprite_enemy_1.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = GM.ancho // 2
        self.rect.centery = 40
        self.x = GM.ancho / 2
        self.y = self.rect.centery

        self.speed = 10

    
    def update(self):
        if self.y <= 40:
            self.y += self.speed
boss = Boss()
class Player_Bullets(Pg.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = Pg.image.load("token.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.rect.y = y
        self.vel_y = -10
 

    def update(self):
        if keys[K_z]:
            self.rect.centery += self.vel_y
            if self.rect.bottom < 0:   
                self.kill()
            

coor_list = []
coor_list1 = []

all_sprites = Pg.sprite.Group()
bullets = Pg.sprite.Group()
enemy = Pg.sprite.Group()
enemy.add(boss)
all_sprites.add(player)


for i in range(200):
    x = rm.randint(225, 575)
    y = rm.randint(0, GM.alto)
    coor_list.append([x,y])

for c in range(200):
    x = rm.randint(225, 575)
    y = rm.randint(0, GM.alto)
    coor_list1.append([x,y])

# Bucle para que el juego se ejecute correctamente
while True:
    for event in Pg.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = Pg.key.get_pressed()
    player.update_sprite(keys)
    Pg.draw.rect(GM.VN, Blue_Space,(0,0,GM.ancho,GM.alto))
    # Limites
    Pg.draw.rect(GM.VN, Color,(  0,   0, 225, GM.alto))            # [posicion x], [posicion y],  [ancho], [alto]
    Pg.draw.rect(GM.VN, Color,(575,   0, 225, GM.alto))            # [posicion x], [posicion y],  [ancho], [alto]

    # Animaciones
    Pg.draw.rect(GM.VN, Gray, (100, 350, 100,  30 ))            # [posicion x], [posicion y],  [ancho], [alto]
    Pg.draw.rect(GM.VN, Black,(585,  25, 210,  40 ))
    Pg.draw.rect(GM.VN, (128, 0, 0)  ,(590,  30, 200,  30 ))
    Pg.draw.rect(GM.VN, Black,(592.5,  32.5, 196,  26 ))        # [posicion x], [posicion y],  [ancho], [alto]    

    all_sprites.update() 
    

    #GM.draw()
    
    player.rect.topleft = (player.pos_x, player.pos_y)
    GM.VN.blit(player.image[player.current_sprite], player.rect) 
    GM.VN.blit(boss.image, boss.rect)
    #   all_sprites.draw(GM.VN)
    


    Pg.display.flip()
    GM.clock.tick(60)
    