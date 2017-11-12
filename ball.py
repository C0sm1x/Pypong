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
        self.ballVelocity.x = 5
        self.ballVelocity.y = 5
        # Go in a random direction on the x axis
        if self.randomXDir == 0:
            self.ballVelocity.x = self.ballVelocity.x * -1
        else: self.ballVelocity.x = self.ballVelocity.x
        # Go in a random direction on the y axis
        if self.randomYDir == 0:
            self.ballVelocity.y = self.ballVelocity.y * -1
        else: self.ballVelocity.y = self.ballVelocity.y


        self.rect.x += self.ballVelocity.x
        self.rect.y += self.ballVelocity.y

