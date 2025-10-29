import pygame, simpleGE, random

""" it's raining men 1-3 steps
    Build your roster!
"""

class Men(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Men.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class Guy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Guy.gif")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Beach.png")
        
        self.sndMen = simpleGE.Sound("DohSound.wav")
        
        self.guy = Guy(self)
        self.men = Men(self)
        
        self.sprites = [self.guy,
                        self.men]
    
    def process(self):
        if self.guy.collidesWith(self.men):
            self.sndMen.play()
            self.men.reset()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()