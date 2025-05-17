import pygame

class Player():
    
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 500
        
    def move(self,delta_time):
        pressed = pygame.key.get_pressed()
        print(delta_time)
        if pressed[pygame.K_w]:
            self.rect.y -= self.speed * delta_time
        if pressed[pygame.K_s]:
            self.rect.y += self.speed * delta_time
        if pressed[pygame.K_a]:
            self.rect.x -= self.speed * delta_time
        if pressed[pygame.K_d]:
            self.rect.x += self.speed * delta_time
        
    def draw(self,window):
        window.blit(self.image,(self.rect.x,self.rect.y))