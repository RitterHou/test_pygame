import pygame

total_width = 800
total_height = 600

bg_widht = 64
bg_height = 16

clock = pygame.time.Clock()


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.surf = pygame.image.load('./sprites/tilesets/decor_16x16.png').convert_alpha().subsurface(
            (0, 0, bg_widht, bg_height))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.width = 22
        self.height = 22
        self.move_speed = 10
        player_default = pygame.image.load('./sprites/characters/player.png').convert_alpha()

        player = player_default.subsurface((15, 20, self.width, self.height))
        self.player = pygame.transform.scale(player, (self.width * 2, self.height * 2))
        self.surf = self.player
        self.rect = self.surf.get_rect(center=(total_width / 2, total_height / 2))

        self.flip = False
        self.walking_players = [
            player_default.subsurface((15, 67, self.width, self.height)),
            player_default.subsurface((63, 67, self.width, self.height)),
            player_default.subsurface((111, 67, self.width, self.height)),
            player_default.subsurface((159, 67, self.width, self.height)),
            player_default.subsurface((206, 67, self.width, self.height)),
            player_default.subsurface((255, 67, self.width, self.height))
        ]
        self.walking_no = 0

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            walking_player = self.walking_players[self.walking_no]
            self.surf = pygame.transform.scale(walking_player, (self.width * 2, self.height * 2))
            self.walking_no += 1
            if self.walking_no == 5:
                self.walking_no = 0

        if keys[pygame.K_LEFT]:
            self.flip = True
            self.rect.move_ip((-self.move_speed, 0))
        elif keys[pygame.K_RIGHT]:
            self.flip = False
            self.rect.move_ip((self.move_speed, 0))
        elif keys[pygame.K_UP]:
            self.rect.move_ip((0, -self.move_speed))
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip((0, self.move_speed))
        else:
            self.surf = self.player

        self.surf = pygame.transform.flip(self.surf, self.flip, False)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > total_width:
            self.rect.right = total_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > total_height:
            self.rect.bottom = total_height


def main():
    pygame.init()
    pygame.display.set_caption('不得了啦的游戏')
    win = pygame.display.set_mode((total_width, total_height))

    bg = Background()
    player = Player()
    all_sprites = [player]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        for i in range(0, total_width, bg_widht):
            for j in range(0, total_height, bg_height):
                win.blit(bg.surf, (i, j))

        keys = pygame.key.get_pressed()
        player.update(keys)

        for sprite in all_sprites:
            win.blit(sprite.surf, sprite.rect)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
