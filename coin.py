import pygame

class Coin(pygame.sprite.Sprite):
    
    def __init__(self,x,y,animation):
        super().__init__()
        self.animation = animation
        self.image = self.animation[0] 
        self.rect = self.image.get_rect(x=x,y=y)
        self.start_time = pygame.time.get_ticks()
        self.cur_frame = 0
        
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.start_time
        if self.cur_frame >= len(self.animation):
            self.cur_frame = 0
        if delta_time > 100:           
            self.image = self.animation[self.cur_frame]
            self.cur_frame += 1
            self.start_time = current_time
            
    def check_collide(self,player):
        if player.rect.colliderect(self.rect):
            player.score += 1
            self.kill()
        