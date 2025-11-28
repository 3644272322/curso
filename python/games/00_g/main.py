import pygame as pg
import os
from enemy import Enemies
from character import Character

#configuracion de la ventana
screen_width = 800
screen_height = 800
fps = 60

#iniciar pygame
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
delta = 0

# cargar imagenes
enemy_image = pg.image.load(os.path.join('python/games/asset/enemy', 'tank_blue.png')).convert_alpha()
player_image = pg.image.load(os.path.join('python/games/asset/enemy', 'tank_blue.png')).convert_alpha()

#configuracion de la ventana
enemy_group = pg.sprite.Group()
enemy_one = Enemies((300,300),enemy_image)
enemy_group.add(enemy_one)

#crear jugador o player
player_group = pg.sprite.Group()
player = Character((150,150), player_image)
player_group.add(player)

#gamelop
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
    screen.fill("gray100")

    enemy_group.update()
    # dibujar el enemy en la ventana
    enemy_group.draw(screen)

    # dibujar el enemy en la ventana
    player_group.draw(screen)

    # detectar las teclas
    keys = pg.key.get_pressed()
    if keys[pg.K_w] or keys[pg.K_UP]:
        player.move_up(300 * delta) 
        pg.transform.rotate(player_image, 90)
    if keys[pg.K_s] or keys[pg.K_DOWN]:
        player.move_down (300 * delta)
    if keys[pg.K_a] or keys[pg.K_LEFT]:
        player.move_left(300 * delta)
    if  keys[pg.K_d] or keys[pg.K_RIGHT]:
        player.move_rigth(300 * delta)

    delta = clock.tick(fps) / 1000
    clock.tick(fps)
    #actualizar la ventana
    pg.display.flip()

pg.quit() 