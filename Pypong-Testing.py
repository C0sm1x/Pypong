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
        if player.playerY > self.bottomLineStartY - Objects.PADDLE_HEIGHT:
            player.playerY = self.bottomLineStartY - Objects.PADDLE_HEIGHT + 4
        elif player.playerY + Objects.PADDLE_HEIGHT - Objects.PADDLE_HEIGHT < self.topLineStartY:
            player.playerY = Objects.PADDLE_HEIGHT - Objects.PADDLE_HEIGHT + self.topLineStartY
        if player2.player2Y > self.DISPLAY_HEIGHT - Objects.PADDLE_HEIGHT:
            player2.player2Y = self.DISPLAY_HEIGHT - Objects.PADDLE_HEIGHT
        elif player2.player2Y + Objects.PADDLE_HEIGHT - Objects.PADDLE_HEIGHT < self.DISPLAY_HEIGHT - self.DISPLAY_HEIGHT:
            player2.player2Y = self.DISPLAY_HEIGHT - self.DISPLAY_HEIGHT + Objects.PADDLE_HEIGHT - Objects.PADDLE_HEIGHT

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


class Objects(object):
    def __init__(self):
        # Paddle
        self.OBJECT_WIDTH = 20
        self.OBJECT_HEIGHT = 63
        self.objectX = game.DISPLAY_WIDTH/8
        self.objectY = game.DISPLAY_HEIGHT/2

        # Booleans
        self.isPlayer = True
        self.isPlayer2 = False
        self.isBall = True


        # objects to be drawn
        self.paddle = pygame.image.load(os.path.join("Sprites", "Pong_Paddle.png"))
        self.ball = pygame.image.load(os.path.join("Sprites", "Pong_Circle.png"))

    def draw(self,):
        if self.isPaddle and self.isPlayer2 == False:
            game.gameDisplay.blit(self.paddle, (self.playerX, self.playerY))

        if self.isPaddle and self.isPlayer2:
            game.gameDisplay.blit(self.paddle, (self.player2X, self.player2Y))

        if self.isBall:
            game.gameDisplay.blit(self.ball, (self.ballX, self.ballY))

    def movement(self):
        if self.player2Y < self.ballY:
            self.player2Y += self.player2YVelocity

        if self.player2Y > self.ballY:
            self.player2Y -= self.player2YVelocity

        if self.playerYVelocity != 0 and self.isPaddle:
            self.playerY += self.playerYVelocity


class Player(Objects):
    def __init__(self):
        # Player
        super(Player, self).__init__()
        self.playerX = self.objectX
        self.playerY = self.objectY
        self.playerYVelocity = 0


class Player2(Objects):
    def __init(self):
        # Player2
        super(Player2, self).__init__()
        self.player2X = self.objectX * 2
        self.player2Y = self.objectY * 2
        self.player2YVelocity = 6

class Ball(Objects):
    def __init__(self):
        # Ball
        super(Ball, self).__init__()
        self.BALL_WIDTH = 37
        self.BALL_HEIGHT = 37
        self.ballX = self.objectX
        self.ballXVelocity = 4
        self.ballY = self.objectY
        self.ballYVelocity = 3
        self.isBall = self.isBall
        self.randomBallDirection = random.randint(0, 3)

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







game = Game()
line = Game()
player = Player()
player2 = Player2()
ball = Ball()

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

    print(player2.player2Y)
    print(ball.ballY)

    #print(ball.ballYVelocity)
    #print(ball.ballXVelocity)
    pygame.display.update()
    game.clock.tick(game.FPS)


pygame.quit()
quit()
