import pygame, simpleGE

""" it's raining men 1-3 steps
    Build your roster!
"""

class Men(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Men.png")
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
        self.men = Men(self)
        self.sprites = [self.men]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()