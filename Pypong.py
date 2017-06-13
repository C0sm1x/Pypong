#!/usr/bin/python
import pygame
import random
import os

class Game:
    def __init__(self):
        pygame.init()
        self.DISPLAY_WIDTH = 640
        self.DISPLAY_HEIGHT = 480
        self.gameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        # Window title
        pygame.display.set_caption("Pypong")
        self.clock = pygame.time.Clock()

        #colors

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.FPS = 60
        self.playerScore = 0
        self.player2Score = 0
        self.font = pygame.font.SysFont("arial", 80)
        self.playerScorePosition = (self.DISPLAY_WIDTH/3, self.DISPLAY_HEIGHT/6)
        self.player2ScorePosition = (self.DISPLAY_WIDTH/3 * 2,  self.DISPLAY_HEIGHT/6)

        self.running = True

        self.topLineStartX = 0
        self.topLineEndX = self.DISPLAY_WIDTH
        self.topLineStartY = 40
        self.topLineEndY = 40

        self.bottomLineStartX = self.topLineStartX
        self.bottomLineEndX = self.topLineEndX
        self.bottomLineStartY = self.DISPLAY_HEIGHT - self.topLineStartY
        self.bottomLineEndY = self.bottomLineStartY
        self.PlayerOneScores = 0


    def collision(self):
        if player.playerX < ball.ballX + ball.BALL_WIDTH and player.playerX + player.PADDLE_WIDTH > ball.ballX and player.playerY < ball.ballY + ball.BALL_HEIGHT and player.playerY + player.PADDLE_HEIGHT > ball.ballY:
            ball.ballXVelocity = ball.ballXVelocity * -1
            # ball.ballYVelocity = ball.ballYVelocity * -1
        if player2.player2X < ball.ballX + ball.BALL_WIDTH and player2.player2X + player2.PADDLE_WIDTH > ball.ballX and player2.player2Y < ball.ballY + ball.BALL_HEIGHT and player2.player2Y + player2.PADDLE_HEIGHT > ball.ballY:
            ball.ballXVelocity = ball.ballXVelocity * -1

        if ball.ballY + ball.BALL_HEIGHT > self.DISPLAY_HEIGHT - self.topLineStartY:
            ball.ballYVelocity = ball.ballYVelocity * -1
        if ball.ballY + ball.BALL_HEIGHT - ball.BALL_HEIGHT < self.topLineStartY:
            ball.ballYVelocity = ball.ballYVelocity * -1

    def draw(self):
        pygame.draw.line(self.gameDisplay, self.WHITE, (self.DISPLAY_WIDTH/2 + ball.BALL_WIDTH/2, self.DISPLAY_HEIGHT - self.DISPLAY_HEIGHT + 40), (self.DISPLAY_WIDTH/2 + ball.BALL_WIDTH/2, self.DISPLAY_HEIGHT - 40))

        pygame.draw.line(self.gameDisplay, self.WHITE, (self.topLineStartX, self.topLineStartY), (self.topLineEndX, self.topLineEndY))

        pygame.draw.line(self.gameDisplay, self.WHITE, (self.bottomLineStartX, self.bottomLineStartY), (self.bottomLineEndX, self.bottomLineEndY))

        # pygame.draw.line(self.gameDisplay, self.WHITE, (), ())


    def bounderies(self):
        if player.playerY + player.PADDLE_HEIGHT >= self.bottomLineStartY:
            player.playerY = self.bottomLineStartY - player.PADDLE_HEIGHT + 4
        elif player.playerY + player.PADDLE_HEIGHT - player.PADDLE_HEIGHT <= self.topLineStartY:
            player.playerY = player.PADDLE_HEIGHT - player.PADDLE_HEIGHT + self.topLineStartY

        if player2.player2Y + player.PADDLE_HEIGHT >= self.bottomLineStartY:
            player2.player2Y = self.bottomLineStartY - player.PADDLE_HEIGHT - 2
        elif player2.player2Y + player.PADDLE_HEIGHT - player.PADDLE_HEIGHT <= self.topLineStartY:
            player2.player2Y = player.PADDLE_HEIGHT - player.PADDLE_HEIGHT + self.topLineStartY

        if ball.ballX - ball.BALL_WIDTH > self.DISPLAY_WIDTH:
            self.playerScore = self.playerScore + 1
            ball.ballX = self.DISPLAY_WIDTH/2
            ball.ballY = self.DISPLAY_HEIGHT/2
            ball.randomBallDirection = random.randint(0, 3)

        if ball.ballX + ball.BALL_WIDTH < 0:
            self.player2Score = self.player2Score + 1
            ball.ballX = self.DISPLAY_WIDTH/2
            ball.ballY = self.DISPLAY_HEIGHT/2
            ball.randomBallDirection = random.randint(0, 3)

    def score(self):
        if ball.ballX < self.DISPLAY_WIDTH/2:
            self.PlayerOneScores = random.randint(0, 1)

            if self.PlayerOneScores == 1:
                player2.player2YVelocity = 0
            elif self.PlayerOneScores == 0:
                player2.player2YVelocity = 6

        print(self.PlayerOneScores)

        self.playerScoreDisplay = self.font.render(str(self.playerScore), True, self.WHITE)
        self.player2ScoreDisplay = self.font.render(str(self.player2Score), True, self.WHITE)
        self.gameDisplay.blit(self.playerScoreDisplay, (self.playerScorePosition))
        self.gameDisplay.blit(self.player2ScoreDisplay, (self.player2ScorePosition))

    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False

            # Keyboard events and movements
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_UP:
                    player.playerYVelocity = -6

                if self.event.key == pygame.K_DOWN:
                    player.playerYVelocity = 6


            if self.event.type == pygame.KEYUP:
                if self.event.key == pygame.K_UP:
                    player.playerYVelocity = 0

                if self.event.key == pygame.K_DOWN:
                    player.playerYVelocity = 0


class Objects:
    def __init__(self, OBJECT_WIDTH, OBJECT_HEIGHT, objectX, objectY, isBall, isPaddle, isPlayer2):
        # Paddle
        self.OBJECT_WIDTH = OBJECT_WIDTH
        self.OBJECT_HEIGHT = OBJECT_HEIGHT
        self.objectX = objectX
        self.objectY = objectY
        self.PADDLE_HEIGHT = self.OBJECT_HEIGHT
        self.PADDLE_WIDTH = self.OBJECT_WIDTH
        self.isPaddle = isPaddle
        self.isPlayer2 = isPlayer2

        # Ball
        self.BALL_WIDTH = OBJECT_WIDTH
        self.BALL_HEIGHT = OBJECT_HEIGHT
        self.ballX = objectX
        self.ballXVelocity = 4
        self.ballY = objectY
        self.ballYVelocity = 3
        self.isBall = isBall
        self.randomBallDirection = random.randint(0, 3)

        self.ball = pygame.image.load(os.path.join("Sprites", "Pong_Circle.png"))

        # Player
        self.playerX = self.objectX
        self.playerY = self.objectY
        self.playerYVelocity = 0

        # Player2
        self.player2X = self.objectX
        self.player2Y = self.objectY
        self.player2YVelocity = 6
        self.paddle = pygame.image.load(os.path.join("Sprites", "Pong_Paddle.png"))

    def randomBallDir(self):
        if self.randomBallDirection == 0:
            self.ballX -= self.ballXVelocity
            self.ballY -= self.ballYVelocity
        elif self.randomBallDirection == 1:
            self.ballX -= self.ballXVelocity
            self.ballY += self.ballYVelocity
        elif self.randomBallDirection == 2:
            self.ballX += self.ballXVelocity
            self.ballY -= self.ballYVelocity
        elif self.randomBallDirection == 3:
            self.ballX += self.ballXVelocity
            self.ballY -= self.ballYVelocity

    def draw(self,):
        if self.isPaddle and self.isPlayer2 == False:
            game.gameDisplay.blit(self.paddle, (self.playerX, self.playerY))

        if self.isPaddle and self.isPlayer2:
            game.gameDisplay.blit(self.paddle, (self.player2X, self.player2Y))

        if self.isBall:
            game.gameDisplay.blit(self.ball, (self.ballX, self.ballY))

    def movement(self):
        if self.player2Y + self.PADDLE_HEIGHT < ball.ballY + self.BALL_HEIGHT:
            self.player2Y += self.player2YVelocity

        if self.player2Y - self.PADDLE_HEIGHT > ball.ballY - self.BALL_HEIGHT:
            self.player2Y -= self.player2YVelocity

        if self.playerYVelocity != 0 and self.isPaddle:
            self.playerY += self.playerYVelocity



game = Game()
line = Game()
player = Objects(20, 63, game.DISPLAY_WIDTH/8, game.DISPLAY_HEIGHT/2, False, True, False)
player2 = Objects(20, 63, game.DISPLAY_WIDTH - game.DISPLAY_WIDTH/8, game.DISPLAY_HEIGHT/2, False, True, True)
ball = Objects(37, 37, game.DISPLAY_WIDTH/2, game.DISPLAY_HEIGHT/2,  True, False, False)

while game.running:

    game.gameDisplay.fill(game.BLACK)
    game.bounderies()
    game.events()
    player.movement()
    player2.movement()
    player.draw()
    player2.draw()
    ball.draw()
    ball.randomBallDir()
    game.collision()
    game.score()
    line.draw()


    #print(ball.ballYVelocity)
    #print(ball.ballXVelocity)
    pygame.display.update()
    game.clock.tick(game.FPS)


pygame.quit()
quit()
