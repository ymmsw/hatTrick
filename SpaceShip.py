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
        self.setImage("likethat.png")
        self.setSize(100, 100)
        self.setBoundAction(self.BOUNCE)
        self.reset()
        
    def reset(self):
        self.x = (random.randint(0, 640))
        self.y = (random.randint(0, 480))
        self.setDX(random.randint(-5, 5))
        self.setDY(random.randint(-5, 5))
    
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.reset()
        if self.collidesWith(self.scene.usership):
            self.scene.score += 1

        

        
class Usership(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("output-onlinepngtools.png")
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
     scene = simpleGE.Scene()
     scene.background = pygame.image.load("kobe.jpg")
     scene.background = pygame.transform.scale(scene.background, (640, 480))
     scene.setCaption("Destroy all the asteroids before time runs out")    
     asteroid = Asteroid(scene)
     usership = Usership(scene)
     
     asteroids = []
     for i in range(7):
         asteroids.append(Asteroid(scene))
         

     
     
     scene.sprites = [asteroids, usership]
     scene.start()

if __name__ == "__main__":
    main()
          

    