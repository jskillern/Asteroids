from constants import *
from circleshape import *

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
            super().__init__(x,y, radius)
            pygame.sprite.Sprite.__init__(self)
            self.add(self.containers)
            

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x, self.position.y), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)    