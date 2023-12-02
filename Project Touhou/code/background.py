from turtle import back
import pygame as PG
import sys
from pygame.locals import *
from sympy import limit

Black =         (  0,   0,   0)
Gray =          (128, 128, 128)
White =         (255, 255, 255)
Green =         (  0, 255,   0)
Blue =          (  0,   0, 255)
Blue_Space =    (  0,   0,  10)
Red =           (255,   0,   0)



ancho = 800
alto = 500

back_x = ancho / 3
limit_x_p = ancho / 1.6
limit_x_n = ancho / 0.8
back_y = alto / 2
ancho_x = 15
alto_y = 10
size_min = (ancho, alto)           # ancho x alto
Ventana = PG.display.set_mode(size_min)     # Crear la ventana del juego
direccion = 1  # Variable de dirección: 1 para moverse hacia la derecha, -1 para moverse hacia la izquierda

# Control FPS
clock = PG.time.Clock()


while True:
    for event in PG.event.get():
        if event.type == QUIT:
            sys.exit()
        print(event)
    PG.draw.rect(Ventana, Blue_Space,(0,0,ancho,alto))         # [posicion x], [posicion y],  [ancho], [alto]
        
    #if back_x < limit_x_p:
     #   back_x += 1
    
    if direccion == 1:  # Si la dirección es 1, moverse hacia la derecha
        back_x += 1
        if back_x < limit_x_p*3/7:
            ancho_x += 1
            alto_y += 1
        if back_x > limit_x_p*5/7:
            ancho_x -= 1
            alto_y -= 1
        if back_x >= limit_x_p:  # Si el cubo alcanza el límite derecho
            direccion = -1  # Cambiar la dirección a -1 para moverse hacia la izquierda
    else:  # Si la dirección es -1, moverse hacia la izquierda
        back_x -= 1
        if back_x > limit_x_p*5/7:
            ancho_x += 1
            alto_y += 1
        if back_x < limit_x_p*5/7:
            ancho_x -= 1
            alto_y -= 1
        if back_x <= ancho / 3:  # Si el cubo alcanza el límite izquierdo
            direccion = 1  # Cambiar la dirección a 1 para moverse hacia la derecha
    

    PG.draw.rect(Ventana, White,(back_x, back_y, ancho_x, alto_y))

    PG.display.flip()
    clock.tick(60)