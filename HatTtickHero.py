# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:50:54 2023

@author: Ymmsw
"""
import pygame
import simpleGE
import random

class Goalpost(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("GPP.png")
        self.setSize(100, 50)
        self.y = 450
        self.x = 320
        self.setBoundAction(self.BOUNCE)
        self.reset()
        
    def reset(self):
        self.setDX(30)
        
        
        
class Ball(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("kiss.png")
        self.setSize(20, 20)
        self.y = 160
        self.x = 320
        self.setDY(0)
        self.ballBitch = simpleGE.Sound("selina.wav")
        self.ballSound = simpleGE.Sound("catwoman2.wav")
        self.score = 0
        self.misses = 0
        

        

        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.setDY(21)
        if self.collidesWith(self.scene.goalpost):
            self.score += 1
            self.ballBitch.play()
            self.reset()    
            self.checkbounds()
            
    def checkbounds(self):
        if self.rect.bottom > self.screen.get_height():
            self.misses += 1
            self.ballSound.play()
            self.reset() 
            
            
    def reset(self):
        self.y = 160
        self.x = 320
        self.setDY(0)

class Striker(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("jude.png")
        self.setSize(100, 100)
        self.y = 120
        self.x = 380
        
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("FP.jpg")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Score a Hattrick")
        #self.goalpost = Goalpost(self)
        #self.ball = Ball(self)
        #self.striker = Striker(self)
        

        #self.instruction = Instructions()
        #self.lblTimer = LblTimer()
        #self.goalMissCounter = GoalMissCounter()

        self.sprites = [self.goalpost]  
    
        self.sprites = [self.goalpost, self.ball, self.striker, self.instruction, self.lblTimer, self.goalMissCounter]

class Instructions(simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines = ["Score a HATTRICK to win the game. "]
        self.center = ((320, 240))
        self.size = ((380, 80))
        self.hide()
        

        self.font = pygame.font.Font("goodfoot.ttf", 40)
        self.fgColor = (0x00, 0XCC, 0XFF)
        self.bgColor = (0x00, 0000, 0000)


class GoalMissCounter(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.goals = 0
        self.misses = 0
        self.text = f"Goals: {self.goals} | Misses: {self.misses}"
        self.center = (100, 40)
        self.size = (200, 30)

    def goals(self):
        self.goals += 1
        self.update_text()

    def misses(self):
        self.misses += 1
        self.update_text()

    def update_text(self):
        self.text = f"Goals: {self.goals} | Misses: {self.misses}"

class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.timer = simpleGE.Timer()
        self.timeQuit = False
        
    def checkEvents(self):
        timeLeft = 30 - self.timer.getElapsedTime()
        self.text = f"{timeLeft: 2f}"
        
            
        if timeLeft <= 0:
            self.timeQuit = True
            
    def reset(self):
        self.timeQuit = False
        self.timer.start()
        
def main():


    game = simpleGE.Scene()
    game.start()


if __name__ == "__main__":
    main()
