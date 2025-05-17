import pygame
from player import *
from enemy import *

class MazeGame():
    def __init__(self):
        self.window = pygame.display.set_mode((700,500))
        pygame.display.set_caption("Maze")
        self.bg = pygame.image.load("asset/character/bg.jpg")
        self.bg = pygame.transform.scale(self.bg,(750,500))
        self.player_img = pygame.image.load("asset/character/elf/idle/elf_f_idle_anim_f0.png")
        self.player_img = pygame.transform.scale(self.player_img,(64,112))
        self.enemy_img = pygame.image.load("asset/character/boss/idle/big_demon_idle_anim_f0.png")
        self.enemy_img = pygame.transform.scale(self.enemy_img,(96,108))
        
        self.player = Player(200,250,self.player_img)
        self.enemy = Enemy(500,350,self.enemy_img)
        
        #time
        self.clock = pygame.time.Clock()
        
    def run(self):
        running = True
        while running:
            delta_time = self.clock.tick(120) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.window.blit(self.bg,(0,0))
            self.player.draw(self.window)
            self.player.move(delta_time)
            self.enemy.draw(self.window)
            pygame.display.update()
                    
game = MazeGame()
game.run()