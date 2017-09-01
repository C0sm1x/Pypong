import settings, pygame

vector = pygame.math.Vector2

class Paddles(pygame.sprite.Sprite, object):
    def __init__(self):
        super(Paddles, self).__init__()
        self.image = pygame.Surface((settings.playerWidth, settings.playerHeight))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()

class Players(Paddles):
        def __init__(self, playerX, playerY):
            super(Players, self).__init__()
            self.playerX = playerX
            self.playerY = playerY
            self.rect.center = (self.playerX, self.playerY)
            self.playerVel = 0

        def movement(self):
            self.playerVel = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                self.playerVel += -5
            if keystate[pygame.K_DOWN]:
                self.playerVel += 5

            self.rect.y += self.playerVel

        def bounderies(self):
            # Top and bottom bounderies.
            if self.rect.bottom > settings.SCREEN_HEIGHT:
                self.rect.bottom = settings.SCREEN_HEIGHT
            if self.rect.top < settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT:
                self.rect.top = settings.SCREEN_HEIGHT - settings.SCREEN_HEIGHT

