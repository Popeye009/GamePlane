import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
ENEMY_EVENT = pygame.USEREVENT
BULLET_EVENT = pygame.USEREVENT + 1
GAME_FRAME = 60


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):

    def __init__(self, is_alt=False):
        image_name = "plane_game/images/background.png"
        super().__init__(image_name)
        if is_alt:
            self.rect.y = -SCREEN_RECT.height

    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Hero(GameSprite):
    def __init__(self):
        super().__init__("plane_game/images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullt_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i * 20
            self.bullt_group.add(bullet)


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("plane_game/images/enemy1.png")
        self.rect.bottom = 0
        max_width = SCREEN_RECT.width - self.rect.width
        self.rect.left = random.randint(0, max_width)
        self.speed = random.randint(1, 3)

    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
           self.kill()


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("plane_game/images/bullet1.png", -3)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
