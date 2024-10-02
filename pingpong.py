from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        
        if self.rect.y > win_height - 50 or self.rect.y < 0:
            speed_y *= -1


        if sprite.collide_rect(racket1, self) or sprite.collide_rect(racket2, self):
            speed_x *= -1
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.clock()
FPS = 60

racket1 = Player("racket.png", 30, 200, 4, 50 , 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180, 0, 0))

speed_x = 1
speed_y = 1

game = True
finish = False
while game:
    pass
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.fill(back)

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

    window.fill(back)
    racket1.update_l()
    racket2.update_r()

    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
