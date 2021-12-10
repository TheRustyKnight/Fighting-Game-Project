# TheRustyKnight

# Version 0.37

# This is a 2d fighting game where two players
# can fight each other until one of them is out of HP
# Player 1 starts on the left and player 2 is on the right
# The players control the characters fighting
# using A/D or J/L to move left or right
# To attack, the players will use Q/E or U/O to attack
# The game is won when one of the two is out of HP,
# and the remaining player will have a prompt showing they won
# Known bugs:
# For some unknown reason, Player1.attackState1 will not turn to true,
# despite being set to true. It was replaced with
# boolean attacking2 which works fine
# Known limitations:
# Need to restart if you want to swap charaters
# Plans:
# 1: Implement the projctile to give player
# 1 a second attack - Done
# 2: Implement a jump feature and a check for
# which side of the field the player is on - Done
# 3: Implement player class for more control
# and to possibly add more fighters - Complete
# 4: Polish game to make it
# look less like a clunky mess. - Done
# 5: Add a new fighter to the roster. - Done

# Started 10/22/2021
# Update 1, loaded code, need to slice
# sprite sheets into gifs, added Folder for images
# Update 2, need to comment a lot of this
# code since most of the stuff was uncommented
# Update 3, 10/24 Finished slicing up the first players animations
# from the sprite sheet, renamed a few variables so
# they make more sense
# Update 4, added some constants that will help clean somethings up
# Update 5, 10/27 Game successfully launches for the first time,
# need to fix sprites in the mean time
# Update 6, Added transform.flip so that player 2 actually faces the right way
# Update 7, Changing the variable names for easier implementation
# of a Player class so more fighters can be added
# Update 8, Cleaning up some redundant variables
# Update 9, 10/31 added music to the game, battle_music_1 is from
# https://www.youtube.com/watch?v=A6cSbof7Pik
# Update 10, Buffed batman so that he steps forward when punching,
# meaning he is not out ranged all the time
# Update 11, 11/1 nerfed hulk so he cannot spam the smash attack,
# gave it a cooldown timer. May add it to all attacks
# Update 12, Fixed the bug where the hulk would not animate,
# but would still attack
# Update 13, 11/2 Added a placeholder main menu screen
# Update 14, Fixed bug when you exit from
# main menu giving an error message.
# Update 15, 11/4 Added a prompt that shows who
# won when the other players HP hits 0
# Update 16, fixed bug that makes the
# other player disappear when defeated
# Update 17, added a little more pazzaze when player is defeated
# Update 18, fixed bug where batman would respawn after being
# defeated and victory for player 2 would not stay
# Update 19, Fixed bug where it would despawn
# player 2 if player 2 was victorious
# Update 20, Removed ability to move after victory,
# solving alot of glitches in the process
# Update 21, 11/7 Finally created the Player Class,
# still need to swap all the pieces over to using it
# Update 22, 11/9 expanded upon the Player class, might need to
# make a special class for Batman so he can use the projectile
# Update 23, 11/13 Attempted implementation of jump, kinda clunky at the moment
# Update 24. 11/17 After 3 days of work, both Player and Game classes
# have been implemented and integrated
# Update 25, 11/18 Jump has been implemented on both players.
# Known bug where they try to correct them selves
# needs to be dealt with
# Update 26, Added random music and background to give more life to the game
# Update 27, fixed bug that prevented player 1 from animating when attacking
# Update 28, 11/23 Implemented the projectile class
# Update 29, Fixed bug of projectile not animating while throwing
# Update 30, Limited the amount of projectiles that
# can be thrown at any one time to 3
# Update 31, 11/26 New charater, Majin Buu has been added
# Update 32, Added attackExtention, which gives different
# ranges for attacks for Batman and Majin Buu
# Update 33, Rebalanced the game, now Batman has 45 HP and
# Buu has 30 because of thier increased range of attack.
# Update 34, Added a replay button, so you do not need to
# reload the game everytime you want a rematch
# Update 35, 11/30 Added an audio for when punch hits
# Update 36, fixed bug where two Player 1 defeat sprites would be displayed
# Update 37, Fixed any Pep 8 issues

import pygame
import time
import random

pygame.init()

# Screen constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 610

FRAME_RATE = 12

MAX_DISTANCE = 180

FALLING_SPEED = 5

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# fonts
# So I can use it everywhere
font = pygame.font.SysFont("serif", 25)
fontSmall = pygame.font.SysFont("serif", 15)

# Music
ran = random.randrange(3)
# Randomizes the music, so that I can give multiple tracks
if(ran == 1):
    music1 = pygame.mixer.music.load("Music/battle_music_1.mp3")
if(ran == 2):
    music1 = pygame.mixer.music.load("Music/battle_music_2.mp3")
else:
    music1 = pygame.mixer.music.load("Music/battle_music_1.mp3")
hitsound = pygame.mixer.Sound("Music/hit_Sound.mp3")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# batman - Added idle
batman_idle = [pygame.image.load('Images/bat.gif'),
               pygame.image.load('Images/bat1.gif'),
               pygame.image.load('Images/bat2.gif'),
               pygame.image.load('Images/bat3.gif'),
               pygame.image.load('Images/bat4.gif'),
               pygame.image.load('Images/bat5.gif'),
               pygame.image.load('Images/bat6.gif'),
               pygame.image.load('Images/bat7.gif')]

majin_idle = [pygame.image.load("Images/majinidle.gif")]
# batman - added move
batman_run = [pygame.image.load('Images/batrun1.gif'),
              pygame.image.load('Images/batrun2.gif'),
              pygame.image.load('Images/batrun3.gif'),
              pygame.image.load('Images/batrun4.gif'),
              pygame.image.load('Images/batrun5.gif'),
              pygame.image.load('Images/batrun6.gif'),
              pygame.image.load('Images/batrun7.gif'),
              pygame.image.load('Images/batrun8.gif')]
majin_run = [pygame.image.load('Images/majinrun1.gif'),
             pygame.image.load('Images/majinrun2.gif'),
             pygame.image.load('Images/majinrun3.gif'),
             pygame.image.load('Images/majinrun4.gif'),
             pygame.image.load('Images/majinrun5.gif'),
             pygame.image.load('Images/majinrun6.gif')]
# batman - Added attack1
batman_attack1 = [pygame.image.load('Images/fig1.gif'),
                  pygame.image.load('Images/fig2.gif'),
                  pygame.image.load('Images/fig3.gif'),
                  pygame.image.load('Images/fig4.gif'),
                  pygame.image.load('Images/fig5.gif')]
majin_attack1 = [pygame.image.load('Images/majinfig1.gif'),
                 pygame.image.load('Images/majinfig2.gif'),
                 pygame.image.load('Images/majinfig3.gif'),
                 pygame.image.load('Images/majinfig4.gif'),
                 pygame.image.load('Images/majinfig5.gif')]
batman_attack2 = [pygame.image.load('Images/throw1.gif'),
                  pygame.image.load('Images/throw2.gif'),
                  pygame.image.load('Images/throw3.gif'),
                  pygame.image.load('Images/throw4.gif')]
majin_attack2 = [pygame.image.load('Images/majinthrow1.gif'),
                 pygame.image.load('Images/majinthrow2.gif'),
                 pygame.image.load('Images/majinthrow3.gif'),
                 pygame.image.load('Images/majinthrow4.gif')]
# hulk - Added
hulk_idle = [pygame.image.load('Images/hulk1.gif'),
             pygame.image.load('Images/hulk2.gif'),
             pygame.image.load('Images/hulk3.gif'),
             pygame.image.load('Images/hulk4.gif'),
             pygame.image.load('Images/hulk5.gif'),
             pygame.image.load('Images/hulk6.gif')]
# hulk - Added
hulk_run = [pygame.image.load('Images/hulkrun1.gif'),
            pygame.image.load('Images/hulkrun2.gif'),
            pygame.image.load('Images/hulkrun3.gif'),
            pygame.image.load('Images/hulkrun4.gif'),
            pygame.image.load('Images/hulkrun5.gif'),
            pygame.image.load('Images/hulkrun6.gif')]
# hulk - Added
hulk_attack1 = [pygame.image.load('Images/hulkAtk1.gif'),
                pygame.image.load('Images/hulkAtk2.gif'),
                pygame.image.load('Images/hulkAtk3.gif'),
                pygame.image.load('Images/hulkAtk4.gif'),
                pygame.image.load('Images/hulkAtk5.gif'),
                pygame.image.load('Images/hulkAtk6.gif')]
# hulk - Added
hulk_attack2 = [pygame.image.load('Images/punch1.gif'),
                pygame.image.load('Images/punch2.gif'),
                pygame.image.load('Images/punch3.gif'),
                pygame.image.load('Images/punch4.gif'),
                pygame.image.load('Images/punch5.gif'),
                pygame.image.load('Images/punch6.gif')]
# batman-added
batman_defeat = [pygame.image.load('Images/fall.gif'),
                 pygame.image.load('Images/fall2.gif'),
                 pygame.image.load('Images/fall3.gif'),
                 pygame.image.load('Images/fall4.gif'),
                 pygame.image.load('Images/fall5.gif'),
                 pygame.image.load('Images/fall6.gif'),
                 pygame.image.load('Images/fall7.gif'),
                 pygame.image.load('Images/fall8.gif')]
majin_defeat = [pygame.image.load('Images/majindefeat1.gif'),
                pygame.image.load('Images/majindefeat2.gif'),
                pygame.image.load('Images/majindefeat3.gif'),
                pygame.image.load('Images/majindefeat4.gif'),
                pygame.image.load('Images/majindefeat5.gif'),
                pygame.image.load('Images/majindefeat6.gif'),
                pygame.image.load('Images/majindefeat7.gif'),
                pygame.image.load('Images/majindefeat8.gif')]
# hulk - Added
hulk_defeat = [pygame.image.load('Images/oof.gif'),
               pygame.image.load('Images/oof.gif'),
               pygame.image.load('Images/oof2.gif'),
               pygame.image.load('Images/oof2.gif'),
               pygame.image.load('Images/oof3.gif'),
               pygame.image.load('Images/oof3.gif'),
               pygame.image.load('Images/oof4.gif'),
               pygame.image.load('Images/oof4.gif'),
               pygame.image.load('Images/oof5.gif'),
               pygame.image.load('Images/oof5.gif')]
# batman - Added
damage = [pygame.image.load('Images/dam.gif'),
          pygame.image.load('Images/dam.gif'),
          pygame.image.load('Images/dam.gif'),
          pygame.image.load('Images/dam.gif'),
          pygame.image.load('Images/dam2.gif'),
          pygame.image.load('Images/dam2.gif'),
          pygame.image.load('Images/dam2.gif'),
          pygame.image.load('Images/dam3.gif'),
          pygame.image.load('Images/dam3.gif'),
          pygame.image.load('Images/dam3.gif'),
          pygame.image.load('Images/dam3.gif'),
          pygame.image.load('Images/dam3.gif'),
          pygame.image.load('Images/dam4.gif'),
          pygame.image.load('Images/dam4.gif'),
          pygame.image.load('Images/dam4.gif'),
          pygame.image.load('Images/dam4.gif'),
          pygame.image.load('Images/dam5.gif'),
          pygame.image.load('Images/dam5.gif'),
          pygame.image.load('Images/dam5.gif'),
          pygame.image.load('Images/dam5.gif'),
          pygame.image.load('Images/dam6.gif'),
          pygame.image.load('Images/dam6.gif'),
          pygame.image.load('Images/dam6.gif'),
          pygame.image.load('Images/dam6.gif')]

majin_damage = [pygame.image.load('Images/majindam1.gif'),
                pygame.image.load('Images/majindam2.gif')]

projectile = pygame.image.load("Images/projectile.gif")
# hulk
out = pygame.image.load('Images/oof5.gif')
hulkhit = [pygame.image.load('Images/ouch.gif')]

ran2 = random.randrange(3)

if ran2 == 1:
    bg = pygame.image.load('Images/city.jpg')
elif ran2 == 2:
    bg = pygame.image.load('Images/city_2.jpg')
else:
    bg = pygame.image.load('Images/city_2.jpg')

char = pygame.image.load('Images/bat1.gif')
# batman idle animation - Added
charl = pygame.image.load('Images/batrun1.gif')
hul = pygame.image.load('Images/hulk1.gif')
# hulk idle animation

jumpBat = pygame.image.load('Images/bat1.gif')
jumpHulk = pygame.image.load('Images/hulkAtk1.gif')
jumpMajin = pygame.image.load('Images/majinidle.gif')


fall = False
fallcount = 0
changer1 = 1
changer = 1
change = 18

jumpRight1 = False
jumpLeft1 = False
jumpEnd = False
jumpCount = 0

jumpRight2 = False
jumpLeft2 = False
jumpEnd2 = False
jumpCount2 = 0
fallSpeed = 10

attackCooldown2 = 0

ProjectileList = []

attacking2 = False

# This controls things like player animations and actions,
# Game will control the players interacting


class Player():
    def __init__(self, PlayerNumber, hpCount, idle_Animation, run_Animation,
                 attack_Animation1, attack_Animation2,
                 defeat_Animation, damage_Animation, hpBarColor,
                 jumpSprite, attackExtention1, attackAmount1, attackAmount2):

        if(PlayerNumber == 1):
            self.currentSide = False
            # left side, no flip
            self.x_pos = 375
        elif(PlayerNumber == 2):
            self.currentSide = True
            # Flip
            self.x_pos = 410
        # True if on the left side, false if on the right side.
        # This is so the game knows to flip the sprite
        self.y_pos = 455
        self.attackExtention1 = attackExtention1
        self.idle_Animation = idle_Animation
        self.idleTotal = len(idle_Animation) - 1
        self.idleCounter = 0
        self.idleState = True
        self.run_Animation = run_Animation
        self.runTotal = len(run_Animation) - 1
        self.runCounter = 0
        self.runStateRight = False
        self.runStateLeft = False
        self.attack_Animation1 = attack_Animation1
        self.attack1Total = len(attack_Animation1) - 1
        self.attack1Counter = 0
        self.attack1State = False
        self.attack1Cooldown = 0
        self.attack_Animation2 = attack_Animation2
        self.attack2Total = len(attack_Animation2) - 1
        self.attack2Counter = 0
        self.attack2State = False
        self.attack2Cooldown = 0
        self.defeat_Animation = defeat_Animation
        self.defeatTotal = len(defeat_Animation) - 1
        self.defeatCounter = 0
        self.defeatState = False
        self.damage_Animation = damage_Animation
        self.damageTotal = len(damage_Animation) - 1
        self.damageCounter = 0
        self.damageState = False
        self.hpBarColor = hpBarColor
        self.hpCount = hpCount
        self.maxHpCount = hpCount
        self.bar = True
        self.attackAmount1 = attackAmount1
        self.attackAmount2 = attackAmount2
        self.jumpRight = False
        self.jumpLeft = False
        self.jumpEnd = False
        self.jumpCount = 0
        self.jumpSprite = jumpSprite

    def showHP(self, currentSide):
        if(currentSide):
            pygame.draw.rect(screen, BLACK, (0, 0, 75 * 5 - 10, 17))
            pygame.draw.rect(screen, self.hpBarColor,
                             (0, 0, self.hpCount * 5 + 5, 14))
            player1HpDisplay = fontSmall.render("HP:" +
                                                str(self.hpCount), True, BLACK)
            screen.blit(player1HpDisplay, [0, 0])
        else:
            pygame.draw.rect(screen, BLACK,
                             (75 * 7, 0, 75 * 5 + 2, 16))
            # Outline, so that you can see the hp
            pygame.draw.rect(screen, self.hpBarColor,
                             (SCREEN_WIDTH - (self.hpCount * 5), 0,
                              self.hpCount * 5, 14))
            player2HpDisplay = fontSmall.render("HP:" + str(self.hpCount),
                                                True, BLACK)
            screen.blit(player2HpDisplay, [SCREEN_WIDTH - 50, 0])

    def running(self, goingRight):
        screen.blit(pygame.transform.flip(self.run_Animation[self.runCounter],
                                          goingRight, False, ),
                    (self.x_pos, self.y_pos))

    def attack1(self):
        screen.blit(pygame.transform.flip(
                     self.attack_Animation1[self.attack1Counter],
                     self.currentSide, False, ),
                    (self.x_pos, self.y_pos))

    def attack2(self, useProjectile):
        screen.blit(pygame.transform.flip(
                    self.attack_Animation2[self.attack2Counter],
                    self.currentSide, False, ),
                    (self.x_pos, self.y_pos))

    def takingDamage(self):
        screen.blit(pygame.transform.flip(
            self.damage_Animation[self.damageCounter],
            self.currentSide, False, ),
            (self.x_pos, self.y_pos))

    def defeat(self):
        if(self.defeatCounter == 0):
            screen.blit(pygame.transform.flip(
                self.defeat_Animation[self.defeatCounter],
                self.currentSide, False, ),
                (self.x_pos, self.y_pos))
        else:
            screen.blit(pygame.transform.flip(
                self.defeat_Animation[self.defeatCounter - 1],
                self.currentSide, False, ),
                (self.x_pos, self.y_pos))
        if self.defeatCounter < int(len(self.defeat_Animation) / 2):
            self.y_pos -= 25
            if self.currentSide:
                self.x_pos += 10
            else:
                self.x_pos -= 10

        elif self.defeatCounter >= int(len(self.defeat_Animation) / 2)\
                and self.defeatCounter < len(self.defeat_Animation) - 1:
            self.y_pos += 25
            if self.currentSide:
                self.x_pos += 10
            else:
                self.x_pos -= 10

        elif self.defeatCounter == len(self.defeat_Animation) - 1:
            changer1 = 0
            defeatCounter = len(self.defeat_Animation) - 1

    def cooldown(self):
        if(self.attack1Cooldown > 0):
            self.attack1Cooldown -= 1
        if(self.attack2Cooldown > 0):
            self.attack2Cooldown -= 1

    def resetCount(self):
        if self.runCounter > self.runTotal:
            self.runCounter = 0
        if self.attack1Counter > self.attack1Total:
            self.attack1Counter = 0
        if self.attack2Counter > self.attack2Total - 1:
            self.attack2Counter = 0
        if self.damageCounter > self.damageTotal:
            self.damageCounter = 0


class Projectile(object):
    def __init__(self, oppnent, x_pos, currentSide, attackAmount):
        self.oppnent = oppnent
        self.x_pos = x_pos
        if(not currentSide):
            self.speed = 15
        else:
            self.speed = -15
        self.maxdistance = MAX_DISTANCE
        self.currentdistance = 0
        self.attackAmount = attackAmount
        self.hitTarget = False

    def checkhit(self):
        if self.speed < 0 and self.x_pos - self.speed\
                <= self.oppnent.x_pos + 50:
            self.oppnent.damageState = True
            self.oppnent.hpCount -= 10
            self.oppnent.x_pos -= 25
            self.hitTarget = True
        if self.speed > 0 and self.x_pos + self.speed >= self.oppnent.x_pos:
            self.oppnent.damageState = True
            self.oppnent.hpCount -= 10
            self.oppnent.x_pos += 25
            self.hitTarget = True
        if self.hitTarget:
            pygame.mixer.Sound.play(hitsound)
            if self.oppnent.hpCount <= 10:
                self.oppnent.hpCount = 0
                self.oppnent.bar = False
                self.oppnent.runStateRight = False
                self.oppnent.runStateLeft = False
                self.oppnent.damageState = False
                self.oppnent.defeatState = True
                self.oppnent.y_pos += 50

    def moveProjectile(self):
        self.x_pos += self.speed
        self.currentdistance += self.speed

        self.checkhit()

# This class is primaraly used for the two players interacting,
# since it does not seem to get calling a Player in a Player Class


class Game(object):
    global ProjectileList

    def __init__(self, Player1, Player2):
        self.Player1 = Player1
        self.Player2 = Player2

    def handleProjectile(self):
        for i in ProjectileList:
            i.moveProjectile()

            if (i.currentdistance >= i.maxdistance and i.speed > 0) or\
                    i.hitTarget:
                # Moving to the right
                ProjectileList.remove(i)
            elif (i.currentdistance <= i.maxdistance * -1 and i.speed < 0) or\
                    i.hitTarget:
                # Moving to the left
                ProjectileList.remove(i)

    def flipSides(self):

        if (self.Player1.x_pos < self.Player2.x_pos):
            self.Player1.currentSide = False
            self.Player2.currentSide = True
        else:
            self.Player1.currentSide = True
            self.Player2.currentSide = False

    def Fighter1Handler(self):
        global changer1
        global attacking2
        screen.blit(bg, (0, 0))
        # Player1_HpDisplay()
        if self.Player1.bar:  # The Health Bar of player 1
            self.Player1.showHP(True)
        if self.Player1.hpCount < 2:
            self.Player1.hpCount = 0
            self.Player1.bar = False
        # Reset animations
        self.Player1.resetCount()
        if self.Player1.runStateRight:
            self.Player1.running(False)
            self.Player1.runCounter += 1
            time.sleep(0.035)
            if self.Player1.x_pos == self.Player2.x_pos - 30:
                # makes sure is cannot go off screen
                self.Player1.x_pos -= 2
        elif self.Player1.runStateLeft:
            self.Player1.running(True)
            self.Player1.runCounter += 1
            time.sleep(0.035)
            if self.Player1.x_pos == self.Player2.x_pos - 30:
                # makes sure is cannot go off screen
                self.Player1.x_pos -= 2
        elif self.Player1.damageState:

            self.Player1.takingDamage()
            self.Player1.damageCounter += 1
        elif self.Player1.attack1State:

            self.Player1.attack1()
            self.Player1.attack1Counter += 1
        elif attacking2:

            # print("We are here")
            self.Player1.attack2(True)
            self.Player1.attack2Counter += 1
        elif self.Player1.defeatState:
            self.Player1.defeat()
            self.Player1.defeatCounter += changer1
            if self.Player1.defeatCounter >=\
                    len(self.Player1.defeat_Animation) - 1:
                changer1 = 0
                self.Player1.y_pos = 455
        elif self.Player1.jumpRight:

            self.Player1.x_pos += 10
            if (not self.Player1.jumpEnd):
                self.Player1.y_pos -= 20

                self.Player1.jumpCount += 1
                if (self.Player1.jumpCount == 5):
                    self.Player1.jumpEnd = True
                    self.Player1.jumpCount = 0
            else:
                self.Player1.y_pos += fallSpeed
            if (455 < self.Player1.y_pos - fallSpeed):
                self.Player1.y_pos = 455
                self.Player1.jumpCount = 0
                self.Player1.jumpRight = False
                self.Player1.jumpEnd = False
            screen.blit(self.Player1.jumpSprite,
                        (self.Player1.x_pos, self.Player1.y_pos))
        elif self.Player1.jumpLeft:
            self.Player1.x_pos -= 10
            if (not self.Player1.jumpEnd):
                self.Player1.y_pos -= 20
                self.Player1.jumpCount += 1
                if (self.Player1.jumpCount == 5):
                    self.Player1.jumpEnd = True
                    self.Player1.jumpCount = 0
            else:
                self.Player1.y_pos += fallSpeed
            if (455 < self.Player1.y_pos + fallSpeed):
                self.Player1.y_pos = 455
                self.Player1.jumpCount = 0
                self.Player1.jumpLeft = False
                self.Player1.jumpEnd = False
            screen.blit(self.Player1.jumpSprite,
                        (self.Player1.x_pos, self.Player1.y_pos))
        else:
            # screen.blit(char, (self.Player1.x_pos, self.Player1.y_pos))
            screen.blit(pygame.transform.flip(
                self.Player1.idle_Animation[0],
                self.Player1.currentSide, False, ),
                (self.Player1.x_pos, self.Player1.y_pos))
            self.Player1.runCounter = 0
            self.Player1.attack1Counter = 0
            self.Player1.attack2Counter = 0

    def Fighter2Handler(self):

        global changer1
        # Player class: Animations
        if self.Player2.bar:  # The Health Bar of Player 2
            self.Player2.showHP(False)
        self.Player2.resetCount()
        if self.Player2.hpCount < 2:
            self.Player2.hpCount = 0
            self.Player2.bar = False
        if self.Player2.x_pos >= 850:
            self.Player2.x_pos = 845
        if self.Player2.runStateRight:
            self.Player2.running(False)
            self.Player2.runCounter += 1
        elif self.Player2.runStateLeft:
            # screen.blit(hulk[runcount], (xl, ym))
            self.Player2.running(True)
            self.Player2.runCounter += 1
        elif self.Player2.attack1State:
            self.Player2.attack1()
            self.Player2.attack1Counter += 1
        elif self.Player2.attack2State:
            self.Player2.attack2(False)
            self.Player2.attack2Counter += 1
        elif self.Player2.damageState:
            self.Player2.y_pos = 435
            self.Player2.takingDamage()
            self.Player2.hpCount -= self.Player1.attackAmount1
        elif self.Player2.defeatState:
            self.Player2.defeat()
            self.Player2.defeatCounter += changer1
            if self.Player2.defeatCounter == self.Player2.defeatTotal:
                changer1 = 0
                self.Player2.y_pos = 455
            self.Player2.y_pos += 70
            # ym += 70
        elif self.Player2.jumpRight:
            self.Player2.x_pos += 10
            if (not self.Player2.jumpEnd):
                self.Player2.y_pos -= 20

                self.Player2.jumpCount += 1
                if (self.Player2.jumpCount == 5):
                    self.Player2.jumpEnd = True
                    self.Player2.jumpCount = 0
            else:
                self.Player2.y_pos += fallSpeed
            if (455 < self.Player2.y_pos + fallSpeed):
                self.Player2.y_pos = 455
                self.Player2.jumpCount = 0
                self.Player2.jumpRight = False
                self.Player2.jumpEnd = False
            screen.blit(self.Player2.jumpSprite,
                        (self.Player2.x_pos, self.Player2.y_pos))
        elif self.Player2.jumpLeft:
            self.Player2.x_pos -= 10
            self.flipSides()
            if (not self.Player2.jumpEnd):
                self.Player2.y_pos -= 20
                self.Player2.jumpCount += 1
                if (self.Player2.jumpCount == 5):
                    self.Player2.jumpEnd = True
                    self.Player2.jumpCount = 0
            else:
                self.Player2.y_pos += fallSpeed
            if (455 < self.Player2.y_pos + fallSpeed):
                self.Player2.y_pos = 455
                self.Player2.jumpCount = 0
                self.Player2.jumpLeft = False
                self.Player2.jumpEnd = False
            screen.blit(pygame.transform.flip(
                self.Player2.jumpSprite,
                self.Player2.currentSide, False, ),
                (self.Player2.x_pos, self.Player2.y_pos))
        else:
            self.Player2.y_pos = 440
            screen.blit(pygame.transform.flip(
                self.Player2.idle_Animation[0],
                self.Player2.currentSide, False, ),
                (self.Player2.x_pos, self.Player2.y_pos))
        for i in ProjectileList:
            screen.blit(projectile, [i.x_pos, 450])
        pygame.display.update()

    def makeProjectile(self, playernumber, oppenentNumber):
        ProjectileList.append(Projectile(oppenentNumber,
                                         playernumber.x_pos,
                                         playernumber.currentSide,
                                         playernumber.attackAmount2))

# (self, PlayerNumber, idle_Animation, run_Animation, attack_Animation1,
# attack_Animation2, defeat_Animation, damage_Animation, hpBarColor):
Player1 = Player(1, 45, batman_idle, batman_run,
                 batman_attack1, batman_attack2,
                 batman_defeat, damage, BLUE, jumpBat, 0, 4, 15)
# Player1 = Player(1, 30, majin_idle, majin_run, majin_attack1, majin_attack2,
# majin_defeat, majin_damage, RED, jumpMajin, 70)
Player2 = Player(2, 70, hulk_idle, hulk_run, hulk_attack1, hulk_attack2,
                 hulk_defeat, hulkhit, GREEN, jumpHulk, 0, 10, 15)

clock = pygame.time.Clock()

# Things planned for the Player() class will be marked with a P next to them
# Controls the actions of player 1

# Main Menu of game
mainmenu = True
quitMenu = False
currentPlayer1 = "Batman"
while mainmenu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainmenu = False
            # This is hear so it just skips over the
            # running state and goes staigh to exit
            quitMenu = True

    screen.fill(WHITE)
    text = font.render(
        "Crossover Fighter: De-make ", True, BLACK)
    text6 = font.render(
        "Created by: TheRustyKnight", True, BLACK)
    text9 = font.render(
        "Player 1 can be swapped by pressing"
        " 1 or 2, current player 1 is: " +
        currentPlayer1, True, BLACK)
    text2 = font.render("How to play:", True, BLACK)
    text3 = font.render("Use A/D  and J/L to move for"
                        " player 1 and 2 respectively", True, BLACK)
    text4 = font.render("To attack, player 1 uses Q/E"
                        " and player 2 uses U/O", True, BLACK)
    text5 = font.render("The first to reduce the other"
                        " player to 0 HP is the winner", True, BLACK)
    text7 = font.render("To start, press the Spacebar", True, BLACK)
    text8 = font.render("Leap back and forth using W/S and I/K", True, BLACK)
    center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
    center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
    screen.blit(text6, [center_x - 25, center_y - 200])
    screen.blit(text, [center_x - 25, center_y - 150])
    screen.blit(text2, [center_x + 70, center_y - 80])
    screen.blit(text3, [center_x - 90, center_y])
    screen.blit(text5, [center_x - 90, center_y + 50])
    screen.blit(text4, [center_x - 90, center_y + 80])
    screen.blit(text8, [center_x - 45, center_y + 120])
    screen.blit(text7, [center_x, center_y + 150])
    screen.blit(text9, [center_x - 180, center_y - 115])

    act = pygame.key.get_pressed()
    if act[pygame.K_1]:
        Player1 = Player1 = Player(1, 45, batman_idle,
                                   batman_run,
                                   batman_attack1, batman_attack2,
                                   batman_defeat, damage,
                                   BLUE, jumpBat, 0, 4, 15)
        currentPlayer1 = "Batman"
    if act[pygame.K_2]:
        Player1 = Player(1, 30, majin_idle,
                         majin_run,
                         majin_attack1, majin_attack2,
                         majin_defeat, majin_damage,
                         RED, jumpMajin, 70, 6, 10)
        currentPlayer1 = "Majin Buu"
    if act[pygame.K_SPACE]:
        # not a repeat, this is if you will continue, not exit out.
        mainmenu = False
    pygame.display.flip()
# Main Menu end
if quitMenu:
    # This corrects for the error that would happen
    # if you where to exit during the main menu
    running = False
else:
    running = True
game = Game(Player1, Player2)
# Game methods
pygame.mixer.music.play(99)
# plays the music on start up
doAct = True
# This makes it so that players cannot act after the fight is over,
# fixing a ton of bugs
fightaction = pygame.key.get_pressed()
player1WinCount = 0
player2WinCount = 0
while running:
    clock.tick(FRAME_RATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fightCount = font.render(str(player1WinCount) + "-" +
                             str(player2WinCount), True, BLACK)
    game.flipSides()
    fightaction = pygame.key.get_pressed()
    if game.Player1.defeatState or game.Player2.defeatState:
        doAct = False
    if fightaction[pygame.K_d] and doAct:
        # player 1 moves right
        if game.Player1.runCounter <= game.Player1.runTotal:
            game.Player1.runStateRight = True
            game.Player1.y_pos = 453
            if game.Player1.runCounter > 0:
                game.Player1.x_pos += change
    elif game.Player1.x_pos <= 0:
        game.Player1.x_pos += 25
    elif game.Player1.x_pos >= (game.Player2.x_pos - 30) and\
            not game.Player1.currentSide:
        game.Player1.x_pos -= 1
        game.Player2.x_pos += 2
    elif game.Player1.x_pos <= (game.Player2.x_pos + 30) and\
            game.Player1.currentSide:
        game.Player1.x_pos += 1
        game.Player2.x_pos -= 2
    elif game.Player1.x_pos <= -5 and\
            game.Player1.x_pos >= game.Player2.x_pos - 30:
        game.Player1.x_pos -= 1
    else:
        game.Player1.runStateRight = False
    game.Fighter1Handler()
    if fightaction[pygame.K_a] and doAct:
        if game.Player1.runCounter <= game.Player1.runTotal:
            game.Player1.runStateLeft = True
            game.Player1.y_pos = 453
            if game.Player1.runCounter > 0:
                game.Player1.x_pos -= change
    elif game.Player1.x_pos <= 0:
        game.Player1.x_pos += 15
    elif game.Player1.x_pos >= game.Player2.x_pos - 30 and\
            not game.Player1.currentSide:
        game.Player1.x_pos -= 5
        game.Player2.x_pos += 5
    elif game.Player1.x_pos <= -5 and\
            game.Player1.x_pos >= game.Player2.x_pos - 30 and\
            not game.Player1.currentSide:
        game.Player1.x_pos -= 7
    else:
        game.Player1.runStateLeft = False

    game.Fighter1Handler()

    if fightaction[pygame.K_w] and doAct:
        game.Player1.jumpRight = True
    if fightaction[pygame.K_s] and doAct:
        game.Player1.jumpLeft = True
    if fightaction[pygame.K_q] and doAct:
        # game.makeProjectile(game.Player1, game.Player2)
        if(not game.Player1.currentSide):
            game.Player1.x_pos += 3
        else:
            game.Player1.x_pos -= 3
        if game.Player1.attack1Counter <= game.Player1.attack1Total:
            game.Player1.attack1State = True
            game.Player1.y_pos = 453
        if ((game.Player1.x_pos >= game.Player2.x_pos - 40 -
             game.Player1.attackExtention1 and
             not game.Player1.currentSide) or
            (game.Player1.x_pos <= game.Player2.x_pos + 40 +
                game.Player1.attackExtention1 and
                game.Player1.currentSide)) and\
                game.Player1.attack1Counter == 4:
            game.Player1.y_pos = 453
            game.Player2.damageState = True
            pygame.mixer.Sound.play(hitsound)
        else:
            game.Player2.damageState = False
        if game.Player2.hpCount <= game.Player1.attackAmount1:
            game.Player2.hpCount = 0
            game.Player2.bar = False
            game.Player2.runStateRight = False
            game.Player2.runStateLeft = False
            game.Player2.damageState = False
            game.Player2.defeatState = True
            # Player 2 loses
            game.Player2.y_pos += 50

        else:
            game.Player2.defeatState = False
    else:
        game.Player1.attack1State = False
        game.Player2.damageState = False
    if fightaction[pygame.K_e] and doAct:
        if game.Player1.attack2Counter <\
                game.Player1.attack2Total and len(ProjectileList) < 3:
            attacking2 = True
            # For some reason,
            # game.Player1.attack2State will not change to True,
            # despite being set = True. No clue why.
            if(game.Player1.attack2Counter == 2):
                game.makeProjectile(game.Player1, game.Player2)

        elif game.Player1.attack2Counter == game.Player1.attack2Total:
            attacking2 = False
    else:
        attacking2 = False
    screen.blit(fightCount, [425, 10])
    game.handleProjectile()
    game.Fighter1Handler()

    if fightaction[pygame.K_j] and\
            game.Player2.x_pos > 30 and\
            ((game.Player2.x_pos < game.Player1.x_pos and
              not game.Player2.currentSide) or
             (game.Player2.x_pos > game.Player1.x_pos and
              game.Player2.currentSide)) and doAct:
        if game.Player2.runCounter <= 5:
            # print(game.Player2.runStateLeft) Testing for errors
            game.Player2.runStateLeft = True
            # print(game.Player2.runStateLeft)
            game.Player2.x_pos -= 18
            game.Player2.y_pos = 430
        if game.Player2.x_pos <= 30:
            game.Player2.x_pos += 5

    elif game.Player1.x_pos <= -5 and\
            game.Player1.x_pos >= game.Player2.x_pos - 30 and\
            not game.Player2.currentSide:
        game.Player1.x_pos -= 1
    elif game.Player1.x_pos <= -5 and\
            game.Player1.x_pos <= game.Player2.x_pos + 30 and\
            game.Player2.currentSide:
        game.Player1.x_pos += 1

    else:
        game.Player2.runStateLeft = False
        game.Player2.y_pos = 440

    if fightaction[pygame.K_l] and\
            game.Player2.x_pos > 20 and\
            ((game.Player2.x_pos < game.Player1.x_pos and
              not game.Player2.currentSide) or
             (game.Player2.x_pos > game.Player1.x_pos and
              game.Player2.currentSide)) and\
            doAct:
        if game.Player2.runCounter <= 5:
            game.Player2.runStateRight = True
            game.Player2.x_pos += 18
            game.Player2.y_pos = 450

    elif game.Player2.x_pos <= 20:
        game.Player2.x_pos += 1
        game.Player2.runStateRight = False
        game.Player2.y_pos = 450

    elif game.Player1.x_pos <= -5 and\
            game.Player1.x_pos >= game.Player2.x_pos - 30:
        game.Player1.x_pos -= 1

    else:
        game.Player2.runStateRight = False
        game.Player2.y_pos = 440

    if fightaction[pygame.K_u] and doAct:

        if game.Player2.attack2Counter <= game.Player2.attack2Total:
            # print(game.Player2.attack2Total)
            game.Player2.attack2State = True
            # print(game.Player2.attack2State)
            if(not game.Player2.currentSide):
                game.Player2.x_pos += 10
            else:
                game.Player2.x_pos -= 10
        if game.Player2.x_pos <= 15:
            game.Player2.x_pos += 14

        if game.Player2.attack2Counter == 5:
            game.Player2.attack2State = False
            game.Player2.attack2State = 0
    else:
        game.Player2.attack2State = False
    if fightaction[pygame.K_o] and doAct:
        if game.Player2.attack1Counter <= game.Player2.attack1Total:
            game.Player2.attack1State = True
            game.Player2.y_pos = 454
            if(game.Player2.currentSide):
                game.Player2.x_pos -= 12
                if(game.Player1.x_pos >= game.Player2.x_pos + 12):
                    game.Player1.x_pos -= 10
            else:
                game.Player2.x_pos += 12
                if (game.Player1.x_pos <= game.Player2.x_pos - 12):
                    game.Player1.x_pos += 10
        if game.Player2.x_pos <= 20:
            game.Player2.x_pos += 14
        if game.Player2.attack1Counter == 1:
            game.Player2.y_pos -= 5
    else:
        game.Player2.attack1State = False
    screen.blit(fightCount, [425, 10])
    game.Fighter2Handler()
    if fightaction[pygame.K_u] and\
            game.Player1.x_pos >= game.Player2.x_pos - 40 and\
            game.Player2.attack2Counter == 2 and doAct:
        if game.Player1.damageCounter <= 24:
            game.Player1.damageState = True
            pygame.mixer.Sound.play(hitsound)
            time.sleep(0.05)
            game.Player1.hpCount -= game.Player2.attackAmount1

        if game.Player1.hpCount < 2:
            game.Player1.hpCount = 0
            game.Player1.bar = False
            game.Player1.damageState = False
            game.Player1.y_pos = 460
            game.Player1.runStateRight = False
            game.Player1.runStateLeft = False
            game.Player1.attack1State = False
            game.Player1.defeatState = True
            # Player 1 loses

        else:
            game.Player1.damageState = True
            game.Player1.defeatState = False
    elif fightaction[pygame.K_o] and\
            (game.Player1.x_pos >= game.Player2.x_pos - 40 and
             game.Player2.currentSide or
             game.Player1.x_pos <= game.Player2.x_pos + 50 and
             not game.Player2.currentSide) and\
            game.Player2.attack1Counter == 2 and\
            doAct:
        if game.Player1.damageCounter <= 24:
            game.Player1.damageState = True
            pygame.mixer.Sound.play(hitsound)
            game.Player1.hpCount -= game.Player2.attackAmount2

        if game.Player1.hpCount < 2:
            game.Player1.hpCount = 0
            game.Player1.bar = False
            game.Player1.damageState = False
            game.Player1.y_pos = 460
            game.Player1.runStateRight = False
            game.Player1.runStateLeft = False
            game.Player1.attack1State = False
            game.Player1.defeatState = True

        else:
            game.Player1.damageState = True
            game.Player1.defeatState = False
    else:
        game.Player1.damageState = False
    if fightaction[pygame.K_i] and doAct:
        game.Player2.jumpRight = True
    if fightaction[pygame.K_k] and doAct:
        game.Player2.jumpLeft = True
    screen.blit(fightCount, [425, 10])
    game.Fighter1Handler()
    game.Player1.cooldown()
    game.Player2.cooldown()

    if game.Player2.defeatState and game.Player2.defeatCounter == 9:
        winText = font.render("Player 1 wins!", True,
                              game.Player1.hpBarColor)
        restartText = font.render("Press R to replay",
                                  True, game.Player1.hpBarColor)
        screen.blit(winText, [(SCREEN_WIDTH // 2) -
                              (winText.get_width() // 2),
                              (SCREEN_HEIGHT // 2) -
                              (winText.get_height() // 2)])
        screen.blit(restartText, [(SCREEN_WIDTH // 2) -
                                  (winText.get_width() // 2),
                                  (SCREEN_HEIGHT // 2) -
                                  (winText.get_height() // 2) + 100])
        screen.blit(pygame.transform.flip(
            game.Player2.defeat_Animation[0],
            game.Player2.currentSide, False, ),
            (game.Player2.x_pos, game.Player2.y_pos))
        pygame.display.flip()

    if game.Player1.defeatState and game.Player1.defeatCounter == 7:
        winText = font.render("Player 2 wins!",
                              True, game.Player2.hpBarColor)
        restartText = font.render("Press R to replay",
                                  True, game.Player2.hpBarColor)
        screen.blit(winText, [(SCREEN_WIDTH // 2) -
                              (winText.get_width() // 2),
                              (SCREEN_HEIGHT // 2) -
                              (winText.get_height() // 2)])
        screen.blit(restartText, [(SCREEN_WIDTH // 2) -
                                  (winText.get_width() // 2),
                                  (SCREEN_HEIGHT // 2) -
                                  (winText.get_height() // 2) + 100])

        screen.blit(pygame.transform.flip(
            game.Player1.defeat_Animation[7],
            game.Player1.currentSide, False, ),
            (game.Player1.x_pos, game.Player1.y_pos))
        game.Fighter2Handler()
        pygame.display.flip()
        # Game method ends
        # Restart method begins
    if not doAct:
        # basically if one of the players has died
        if fightaction[pygame.K_r]:
            if game.Player1.defeatState:
                player2WinCount += 1
            if game.Player2.defeatState:
                player1WinCount += 1
            game.Player1.defeatState = False
            game.Player2.defeatState = False
            game.Player1.hpCount = game.Player1.maxHpCount
            game.Player2.hpCount = game.Player2.maxHpCount
            game.Player1.bar = True
            game.Player2.bar = True
            game.Player1.x_pos = 375
            game.Player2.x_pos = 410
            game.Player1.y_pos = 455
            game.Player2.y_pos = 455
            game.Player1.defeatCounter = 0
            game.Player2.defeatCounter = 0
            doAct = True
            changer1 = 1
pygame.quit()
