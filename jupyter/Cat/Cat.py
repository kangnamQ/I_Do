import pygame

black = [0, 0, 0]
white = [255, 255, 255]
back_color = [255, 255, 153]


class GraphicWall(pygame.sprite.Sprite):
    def setGraphic(self, tilex, tiley, tilewidth, tileheight, x, y, width, height):
        myimage = pygame.image.load("terrain_atlas.png").convert()
        self.image = pygame.Surface([width, height])

        for row in range(height // tileheight):
            for column in range(width // tilewidth):
                self.image.blit(myimage, [column * tilewidth, row * tileheight],
                                [tilex, tiley, tilewidth, tileheight])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.image.set_colorkey(white)

    def setGraphic2(self, tilex, tiley, x, y, width, height):
        myimage = pygame.image.load("terrain_atlas.png").convert()
        self.image = pygame.Surface([width, height])
        self.image.blit(myimage, [0, 0], [tilex, tiley, 32, 32])

        for column in range(width // 32 - 2):
            self.image.blit(myimage, [(column + 1) * 32, 0], [tilex + 32, tiley, 32, 32])
            self.image.blit(myimage, [(width // 32 - 1) * 32, 0], [tilex + 64, tiley, 32, 32])

        for row in range(height // 32 - 2):
            self.image.blit(myimage, [0, (row + 1) * 32], [tilex, tiley + 32, 32, 32])
            for column in range(width // 32 - 2):
                self.image.blit(myimage, [(column + 1) * 32, (row + 1) * 32],
                                [tilex + 32, tiley + 32, 32, 32])
            self.image.blit(myimage, [(width // 32 - 1) * 32, (row + 1) * 32],
                            [tilex + 64, tiley + 32, 32, 32])

        self.image.blit(myimage, [0, (height // 32 - 1) * 32], [tilex, tiley + 64, 32, 32])

        for column in range(width // 32 - 2):
            self.image.blit(myimage, [(column + 1) * 32, (height // 32 - 1) * 32],
                            [tilex + 32, tiley + 64, 32, 32])
        self.image.blit(myimage, [(width // 32 - 1) * 32, (height // 32 - 1) * 32],
                        [tilex + 64, tiley+64, 32, 32])

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.image.set_colorkey(white)

class StoneWall(GraphicWall):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        tilex = 32 * 16
        tiley = 32 * 29
        self.setGraphic2(tilex, tiley, x, y, width, height)


class StoneWall2(GraphicWall):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        tilex = 32 * 16
        tiley = 32 * 23
        self.setGraphic2(tilex, tiley, x, y, width, height)

class Tree1(GraphicWall):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = 64
        height = 160
        tilewidth = 64
        tileheight = 160
        tilex = 32 * 30
        tiley = 32 * 0
        self.setGraphic(tilex, tiley, tilewidth, tileheight, x, y, width, height)

class Tree2(GraphicWall):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = 96
        height = 128 * 2
        tilewidth = 96
        tileheight = 128
        tilex = 32 * 29
        tiley = 32 * 28
        self.setGraphic(tilex, tiley, tilewidth, tileheight, x, y, width, height)

class WaterWall(GraphicWall):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        tilex = 32 * 9
        tiley = 32 * 11
        self.setGraphic2(tilex, tiley, x, y, width, height)

class GardenWall(GraphicWall):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        tilex = 32 * 5
        tiley = 32 * 17
        self.setGraphic2(tilex, tiley, x, y, width, height)

class TallGrass(GraphicWall):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        tilex = 32 * 0
        tiley = 32 * 22
        self.setGraphic2(tilex, tiley, x, y, width, height)

class FallGrass(GraphicWall):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        tilex = 32 * 0
        tiley = 32 * 28
        self.setGraphic2(tilex, tiley, x, y, width, height)

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    frame = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,9):
            img = pygame.image.load("cat"+str(i)+".jpg").convert()
            img.set_colorkey(white)
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self, walls):
        old_x = self.rect.x
        new_x = old_x + self.change_x
        self.rect.x = new_x
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            self.rect.x = old_x

        old_y =self.rect.y
        new_y = old_y + self.change_y
        self.rect.y = new_y
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            self.rect.y = old_y

        if self.change_x < 0:
            self.frame += 1

            if self.frame > 3*4:
                self.frame = 0
            self.image = self.images[self.frame//4]

        if self.change_x > 0:
            self.frame += 1

            if self.frame > 3*4:
                self.frame = 0
            self.image = self.images[self.frame//4+4]

def setupRoomOne():
    wall_list = pygame.sprite.Group()
    wall = StoneWall(390, 80, 96, 448)
    wall_list.add(wall)
    wall = StoneWall2(600, 0, 128, 320)
    wall_list.add(wall)

    return wall_list

def setupRoomTwo():
    wall_list = pygame.sprite.Group()
    wall = Tree1(100, 100)
    wall_list.add(wall)
    wall = Tree2(300, 250)
    wall_list.add(wall)
    wall = TallGrass(100, 400, 64, 160)
    wall_list.add(wall)
    wall = Tree1(500, 160)
    wall_list.add(wall)
    wall = FallGrass(600, 128, 192, 160)
    wall_list.add(wall)
    wall = Tree1(700, 350)
    wall_list.add(wall)

    return wall_list

def setupRoomThree():
    wall_list = pygame.sprite.Group()
    wall = WaterWall(64, 64, 192, 192)
    wall_list.add(wall)
    wall = GardenWall(128, 325, 256, 192)
    wall_list.add(wall)
    wall = Tree1(520, 256)
    wall_list.add(wall)

    return wall_list


pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("고양이 모험")

player = Player()
player.rect.x = 50
player.rect.y = 50

movingsprites = pygame.sprite.Group()
movingsprites.add(player)

current_room = 1
wall_list = setupRoomOne()

clock = pygame.time.Clock()
done = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, -5)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, 5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5, 0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-5, 0)
            if event.key == pygame.K_UP:
                player.changespeed(0, 5)
            if event.key == pygame.K_DOWN:
                player.changespeed(0, -5)

    player.update(wall_list)

    if player.rect.x < -15:
        if current_room == 1:
            wall_list = setupRoomThree()
            current_room = 3
            player.rect.x = 790
        elif current_room == 3:
            wall_list = setupRoomTwo()
            player.rect.x = 790
            current_room = 2
        else:
            wall_list = setupRoomOne()
            player.rect.x = 790
            current_room = 1

    if player.rect.x > 801:
        if current_room == 1:
            wall_list = setupRoomTwo()
            current_room = 2
            player.rect.x = 0
        elif current_room == 2:
            wall_list = setupRoomThree()
            current_room = 3
            player.rect.x = 0
        else:
            wall_list = setupRoomOne()
            current_room = 1
            player.rect.x = 0

    screen.fill(back_color)
    movingsprites.draw(screen)
    wall_list.draw(screen)
    pygame.display.flip()

    clock.tick(40)

pygame.quit()
