
import settings, pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, ballX, ballY):
        super(Ball, self).__init__()
        self.ballX = ballX
        self.ballY = ballY
        self.rect.center = (self.ballX, self.ballY)
        self.ballVel = 0

    def movement(self):
        self.ballVel = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.ballVel += -5
        if keystate[pygame.K_DOWN]:
            self.ballVel += 5

        self.rect.y += self.ballVel

    def bounderies(self):
        # Top and bottom bounderies.
        if self.rect.bottom > settings.SCREEN_HEIGHT:
            self.rect.bottom = settings.SCREEN_HEIGHT
        if self.rect.top < settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT:
            self.rect.top = settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT
