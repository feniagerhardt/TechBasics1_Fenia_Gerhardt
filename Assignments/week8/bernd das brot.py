import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Character:
    def __init__(self, x, y):
        self.original_image = self.image
        self.rect = self.image.get_rect(x=x, y=y)
        self.angle = 0
        self.direction = random.choice([-5, 5])  # pick once at start
        self.walk_timer = 0

    def walk(self):
        self.walk_timer += 1
        if self.walk_timer > 60:  # after 60 frames, pick a new direction
            self.direction = random.choice([-5, 5])
            self.walk_timer = 0
        self.rect.x += self.direction

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotate(self.original_image, self.angle)

class Bernd (Character):
    def __init__(self, x, y):
        self.image = pygame.image.load("bernd.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        super().__init__(x, y)

    def walk(self):
        super().walk()
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH

class DarthVader (Character):
    def __init__(self, x, y):
        self.image = pygame.image.load("darth vader.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        super().__init__(x, y)

    def walk(self):
        super().walk()
        if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
            self.direction *= -1

bernd = Bernd(100, 100)
vader = DarthVader(400, 100)

screen.blit(bernd.image, bernd.rect)
screen.blit(vader.image, vader.rect)

clock = pygame.time.Clock()

flag = True
vader_appeared_time = None

# music elements were done with the help of AI
pygame.mixer.music.load("bernd.mp3")
pygame.mixer.music.play(-1, start=24.0)  # -1 loops forever
pygame.mixer.init()

while flag:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    if vader_appeared_time is None:
        screen.fill('white')
    else:
        screen.fill('black')

    if pygame.time.get_ticks() > 10000:
        if vader_appeared_time is None:
            vader_appeared_time = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Star Wars.mp3")
            pygame.mixer.music.play(start=9.0)

        if pygame.time.get_ticks() - vader_appeared_time > 20000:
            pygame.mixer.music.stop()

        if vader_appeared_time is None:
            vader_appeared_time = pygame.time.get_ticks()

        vader.walk()
        screen.blit(vader.image, vader.rect)

        if pygame.time.get_ticks() - vader_appeared_time < 3000:
            bernd.rotate()
        else:
            bernd.angle = 0  # reset angle
            bernd.image = bernd.original_image  # restore original image
            bernd.walk()
    else:
        bernd.walk()

    screen.blit(bernd.image, bernd.rect)

    pygame.display.flip()
pygame.quit()
