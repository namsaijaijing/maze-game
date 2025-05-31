import pygame
from player import *
from enemy import *
from coin import *
from wall import *
import os
import csv

class MazeGame():
    def __init__(self):
        self.window = pygame.display.set_mode((800,640))
        pygame.display.set_caption("Maze")
        self.bg = pygame.image.load("asset/background/bg.jpg")
        self.bg = pygame.transform.scale(self.bg,(800,640))
        # self.player_img = pygame.image.load("asset/character/elf/idle/elf_f_idle_anim_f0.png")
        # self.player_img = pygame.transform.scale(self.player_img,(64,112))
        # self.enemy_img = pygame.image.load("asset/character/boss/idle/big_demon_idle_anim_f0.png")
        # self.enemy_img = pygame.transform.scale(self.enemy_img,(96,108))
        
        #animation
        self.animation_player = self.load_animate_player()
        self.animation_enemy = self.load_animate_enemy()
        self.animation_coin = self.load_animate_coin()
        
        self.player = Player(80,70,self.animation_player)
        self.enemy1 = Enemy(650,450,self.animation_enemy)
        self.enemy2 = Enemy(300,370,self.animation_enemy)
        self.enemy3 = Enemy(680,100,self.animation_enemy)
        
        #coin
        self.coin1 = Coin (95,530,self.animation_coin)
        self.coin2 = Coin (700,50,self.animation_coin)
        self.coin3 = Coin (700,530,self.animation_coin)
        
        self.coins_group = pygame.sprite.Group()
        self.coins_group.add(self.coin1)
        self.coins_group.add(self.coin2)
        self.coins_group.add(self.coin3)
        
        #time
        self.clock = pygame.time.Clock()
        
        
        self.wall_img = pygame.image.load("asset/level/wall.png")
        self.wall_img = pygame.transform.scale(self.wall_img,(32,32))
        self.walls = []
        self.generate_wall()
        
    def load_animate_player(self):
        path = "asset/character/skel/idle"
        lst = []
        for i in range(4):
            img = pygame.image.load(os.path.join(path, f"{i}.png"))
            img = pygame.transform.scale(img,(64,64))
            lst.append(img)
            
        return lst
    
    def load_animate_enemy(self):
        path = "asset/character/boss/run/"
        lst = []
        for i in range(4):
            img = pygame.image.load(os.path.join(path, f"run{i}.png"))
            img = pygame.transform.scale(img,(96,108))
            lst.append(img)
            
        return lst
    
    
    def load_animate_coin(self):
        path = "asset/items"
        lst = []
        for i in range(4):
            img = pygame.image.load(os.path.join(path, f"coin_f{i}.png"))
            img = pygame.transform.scale(img,(32,32))
            lst.append(img)
            
        return lst
    
    def generate_wall(self):
        with open("asset/level/map.csv","r") as file:
            self.map = csv.reader(file)
            for r,row in enumerate(self.map):
                for c,col in enumerate(row):
                    if (col == "1"):
                        x = c*self.wall_img.get_width()
                        y = r*self.wall_img.get_width()
                        wall = Wall(x,y,self.wall_img)
                        self.walls.append(wall)
            
    def run(self):
        running = True
        while running:
            delta_time = self.clock.tick(120) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.window.blit(self.bg,(0,0))
            for wall in self.walls:
                wall.draw(self.window)
            self.player.draw(self.window)
            self.player.update()
            self.player.move(delta_time)
            self.enemy1.draw(self.window)
            self.enemy1.update()
            self.enemy1.move()
            self.enemy2.draw(self.window)
            self.enemy2.update()
            self.enemy2.move()
            self.enemy3.draw(self.window)
            self.enemy3.update()
            self.enemy3.move()
            self.coins_group.draw(self.window)
            self.coins_group.update()
            for coin in self.coins_group:
                coin.check_collide(self.player)
            pygame.display.update()
                    
game = MazeGame()
game.run()