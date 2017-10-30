#! /usr/bin/python2
import pygame, settings, paddles, ball, os, random

class Game:
    def __init__(self):
        pygame.mixer.pre_init(49100, -16, 1, 2048)
        pygame.mixer.init()
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.hitPaddle1Sound = pygame.mixer.Sound(os.path.join("SFX", "paddleHit.ogg"))
        self.boundBallHitSound = pygame.mixer.Sound(os.path.join("SFX", "boundPaddleHit.ogg"))
        self.lossSound = pygame.mixer.Sound(os.path.join("SFX", "loss.ogg"))

    def update(self):
        self.clock.tick(settings.FPS)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(player1)
        self.sprites.add(player2)
        self.sprites.add(ball)
        self.sprites.update()
        self.sprites.draw(self.screen)
        pygame.display.update()
        self.screen.fill(settings.BLACK)

    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False

    def line(self):
        pygame.draw.line(self.screen, settings.WHITE, [settings.SCREEN_WIDTH/2, 0], [settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT])

    def collision(self):
        self.player1andBallCollision = pygame.sprite.collide_rect(player1, ball)
        if self.player1andBallCollision == True:
            self.hitPaddle1Sound.play()
            ball.randomXDir = 1
            self.hitPaddle1Sound.set_volume(1.0)

        self.player2andBallCollision = pygame.sprite.collide_rect(player2, ball)
        if self.player2andBallCollision == True:
            self.hitPaddle1Sound.play()
            ball.randomXDir = 0
            self.hitPaddle1Sound.set_volume(1.0)

        # Ball collision

        #Left and right bounderies
        if ball.rect.left > settings.SCREEN_WIDTH:
            self.lossSound.play()
            ball.rect.x = ball.ballX
            ball.rect.y = ball.ballY
            settings.p1_score+=1
            ball.randomXDir = random.randint(0, 1)
            ball.randomYDir = random.randint(0, 1)
        if ball.rect.right < settings.SCREEN_WIDTH - settings.SCREEN_WIDTH:
            self.lossSound.play()
            ball.rect.x = ball.ballX
            ball.rect.y = ball.ballY
            settings.p2_score+=1
            ball.randomXDir = random.randint(0, 1)
            ball.randomYDir = random.randint(0, 1)
        # Top and bottom bounderies.
        if ball.rect.top <= settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT:
            ball.randomYDir = 1
            self.boundBallHitSound.play()
        if ball.rect.bottom >= settings.SCREEN_HEIGHT:
            ball.randomYDir = 0
            self.boundBallHitSound.play()

    def player2FollowsBall(self):
        if ball.rect.y < player2.rect.y + settings.playerHeight/2:
            player2.rect.y -=4
        if ball.rect.y > player2.rect.y + settings.playerHeight/2:
            player2.rect.y +=4

    def p1_Score_Display(self):
       self.font = pygame.font.SysFont("none", 50)
       self.score_Font_Render = self.font.render(str(settings.p1_score), True, settings.WHITE)
       self.screen.blit(self.score_Font_Render, (settings.SCREEN_WIDTH/3, 20))

    def p2_Score_Display(self):
       self.font = pygame.font.SysFont("none", 50)
       self.score_Font_Render = self.font.render(str(settings.p2_score), True, settings.WHITE)
       self.screen.blit(self.score_Font_Render, (settings.SCREEN_WIDTH/1.5, 20))


game = Game()
player1 = paddles.Players(settings.playerX, settings.playerY)
player2 = paddles.Players(settings.SCREEN_WIDTH - settings.playerWidth/1.5, settings.playerY)
ball = ball.Ball(settings.ballX, settings.ballY)

def gameStart():
    while game.running:
        game.events()
        game.line()
        game.collision()
        game.player2FollowsBall()
        game.p1_Score_Display()
        game.p2_Score_Display()

        player1.movement()
        player1.bounderies()
        player2.bounderies()
        ball.movement()
        game.update()

if __name__ == "__main__":
    gameStart()
