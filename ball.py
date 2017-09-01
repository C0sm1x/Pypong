
import settings, pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Paddles, self).__init__()
        self.image = pygame.Surface((settings.playerWidth, settings.playerHeight))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
