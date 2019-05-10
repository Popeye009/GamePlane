from plane_game.plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        pygame.time.set_timer(BULLET_EVENT, 500)

        # 背景图片的初始化
        self.creat_sprites()

    def creat_sprites(self):
        self.bg1 = BackGround()
        self.bg2 = BackGround(True)
        self.hero = Hero()
        self.bggroup = pygame.sprite.Group(self.bg1,
                                           self.bg2)
        self.herogroup = pygame.sprite.Group(self.hero)
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

    def start_game(self):
        print("开始游戏")

        while True:
            self.clock.tick(GAME_FRAME)
            self.__group_update()
            self.__check_collide()
            self.__event_handler()
            pygame.display.update()

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullt_group, self.enemy_group,
                                   True, True)
        enemy_collided_list = pygame.sprite.spritecollide(self.hero,
                                                          self.enemy_group,
                                                          True)
        if len(enemy_collided_list):
            PlaneGame.__game_over()

    def __event_handler(self):
        keys_pressed = pygame.key.get_pressed()  # 监听键盘，返回按键元组
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0
        for even in pygame.event.get():

            if even.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif even.type == ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            elif even.type == BULLET_EVENT:
                self.hero.fire()

    def __group_update(self):
        self.bggroup.update()
        self.bggroup.draw(self.screen)
        self.herogroup.update()
        self.herogroup.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero.bullt_group.update()
        self.hero.bullt_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game Over!")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
