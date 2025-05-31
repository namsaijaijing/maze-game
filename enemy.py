import pygame

class Enemy():
    
    def __init__(self,x,y,animation):
        self.animation = animation
        self.rect = self.animation[0].get_rect(topleft = (x,y))
        self.image = self.animation[0]
        self.start_time = pygame.time.get_ticks()
        self.update_time = pygame.time.get_ticks()
        self.cur_frame = 0
        self.direction = -1
        self.is_filp = 1
        
    def draw(self,window):
        self.flip = pygame.transform.flip(self.image, self.is_filp, 0)
        window.blit(self.flip, (self.rect.x,self.rect.y))
        
    def move(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time -self.update_time
        if (delta_time <= 2000):
            self.rect.x += self.direction
        else:
            self.is_filp = (self.is_filp + 1)%2
            self.direction *= -1
            self.update_time = current_time
        
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.start_time
        if self.cur_frame >= len(self.animation):
            self.cur_frame = 0
        if delta_time > 70:           
            self.image = self.animation[self.cur_frame]
            self.cur_frame += 1
            self.start_time = current_time