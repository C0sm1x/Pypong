
import settings, pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, ballX, ballY):
        super(Ball, self).__init__()
        self.image = pygame.Surface((settings.ballWidth, settings.ballHeight))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
        self.ballX = ballX
        self.ballY = ballY
        self.rect.center = (self.ballX, self.ballY)
        self.ballVel = 0

    def movement(self):
        self.ballVel = 0
        randomYDir = random.randint(0, 1)
        if randomYDir == 0:
            self.ballVel += -5
        else: self.ballVel += 5
        randomXDir = random.randint(0, 1)
        if randomXDir == 0:
            self.ballVel += -5
        else: self.ballVel += 5


        self.rect.y += self.ballVel
        self.rect.x += self.ballVel

    def bounderies(self):
        # Top and bottom bounderies.
        if self.rect.bottom > settings.SCREEN_HEIGHT:
            self.rect.bottom = settings.SCREEN_HEIGHT
        if self.rect.top < settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT:
            self.rect.top = settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT
