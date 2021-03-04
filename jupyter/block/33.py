import math
import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 블록의 크기
block_width = 23
block_height = 15


# 블록을 정의하는 클래스
# sprite 부모 클래스를 상속
class Block(pygame.sprite.Sprite):  # 왜 스프라이트가 2개 붙는지?
    # 생성자, 블록의 색과 위치를 인수로 전달
    def __init__(self, color, x, y):
        # 부모클래스 생성자 호출
        pygame.sprite.Sprite.__init__(self)  # 파이게임 위를 불로오고 init를 쓰고 self를 하면 부모 클래스 생성자 호출인가?
        # 블록의 이미지와 색 지정
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        # 이미지 크기의 rect 객체 지정 (사각형)
        self.rect = self.image.get_rect()
        # 블록의 위치 지정
        self.rect.x = x
        self.rect.y = y


# 공을 정리하는 클래스
# Sprite 부모 클래스를 상속
class Ball(pygame.sprite.Sprite):
    # 이동속도(픽셀/사이클)
    speed = 10.0
    # 공의 위치를 표현하는 실수
    x = 0.0
    y = 180.0
    # 공의 방향 (도,degrees)
    direction = 200
    # 공의 크기
    width = 10
    height = 10

    # 생성자
    def __init__(self):
        # 부모 클래스 생성자 호출
        pygame.sprite.Sprite.__init__(self)

        # 공의 이미지와 색 지정
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(red)
        # 이미지 크기의 rect 객체 지정
        self.rect = self.image.get_rect()
        # 스크린의 높이와 너비 지정
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

    # 수평면에 공을 되튕기는 함수
    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        # cos 부호 반전, y방향 반전
        self.direction -= diff
        # 공의 위치를 갱신

    def update(self):
        # 각도를 라디안으로 변환
        direction_radians = math.radians(self.direction)
        # 이동속도와 방향에 따라 위치를 결정
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
        # 이미지를 이동
        self.rect.x = self.x
        self.rect.y = self.y

        # 스크린 위에서 충돌 후 되튕기기
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
        # 스크린 왼쪽에서 충돌 후 되튕기기
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            # sin부호 반전, x방향 반전
            self.x = 1
            # 스크린 오른쪽에서 충돌후 되튕기기
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            # sin부호 반전, x방향 반전
            self.x = self.screenwidth - self.width - 1
        # 스크린 아래로 떨어지는 여부 조사
        if self.y > 600:
            return True
        else:
            return False


# 플레이어 막대를 정의하는 클래스
class Player(pygame.sprite.Sprite):
    # 생성자
    def __init__(self):
        # 부모 클래스 생성자 호출
        pygame.sprite.Sprite.__init__(self)
        # 막대의 이미지와 색 지정
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(green)
        # 이미지 크기의  rect 객체에 위치 지정
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.topleft = (0, self.screenheight - self.height)
        # 플레이어 막대의 위치 갱신

    def update(self):
        # 마우스 현재 위치에서 막대위치
        pos = pygame.mouse.get_pos()
        self.rect.left = pos[0]
        # 스크린 오른쪽 경계를 막대가 너지 않도록 조정
        if self.rect.left > self.screenwidth - self.width:
            self.rect.left = self.screenwidth - self.width


pygame.init()

# 윈도우설정
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('블록 깨기')

##여기부터
background_position = [0, 0]
# 이미지 적재
background_image = pygame.image.load("cat1.png").convert()



# 마우스 포인트 감춤
pygame.mouse.set_visible(0)

# 텍스트 폰트생성
font = pygame.font.Font('NanumGothic.ttf', 36)
# 스프라이트 리스트 생성
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

# 플레이어 막대 생성
player = Player()
allsprites.add(player)

# 공 생성
ball = Ball()
allsprites.add(ball)
balls.add(ball)

# 블록의 꼭대기 y좌표
top = 80
# 한행의 총 블록의 수
blockcount = 32

# 5 x 32 블록 생성
# 5행의 블록
for row in range(5):
    for column in range(0, blockcount):
        block = Block(blue, column * (block_width + 2) + 1, top)
        blocks.add(block)
        allsprites.add(block)
        # 아래 행으로 블록 위치 이동
    top += block_height + 2
clock = pygame.time.Clock()
game_over = False
exit_program = False

while exit_program != True:
    # 30프레임 /초
    clock.tick(30)

    # 스크린 클리어
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

            # 공과 플레이어 위치 갱신
    if not game_over:
        player.update()
        game_over = ball.update()

    screen.blit(background_image, background_position)

    if game_over:  # 게임 종료이면 Game Over 출력
        text = font.render("Game Over", 1, black)
        textpos = text.get_rect(centerx=screen.get_width() / 2)
        screen.blit(text, textpos)
        # 플레이어 막대와 공이 충돌하면
    if pygame.sprite.spritecollide(player, balls, False):
        # 막대의 중앙에서 공이 충돌한 위치의 차이 계산,
        # 중앙 왼쪽 충돌+, 오른쪽충돌-
        diff = (player.rect.left + player.width / 2) - (ball.rect.left + ball.width / 2)

        # 공의 y위치를 막대 경계값으로 조정
        ball.rect.top = screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)

        # 공과 블록의 충돌 조사
    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)

    # 공이 블록에 충동했으면 되튕기기
    if len(deadblocks) > 0:
        ball.bounce(0)

        # 모든 블록을 깼으면 게임 종료
        if len(blocks) == 0:
            game_over = True

            # 모든 스프라이트 그리기
    allsprites.draw(screen)
    # 스크린 갱신하여 디스플레이
    pygame.display.flip()

pygame.quit()
