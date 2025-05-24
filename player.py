import pygame

class Player():
    
    def __init__(self,x,y,animation):
        self.animation = animation
        self.image = self.animation[0]
        self.rect = self.animation[0].get_rect(topleft = (x,y))
        self.speed = 500
        self.cur_frame = 0
        self.start_time = pygame.time.get_ticks()
        self.is_filp = 0
        
    def move(self,delta_time):
        pressed = pygame.key.get_pressed()
        print(delta_time)
        if pressed[pygame.K_w]:
            self.rect.y -= self.speed * delta_time
        if pressed[pygame.K_s]:
            self.rect.y += self.speed * delta_time
        if pressed[pygame.K_a]:
            self.rect.x -= self.speed * delta_time
            self.is_filp = 1
        if pressed[pygame.K_d]:
            self.rect.x += self.speed * delta_time
            self.is_filp = 0
            
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.start_time
        print(delta_time)
        if self.cur_frame >= len(self.animation):
            self.cur_frame = 0
        if delta_time > 70:           
            self.image = self.animation[self.cur_frame]
            self.cur_frame += 1
            self.start_time = current_time
        
        
    def draw(self,window):
        self.filp = pygame.transform.flip(self.image,self.is_filp,0)
        window.blit(self.filp,(self.rect.x,self.rect.y))