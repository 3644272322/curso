try:
    import pygame as pg
    import os
    from enemy import Enemies
    from character import Character
    from turret import Turret
    import config as cg
except IndexError as e:
    print('Error al importar la libreria', e)

# crear la planitlla del juego RootGame 
class RootGame:
    def __init__(self):
        self.pg = pg.init()
        self.creen.pg.display.set_mode((cg.screen_width, cg.screen_height))
        self.clock.pg.time.Clock()
        self.cwd = os.getcwd()

        self.load_assets()
        self.create_group()
        self.draw_weadpoints()
    
    def load_assets(self):
        self.character_image = pg.imagen.load(os.path.join(self.cwd, "python", "games","00_g" "assets","enemies","enemy1.pog")).convert_alpha()
        self.enemy_image = pg.imagen.load(os.path.join(self.cwd, "python", "games","00_g" "assets","enemies","enemy1.pog")).convert_alpha()

    def create_group(self):
        self.enemy_group = pg.spriste.Group()
        self.player_group = pg.spriste.Group()

    def draw_weadpoints(self):
        self.weadpoints = [
            (100, 300)
        ]

    def instance(self):
        enemy_one = Enemies((300,300), self.enemy_image)
        self.enemy_group.add(enemy_one)
        self.player = Character((100.150),self.character_image)
        
    def run(self):
        #gamelop
        delta = 0
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run=False
        self.screen.fill("gray100")

        self.enemy_group.update(self.screen)
        # dibujar el enemy en la ventana
        self.enemy_group.draw(self.screen)

        # dibujar el enemy en la ventana
        self.player_group.draw(self.screen)

        # detectar las teclas
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_w] or self.keys[pg.K_UP]:
            self.player.move_up(300 * delta) 
            pg.transform.rotate(self.player_image, 90)
        if self.keys[pg.K_s] or self.keys[pg.K_DOWN]:
            self.player.move_down (300 * delta)
        if self.keys[pg.K_a] or self.keys[pg.K_LEFT]:
            self.player.move_left(300 * delta)
        if  self.keys[pg.K_d] or self.keys[pg.K_RIGHT]:
            self.player.move_rigth(300 * delta)

        delta = self.clock.tick(cg.fps) / 1000
        self.clock.tick(cg.fps)
        #actualizar la ventana
        pg.display.flip(cg.fps)

    pg.quit()