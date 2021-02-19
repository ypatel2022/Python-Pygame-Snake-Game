# Final Culminating ICS20
# Yax
# Snake game

import pygame
from random import randint
from time import sleep
pygame.init()

# varibles
# colors
red       = (255,  0,  0)
darkred   = (175,  0,  0)
green     = (  0,255,  0)
midgreen  = (  0,180,  0)
darkgreen = (  0,160,  0)
black     = (  0,  0,  0)
blue      = (  0,115,255)
midblue   = (  0, 60,255)
darkblue  = (  0, 40,255)
orange    = (255,153,  0)
yellow    = (255,217,  0)
pink      = (255,  0,102)
white     = (255,255,255)
# default colors for player 2
snakeBodyColor2 = yellow
snakeHeadColor2 = orange
foodColor2 = pink
# win size
screenWidth, screenHeight = 400, 400
# starting length of snake
length = 1
length2 = 1
# start pos of snake
x = 100
y = 100
x2 = 300
y2 = 300
# width of snake and food
w = 10
# for making snake move - in the start the snake is idle
xChange = 0
yChange = 0
xChange2 = 0
yChange2 = 0
# delay between each loop
delay = 80
# used for main loops
run = True
intro = True
# used for making snake longer
snakeList = []
snakeList2 = []
# declaring fonts
titleFont = pygame.font.Font('freesansbold.ttf', 60)
titleFont2 = pygame.font.Font('freesansbold.ttf', 32)
titleFont3 = pygame.font.Font('freesansbold.ttf', 15)
titleFont4 = pygame.font.Font('freesansbold.ttf', 20)
fontButtonColor = black
# for keeping track of highscore
highscore = 0
change = True # for counteracting a glitch with teleporting
change2 = True
teleportation = False
nosuicide = False
twoplayers = False
bTheme = False
wTheme = True
# creates window
win = pygame.display.set_mode((screenWidth, screenHeight))

# themes
def WHITE_THEME():
    global bg, snakeHeadColor, snakeBodyColor, foodColor, fontColor, buttonColor, buttonOffColor, buttonOnColor, lineColor
    bg = white
    snakeHeadColor = (0, 40, 255)
    snakeBodyColor = blue
    foodColor = green
    fontColor = black
    buttonColor = darkblue
    buttonOffColor = blue
    buttonOnColor = midblue
    lineColor = black
def BLACK_THEME():
    global bg, snakeHeadColor, snakeBodyColor, foodColor, fontColor, buttonColor, buttonOffColor, buttonOnColor, lineColor
    bg = black
    snakeHeadColor = darkgreen
    snakeBodyColor = green
    foodColor = red
    fontColor = green
    buttonColor = darkgreen
    buttonOffColor = green
    buttonOnColor = midgreen
    lineColor = white
# game uses white theme by default
WHITE_THEME()

# used for making snake longer and making sqaures behind it follow
def snakeL(snakeList): # for snake 1
    for xPos in snakeList:
        pygame.draw.rect(win, snakeBodyColor, [xPos[0], xPos[1], w, w])
def snakeL2(snakeList2): # for snake 2
    for xPos2 in snakeList2:
        pygame.draw.rect(win, snakeBodyColor2, [xPos2[0], xPos2[1], w, w])

# for displaying game over message
def gameover():
    # making these variable global because they're needed outside the function
    global x, y, xChange, yChange, length, snakeList, snakeHead, x2, y2, xChange2, yChange2, length2, snakeList2, snakeHead2, run, intro, highscore

    #fills window with color so the new shapes can be displayed with new positions
    win.fill(bg)

    # when game ends the highest score is stored in a variable
    if length > length2:
        if length > highscore:
            highscore = length
    else:
        if length2 > highscore:
            highscore = length2

    # what messages to display and varibles to set if twoplayers is off
    if twoplayers != True:
        length1 = 'Score: ' + str(length - 1)
        text = titleFont2.render('Game Over!', True, fontColor)
        text2 = titleFont2.render(length1, True, fontColor)
        text3 = titleFont3.render('Press Space to play again or press Backspace to exit', True, fontColor)
        win.blit(text, (110, 170))
        win.blit(text2, (140, 210))
        win.blit(text3, (20, 250))
        pygame.display.update()

        # loop for checking which key was pressed
        run2 = True
        while run2:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_SPACE]: # if space is pressed then the game will start again
                    run2 = False
                    break
                elif keys[pygame.K_BACKSPACE] or keys[pygame.K_ESCAPE]: # if esc or backspace is pressed it will send user to main menu
                    run = False
                    intro = True
                    run2 = False
                    break
                elif event.type == pygame.QUIT: # is quit is pressed then program will close
                    pygame.quit()
                    quit()
                # resets variables
                x = 100
                y = 100
                xChange = 0
                yChange = 0
                length = 1
                snakeList = []
                snakeHead = []
    # what messages to display and varibles to set if twoplayers is on
    else:
        # sets scores
        p1Score = str(length - 1)
        p2Score = str(length2 - 1)
        text = titleFont2.render('Game Over!', True, fontColor)

        # displays message according to score of players
        if length > length2:
            text2 = titleFont4.render('Player 1 WINS! | Score: ' + p1Score, True, fontColor)
            win.blit(text2, (70, 215))
        elif length < length2:
            text2 = titleFont4.render('Player 2 WINS! | Score: ' + p2Score, True, fontColor)
            win.blit(text2, (70, 215))
        else:
            text2 = titleFont2.render('TIE!', True, fontColor)
            win.blit(text2, (170, 210))
        text3 = titleFont3.render('Press Space to play again or press Backspace to exit', True, fontColor)
        # displays text
        win.blit(text, (110, 170))
        win.blit(text3, (20, 250))
        pygame.display.update()
        # loop for checking which key was pressed
        run2 = True
        while run2:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_SPACE]: # if space is pressed then the game will start again
                    run2 = False
                    break
                elif keys[pygame.K_BACKSPACE] or keys[pygame.K_ESCAPE]: # if esc or backspace is pressed it will send user to main menu
                    run = False
                    intro = True
                    run2 = False
                    break
                elif event.type == pygame.QUIT: # is quit is pressed then program will close
                    pygame.quit()
                    quit()
                # resets variables
                x = 100
                y = 100
                xChange = 0
                yChange = 0
                length = 1
                snakeList = []
                snakeHead = []
                x2 = 300
                y2 = 300
                xChange2 = 0
                yChange2 = 0
                length2 = 1
                snakeList2 = []
                snakeHead2 = []

# for choosing new food position and preventing it from spawning on snake
def foodPOS():
    # global food positions
    global foodX, foodY
    foods = True
    while foods:
        # random positions for food
        foodX = randint(0, (screenWidth - 10) / 10)*10
        foodY = randint(0, (screenHeight - 10) / 10)*10
        if twoplayers == True: # if two players is turned on
            for positions in snakeList: # checks every position of snake body
                # checks if food position is somewhere its not supposed to be,
                # and if it is there then it will choose new position for food
                # by restarting the while loop
                if positions == [foodX, foodY] or (foodX, foodY) == (x, y) or (foodX, foodY) == (x2, y2):
                    foods = True
                    loop2 = False
                    break
                else:
                    foods = False
                    loop2 = True
            if loop2 == True:
                for positions in snakeList2:
                    if positions == [foodX, foodY] or (foodX, foodY) == (x, y) or (foodX, foodY) == (x2, y2):
                        foods = True
                        break
                    else:
                        foods = False
        # does the same thing as if but if two players if off
        else:
            for positions in snakeList:
                if positions == [foodX, foodY] or (foodX, foodY) == (x, y):
                    foods = True
                    break
                else:
                    foods = False

def foodPOS2():
    # global food positions
    global foodX2, foodY2
    foods = True
    while foods:
        # random positions for food
        foodX2 = randint(0, (screenWidth - 10) / 10)*10
        foodY2 = randint(0, (screenHeight - 10) / 10)*10
        loop2 = True
        for positions in snakeList2: # checks every position of snake body
            # checks if food position is somewhere its not supposed to be,
            # and if it is there then it will choose new position for food
            # by restarting the while loop
            if positions == [foodX2, foodY2] or (foodX2, foodY2) == (x2, y2) or (foodX2, foodY2) == (x, y):
                foods = True
                loop2 = False
                break
            else:
                foods = False
                loop2 = True
        if loop2 == True:
            for positions in snakeList:
                if positions == [foodX2, foodY2] or (foodX2, foodY2) == (x2, y2) or (foodX2, foodY2) == (x, y):
                    foods = True
                    break
                else:
                    foods = False

### buttons ###
# buttons and their locations with text
def playbutton(color):
    play = pygame.draw.rect(win, color, (160, 100, 80, 40))
    global playText
    playText = titleFont2.render('Play', True, fontButtonColor)
    win.blit(playText, (165, 103))
def whitebutton(color):
    whiteTheme = pygame.draw.rect(win, color, (50, 320, 80, 20))
    global whiteText
    whiteText = titleFont3.render('White', True, fontButtonColor)
    win.blit(whiteText, (69, 322))
def blackbutton(color):
    blackTheme = pygame.draw.rect(win, color, (50, 341, 80, 20))
    global blackText
    blackText = titleFont3.render('Black', True, fontButtonColor)
    win.blit(blackText, (69, 343))
def resetbutton(color):
    reset = pygame.draw.rect(win, color, (270, 320, 80, 40))
    global resetText
    resetText = titleFont4.render('Reset', True, fontButtonColor)
    win.blit(resetText, (283, 330))


def instructbutton(color):
    instructions = pygame.draw.rect(win, color, (160, 320, 80, 40))
    global infoText
    infoText = titleFont2.render('INFO', True, fontButtonColor)
    win.blit(infoText, (162, 325))

def twoplayerbutton(color):
    twoplayer = pygame.draw.rect(win, color, (50, 250, 80, 40))
    global twoplayerText
    twoplayerText = titleFont3.render('2 Players', True, fontButtonColor)
    win.blit(twoplayerText, (57, 263))
def nokillbutton(color):
    nokill = pygame.draw.rect(win, color, (160, 250, 80, 40))
    global nokillText, nokillText2
    nokillText = titleFont3.render('No', True, fontButtonColor)
    nokillText2 = titleFont3.render('Suicide', True, fontButtonColor)
    win.blit(nokillText, (190, 255))
    win.blit(nokillText2, (170, 270))
def teleportbutton(color):
    teleport = pygame.draw.rect(win, color, (270, 250, 80, 40))
    global teleportText
    teleportText = titleFont3.render('Teleport', True, fontButtonColor)
    win.blit(teleportText, (279, 263))





def INTRO():
    global run, intro, teleportation, nosuicide, twoplayers, wTheme, bTheme, event
    while intro:
        pygame.display.set_caption("Snake Game")
        text = titleFont.render('Snake Game', True, fontColor)

        p1 = titleFont3.render('P1', True, fontColor)
        p2 = titleFont3.render('P2', True, fontColor)

        win.fill(bg)

        # preview of snakes in main menu
        pygame.draw.rect(win, foodColor, (70, 120, w, w))
        pygame.draw.rect(win, snakeHeadColor, (70, 150, w, w))
        pygame.draw.rect(win, snakeBodyColor, (70, 160, w, w))
        pygame.draw.rect(win, snakeBodyColor, (70, 170, w, w))
        pygame.draw.rect(win, snakeBodyColor, (70, 180, w, w))
        pygame.draw.rect(win, snakeBodyColor, (70, 190, w, w))
        pygame.draw.rect(win, snakeBodyColor, (60, 190, w, w))
        win.blit(p1, (65, 100))

        # preveiw of 2nd snake when two players is turned on
        if twoplayers == True:
            pygame.draw.rect(win, foodColor2, (310, 120, w, w))
            pygame.draw.rect(win, snakeHeadColor2, (310, 150, w, w))
            pygame.draw.rect(win, snakeBodyColor2, (310, 160, w, w))
            pygame.draw.rect(win, snakeBodyColor2, (310, 170, w, w))
            pygame.draw.rect(win, snakeBodyColor2, (310, 180, w, w))
            pygame.draw.rect(win, snakeBodyColor2, (310, 190, w, w))
            pygame.draw.rect(win, snakeBodyColor2, (300, 190, w, w))
            win.blit(p2, (305, 100))

        # displays highscore in main menu
        highscoreText = titleFont3.render('Highscore: ' + str(highscore), True, fontColor)
        win.blit(highscoreText, (155, 180))

        # the program will close if quit is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # button will be a different color if it is on
        playbutton(buttonOffColor)
        resetbutton(buttonOffColor)
        instructbutton(buttonOffColor)

        # buttons will be different color if turned on
        if wTheme == True:
            whitebutton(buttonOnColor)
        else:
            whitebutton(buttonOffColor)
        if bTheme == True:
            blackbutton(buttonOnColor)
        else:
            blackbutton(buttonOffColor)
        if twoplayers == True:
            twoplayerbutton(buttonOnColor)
        else:
            twoplayerbutton(buttonOffColor)
        if nosuicide == True:
            nokillbutton(buttonOnColor)
        else:
            nokillbutton(buttonOffColor)
        if teleportation == True:
            teleportbutton(buttonOnColor)
        else:
            teleportbutton(buttonOffColor)

        # mouse position needed for buttons
        mouse = pygame.mouse.get_pos()

        # what to do if each button is pressed
        if 160 + 80 > mouse[0] > 160 and 100 + 40 > mouse[1] > 100: # play button - starts game loop when pressed
            playbutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = True
                intro = False
                break

        elif 50 + 80 > mouse[0] > 50 and 320 + 20 > mouse[1] > 320: # light theme - changes theme colors to white
            whitebutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                WHITE_THEME()
                wTheme = True
                bTheme = False

        elif 50 + 80 > mouse[0] > 50 and 341 + 20 > mouse[1] > 341: # dark theme - changes theme colors to black
            blackbutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                BLACK_THEME()
                bTheme = True
                wTheme = False

        ##### insert instruction code here
        elif 160 + 80 > mouse[0] > 160 and 320 + 40 > mouse[1] > 320: # instructions - displays the instructions of the game
            instructbutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Documents\PythonProjects\snakeGame\instructionText.png
                image = pygame.image.load(".\\instructionText.png")
                win.blit(image,(2,2))
                pygame.display.update()

                info = True
                while info:
                    keys = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif keys[pygame.K_BACKSPACE] or keys[pygame.K_ESCAPE]:
                            info = False
                            break
        
        elif 270 + 80 > mouse[0] > 270 and 320 + 40 > mouse[1] > 320: # reset - to reset buttons that are on
            resetbutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                teleportation = False
                nosuicide = False
                twoplayers = False

        elif 50 + 80 > mouse[0] > 50 and 250 + 40 > mouse[1] > 250: # 2 player button - turns on 2 player mode
            twoplayerbutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                twoplayers = True

        elif 160 + 80 > mouse[0] > 160 and 250 + 40 > mouse[1] > 250: # no kill button - turns on mode where snake cant kill itslef
            nokillbutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                nosuicide = True
                teleportation = False

        elif 270 + 80 > mouse[0] > 270 and 250 + 40 > mouse[1] > 250: # teleport button - turns on mode where snake can teleport
            teleportbutton(buttonColor)
            if event.type == pygame.MOUSEBUTTONDOWN:
                teleportation = True
                nosuicide = False
        

        # displays text
        win.blit(text, (10, 20))

        pygame.display.update()

# for choosing new food position
# this is different from the food function because
# the food function checks if the food is in the body of the snake
# and at the start there is no body of the snake
while True:
    foodX = randint(0, (screenWidth - 10) / 10)*10
    foodY = randint(0, (screenHeight - 10) / 10)*10
    if foodX != x and foodY != y:
        break
while True:
    foodX2 = randint(0, (screenWidth - 10) / 10)*10
    foodY2 = randint(0, (screenHeight - 10) / 10)*10
    if foodX2 != x2 and foodY2 != y2:
        break

def grid():
    for X in range(0, screenWidth, w):
        for Y in range(0, screenHeight, w):
            pygame.draw.line(win, lineColor, (X, Y), (X+screenWidth, Y), 1)
    for X in range(0, screenWidth, w):
        for Y in range(0, screenHeight, w):
            pygame.draw.line(win, lineColor, (X, Y), (X, Y+screenHeight), 1)




# main loop
while True:
    # main menu loop
    INTRO()

    # game loop
    while run:
        pygame.time.delay(delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # sets variable that represents every key that is pressed
        keys = pygame.key.get_pressed()

        # this the part that does the teleportation
        if teleportation == True:
            if x < 0:
                x += screenWidth
                change = False
            elif x > screenWidth - 10:
                x -= screenWidth
                change = False
            if y < 0:
                y += screenHeight
                change = False
            elif y > screenHeight - 10:
                y -= screenHeight
                change = False

        # what to do if arrow is pressed
        if change != False: # for teleportation issue
            if keys[pygame.K_LEFT] and x > - 1 and xChange != 10:
                xChange = -10
                yChange = 0
            elif keys[pygame.K_RIGHT] and x < screenWidth + 1 and xChange != -10:
                xChange = 10
                yChange = 0
            elif keys[pygame.K_UP] and y > - 1 and yChange != 10:
                xChange = 0
                yChange = -10
            elif keys[pygame.K_DOWN] and y < screenWidth + 1 and yChange != -10:
                xChange = 0
                yChange = 10

        # for fixing issue with teleportation
        if change != False:
            x += xChange # what to change snake pos by each time
            y += yChange
        change = True

        win.fill(bg)

        # for making snake longer and making tail follow same path as head of snake
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        if len(snakeList) > length:
            del snakeList[0]

        # for when the snake touches itself
        if nosuicide != True:
            for xyPos in snakeList[:-1]:
                if xyPos == snakeHead:
                    gameover()

        # draws food, snake and snake segments + line at top to see where screen ends
        snakeL(snakeList)
        pygame.draw.line(win, black, (0, 0), (screenWidth, 0), 1)
        snake = pygame.draw.rect(win, snakeHeadColor, (x, y, w, w))
        food = pygame.draw.rect(win, foodColor, (foodX, foodY, w, w))
        # grid()

        # shows instructions when snake is not moving
        if xChange == 0 and yChange == 0 and twoplayers != True:
            moveText = titleFont3.render('Press arrow keys to move', True, fontColor)
            win.blit(moveText, (110, 190))

        # what to do if food is eaten
        if x == foodX and y == foodY:
            foodPOS()
            length += 1

        # setting caption for displaying score
        if twoplayers != True:
            pygame.display.set_caption("Snake Game | Score : " + str(length - 1))

        # what to do if snake hits wall if teleportation is off
        if teleportation != True:
            if x < -1 or x > screenWidth - w + 1 or y < -1 or y > screenWidth - w + 1:
                gameover()


        if twoplayers == True:
            # setting caption for displaying score
            pygame.display.set_caption("Snake Game | P1 Score : " + str(length - 1) + " | P2 Score : " + str(length2 - 1))

            # what to do if teleportation is turned on
            if teleportation == True:
                if x2 < 0:
                    x2 += screenWidth
                    change2 = False
                elif x2 > screenWidth - 10:
                    x2 -= screenWidth
                    change2 = False
                if y2 < 0:
                    y2 += screenHeight
                    change2 = False
                elif y2 > screenHeight - 10:
                    y2 -= screenHeight
                    change2 = False

            if change2 != False: # for teleportation issue
                # turn buttons
                if keys[pygame.K_a] and x2 > - 1 and xChange2 != 10:
                    xChange2 = -10
                    yChange2 = 0
                elif keys[pygame.K_d] and x2 < screenWidth + 1 and xChange2 != -10:
                    xChange2 = 10
                    yChange2 = 0
                elif keys[pygame.K_w] and y2 > - 1 and yChange2 != 10:
                    xChange2 = 0
                    yChange2 = -10
                elif keys[pygame.K_s] and y2 < screenWidth + 1 and yChange2 != -10:
                    xChange2 = 0
                    yChange2 = 10

            if change2 != False: # for teleportation issue
                # changes x and y coords of 2nd snake
                x2 += xChange2
                y2 += yChange2
            change2 = True

            # for making snake longer and making tail follow same path as head of snake
            snakeHead2 = []
            snakeHead2.append(x2)
            snakeHead2.append(y2)
            snakeList2.append(snakeHead2)
            if len(snakeList2) > length2:
                del snakeList2[0]

            # for when the snake touches itself
            if nosuicide != True:
                for xyPos in snakeList2[:-1]:
                    if xyPos == snakeHead2:
                        gameover()

            # draws food and snake + snake segments
            snakeL2(snakeList2)
            snake2 = pygame.draw.rect(win, snakeHeadColor2, (x2, y2, w, w))
            food2 = pygame.draw.rect(win, foodColor2, (foodX2, foodY2, w, w))

            # displays instructions to each player
            if xChange2 == 0 and yChange2 == 0 or xChange == 0 and yChange == 0:
                moveText = titleFont3.render('P1 Press arrow keys to move', True, fontColor)
                moveText2 = titleFont3.render('P2 Press W A S D to move', True, fontColor)
                win.blit(moveText, (110, 190))
                win.blit(moveText2, (120, 210))

            # when the snake touches food
            if x2 == foodX2 and y2 == foodY2:
                foodPOS2()
                length2 += 1

            # ends game if teleport is off
            if teleportation != True:
                if x2 < -1 or x2 > screenWidth - w + 1 or y2 < -1 or y2 > screenWidth - w + 1:
                    gameover()

            # for when one snake touches the other
            for xyPos in snakeList:
                if xyPos == [x2, y2]:
                    gameover()

            # for when one snake touches the other
            for xyPos in snakeList2:
                if xyPos == [x, y] or (x, y) == (x2, y2) or (x, y) == (foodX2, foodY2) or (x2, y2) == (foodX, foodY):
                    gameover()


        pygame.display.update()
