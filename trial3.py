import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TanXinAssignment3")

WHITE = (255, 255, 255)

class Circle:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

circles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            radius = random.randint(10, 50)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            speed_x = random.choice([-1, 1]) * random.uniform(0.5, 2)
            speed_y = random.choice([-1, 1]) * random.uniform(0.5, 2)
            circles.append(Circle(x, y, radius, color, speed_x, speed_y))

    for circle in circles:
        circle.move()

    screen.fill(WHITE)
    for circle in circles:
        circle.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()