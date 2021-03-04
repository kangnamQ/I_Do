##그리드 클라이언트 프로그램
import pygame
from socket import *
from threading import *

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

width = 20
height = 20

margin = 5

def clientRecv():
    while True:
        serverIndex = list(clientSocket.recv(1024))
        row = serverIndex[0]
        column = serverIndex[1]
        grid[row][column] = 1
        print("Receive, Grid Server Index:", row, column)

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

print("Client TCP initialize...")

serverName = '127.0.0.1'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Server connected...")

Thread(target = clientRecv).start()
pygame.init()

size=[255,255]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("클라이언트 그리드")
done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            grid[row][column] = 2
            print("Click", pos, "Grid Server Index:", row, column)

            clientIndex = [row,column]
            indexBytes = bytes(clientIndex)
            clientSocket.send(indexBytes)
            print("Send, Grid Client Index:", row, column)

    screen.fill(black)
    for row in range(10):
        for column in range(10):
            color = white
            if grid[row][column] == 1:
                color = green
            elif grid[row][column] == 2:
                color = red

            pygame.draw.rect(screen, color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin, width, height])
    clock.tick(20)
    pygame.display.flip()

pygame.quit()