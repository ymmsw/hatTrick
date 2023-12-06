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
import pygame, simpleGE, spacex
import random

  
class Asteroid(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("likethat.png")
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
            self.addForce(.2, self.rotation)

class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.timer = simpleGE.Timer()
        self.timeOver = False
        self.hide()
        
    def checkEvents(self):
        timeLeft = 5 - self.timer.getElapsedTime()
        self.text = f"{timeLeft:.2f}"
        
       
        if self.center[0] < 0:
            timeLeft = 1000
            
        if timeLeft < 0:
            self.timeOver = True

    def reset(self):
        self.timeOver = False
        self.timer.start()



class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("kobe.jpg")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Destroy all the asteroids before time runs out")
        self.usership = spacex.Usership(self)
        asteroids = []
        for i in range(4):
            asteroids.append(Asteroid(self))
        self.sprites = [self.usership]
        self.asteroidGroup = self.makeSpriteGroup(asteroids)
        self.addGroup(self.asteroidGroup)
        self.asteroidSound = simpleGE.Sound("buchiecatenjoyer.wav")
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (50, 50)
        self.score = 0


        self.sprites = [self.lblScore, self.asteroidGroup, self.usership]

    def update(self):
        timeLeft = 30 - self.timer.getElapsedTime()
        if timeLeft < 0:
            self.stop()
        self.lblTime.text = f"Time left: {timeLeft:.2f}"
        self.lblScore.text = f"score: {self.score}"
   

        
    def update(self):
        asteroidHit = self.usership.collidesGroup(self.asteroidGroup)
        if asteroidHit:
            asteroidHit.reset()
            self.asteroidSound.play()

    
        
        
        
        
def main():
    
     game = Game()
     game.start()

if __name__ == "__main__":
    main()
          

    