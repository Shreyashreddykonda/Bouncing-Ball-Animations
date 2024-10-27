import pygame
import time
pygame.init()

width = 1000
height = 600

pygame.display.set_caption("This is a bouncing ball simulation")
screen = pygame.display.set_mode((600, 600))

red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 225, 0)
brown = (204, 102, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
ball = pygame.draw.circle(surface=screen, color=red, center=[100, 100], radius=40)
ball1 = pygame.draw.circle(surface=screen, color=blue, center=[600, 0], radius=40)
ball2 = pygame.draw.circle(surface=screen, color=green, center=[13, 25], radius=40)
ball3 = pygame.draw.circle(surface=screen, color=brown, center=[300, 300], radius=40)
ball4 = pygame.draw.circle(surface=screen, color=yellow, center=[-20, 24], radius=40)
ball5 = pygame.draw.circle(surface=screen, color=white, center=[90, 90], radius=40)

speed = [0, 1]
speed1 = [-2, 2]
speed2 = [3, 3]
speed3 = [2, 2]
speed4 = [5, 0]
speed5 = [9, 9]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(black)
    ball = ball.move(speed)
    ball1 = ball1.move(speed1)
    ball2 = ball2.move(speed2)
    ball3 = ball3.move(speed3)
    ball4 = ball4.move(speed4)
    ball5 = ball5.move(speed5)

    if ball.left <= 0 or ball.right >= width:
        speed[0] = -speed[0]
    if ball.top <= 0 or ball.bottom >= height:
        speed[1] = -speed[1]
        
    if ball1.left <= 0 or ball1.right >= width:
        speed1[0] = -speed1[0]
    if ball1.top <= 0 or ball1.bottom >= height:
        speed1[1] = -speed1[1]

    if ball2.left <= 0 or ball2.right >= width:
        speed2[0] = -speed2[0]
    if ball2.top <= 0 or ball2.bottom >= height:
        speed2[1] = -speed2[1]
        
    if ball3.left <= 0 or ball3.right >= width:
        speed3[0] = -speed3[0]
    if ball3.top <= 0 or ball3.bottom >= height:
        speed3[1] = -speed3[1]

    if ball4.left <= 0 or ball4.right >= width:
        speed4[0] = -speed4[0]
    if ball4.top <= 0 or ball4.bottom >= height:
        speed4[1] = -speed4[1]

    if ball5.left <= 0 or ball5.right >= width:
        speed5[0] = -speed5[0]
    if ball5.top <= 0 or ball5.bottom >= height:
        speed5[1] = -speed5[1]
        
    pygame.draw.circle(surface = screen, color = red, center=ball.center, radius=40)
    pygame.draw.circle(surface = screen, color = blue, center=ball1.center, radius=40)
    pygame.draw.circle(surface = screen, color = green, center=ball2.center, radius=40)
    pygame.draw.circle(surface = screen, color = brown, center=ball3.center, radius=40)
    pygame.draw.circle(surface = screen, color = yellow, center=ball4.center, radius=40)
    pygame.draw.circle(surface = screen, color = white, center=ball5.center, radius=40)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
                       
                       
