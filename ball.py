
import settings, pygame, random
vector = pygame.math.Vector2

class Ball(pygame.sprite.Sprite):
    def __init__(self, ballX, ballY):
        super(Ball, self).__init__()
        self.image = pygame.Surface((settings.ballWidth, settings.ballHeight))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
        self.ballX = ballX
        self.ballY = ballY
        self.rect.center = (self.ballX, self.ballY)
        self.randomXDir = random.randint(0, 1)
        self.randomYDir = random.randint(0, 1)
        self.ballVelocity = vector(0, 0)

    def movement(self):
        # Go in a random direction on the x axis
        if self.randomXDir == 0:
            self.ballVelocity.x = -3
        else: self.ballVelocity.x = 3
        # Go in a random direction on the y axis
        if self.randomYDir == 0:
            self.ballVelocity.y = -3
        else: self.ballVelocity.y = 3


        self.rect.x += self.ballVelocity.x
        self.rect.y += self.ballVelocity.y

    def bounderies(self):
        #Left and right bounderies
        if self.rect.x > settings.SCREEN_WIDTH:
            self.rect.x = self.ballX
            self.rect.y = self.ballY
            self.randomXDir = random.randint(0, 1)
            self.randomYDir = random.randint(0, 1)
        if self.rect.x < settings.SCREEN_WIDTH - settings.SCREEN_WIDTH:
            self.rect.x = self.ballX
            self.rect.y = self.ballY
            self.randomXDir = random.randint(0, 1)
            self.randomYDir = random.randint(0, 1)
        # Top and bottom bounderies.
        if self.rect.top < settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT:
            self.randomYDir = 1
        if self.rect.bottom > settings.SCREEN_HEIGHT:
            self.randomYDir = 0
