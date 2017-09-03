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


game = Game()
player1 = paddles.Players(settings.playerX, settings.playerY)
player2 = paddles.Players(settings.SCREEN_WIDTH - settings.playerWidth/1.5, settings.playerY)
ball = ball.Ball(settings.ballX, settings.ballY)

def gameStart():
    while game.running:
        game.events()

        player1.movement()
        player1.bounderies()
        ball.movement()
        ball.bounderies()
        game.update()

if __name__ == "__main__":
    gameStart()
