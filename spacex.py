# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:12:08 2023

@author: Ymmsw
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:02:23 2023

@author: Ymmsw
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:03:35 2023

@author: Ymmsw
"""
import pygame, simpleGE
import random

  
class Asteroid(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("MP1.png")
        self.setSize(100, 100)
        self.setBoundAction(self.BOUNCE)
        self.asteroidSound = simpleGE.Sound("buchiecatenjoyer.wav")
        self.reset()
        
    def reset(self):
        self.x = (random.randint(0, 640))
        self.y = (random.randint(0, 480))
        self.setDX(random.randint(-5, 5))
        self.setDY(random.randint(-5, 5))
    
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.reset()
            
class Usership(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("MP1.png")
        self.setSize(60, 60)
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.turnBy(5)
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.turnBy(-5)
        if self.scene.isKeyPressed(pygame.K_UP):
            self.forward(5)
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.forward(-5)



class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
def main():
     game = simpleGE.Scene()
     game.background = pygame.image.load("FP.jpg")
     game.background = pygame.transform.scale(game.background, (640, 480))
     game.setCaption("Destroy all the asteroids before time runs out")
     game.usership = Usership(game)
     game.asteroidSound = simpleGE.Sound("buchiecatenjoyer.wav") 
     
     asteroids = []
     for i in range(7):
         asteroids.append(Asteroid(game))

           
     
     game.sprites = [asteroids, game.usership]
     game.start()

if __name__ == "__main__":
    main()
          

    