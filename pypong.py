#! /usr/bin/python2
import pygame, settings, paddles, ball

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()

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
            ball.randomXDir = 1
        self.player2andBallCollision = pygame.sprite.collide_rect(player2, ball)
        if self.player2andBallCollision == True:
            ball.randomXDir = 0

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
        ball.bounderies()
        game.update()

if __name__ == "__main__":
    gameStart()
