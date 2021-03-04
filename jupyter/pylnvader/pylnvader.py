import pygame
import random

white = (255, 255, 255)
black = (0, 0, 0)

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey(black)

    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Collision(x1, y1, x2, y2):
    if (x1 > x2 - 30) and(x1 < x2 + 30) and (y1 > y2 - 30) and (y1 < y2 + 30):
        True
    else:
        return False

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pylnvaders')
pygame.key.set_repeat(1, 1)
font = pygame.font.Font('malgun.ttf', 36)
backdrop = pygame.image.load('back.png')

#우주선 이미지, 미사일 이미지 필요
hero = Sprite(20, 400, 'hero.png')
#hero.set_colorkey(white)
ourmissile =Sprite(0, 480, 'heromissile.png')
#hero.set_colorkey(white)

#적 이미지, 미사일 이미지 필요
enemies = []
x = 0
for count in range(10):
    enemies.append(Sprite(50 * x + 50, 50, 'baddie.png'))
    x += 1

enemymissile = Sprite(0, 480, 'baddiemissile.png')

enemyspeed = 3
clock = pygame.time.Clock()
quit = False
game_over = False

while quit != True:
    screen.blit(backdrop, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and hero.x < 590:
                hero.x += 5
            if event.key == pygame.K_LEFT and hero.x > 10:
                hero.x -= 5
            if event.key == pygame.K_SPACE:
                ourmissile.x = hero.x
                ourmissile.y = hero.y

    if not game_over:
        for count in range(len(enemies)):
            enemies[count].x += enemyspeed

        if enemies[len(enemies)-1].x > 590:
            enemyspeed = -3
            for count in range(len(enemies)):
                enemies[count].y += 5
        if enemies[0].x < 10:
            enemyspeed = 3
            for count in range(len(enemies)):
                enemies[count].y += 5

        if ourmissile.y <479 and ourmissile.y > 0:
            ourmissile.render()
            ourmissile.y -= 5

        if enemymissile.y >= 480 and len(enemies) > 0:
            enemymissile.x = enemies[random.randint(0, len(enemies) -1)].x
            enemymissile.y = enemies[0].y

        if Collision(hero.x, hero.y, enemymissile.x, enemymissile.y):
            game_over = True

        for count in range(0, len(enemies)):
            if Collision(ourmissile.x, ourmissile.y, enemies[count].x, enemies[count].y):
                del enemies[count]
                break

        if len(enemies) == 0:
            game_over = True

        enemymissile.render()
        enemymissile.y += 5

    if game_over:
        text = font.render("Game Over", 1, white)
        screen.blit(text, [200, 200])

    hero.render()

    for count in range(len(enemies)):
        enemies[count].render()

    clock.tick(70)
    pygame.display.update()

pygame.quit()


