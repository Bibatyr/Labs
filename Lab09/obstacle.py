import entity
import random
import settings

class Obstacle(entity.Entity):
    def __init__(self, width, ascpect_ratio, image_path, speed):
        super().__init__(width, ascpect_ratio, image_path, speed)
        self.rect.center = self.randomize_position()
    
    def randomize_position(self):
        y = int(-self.height)
        x = random.randint(25, settings.SCREEN_WIDTH - 25 - self.rect.width)
        return x, y
    
    def move(self):
        self.rect.move_ip(0, self.MOVEMENT_SPEED)
        if(self.rect.top > 600):
            self.__init__()