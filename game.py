# Love Saroha
# lovesaroha1994@gmail.com (email address)
# https://www.lovesaroha.com (website)
# https://github.com/lovesaroha  (github)

import pygame
import random
from collections import namedtuple

# Pygame.
pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 25)

# Default values.
Point = namedtuple('Point', 'x, y')
snakeColor = (84, 104, 231)
blockSize = 20
speed = 10

class SnakeGame:

    def __init__(self, w=640, h=480):
        self.width = w
        self.height = h
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.direction = 1
        self.head = Point(self.width/2, self.height/2)
        self.snake = [self.head,
                      Point(self.head.x-blockSize, self.head.y),
                      Point(self.head.x-(2*blockSize), self.head.y)]

        self.score = 0
        self.food = None
        self.placeFood()

    def placeFood(self):
        x = random.randint(0, (self.width-blockSize)//blockSize)*blockSize
        y = random.randint(0, (self.height-blockSize)//blockSize)*blockSize
        self.food = Point(x, y)
        if self.food in self.snake:
            self.placeFood()

    def update(self):
        # Controls key events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = 2
                elif event.key == pygame.K_RIGHT:
                    self.direction = 1
                elif event.key == pygame.K_UP:
                    self.direction = 3
                elif event.key == pygame.K_DOWN:
                    self.direction = 4

        self.moveSnake(self.direction) 
        self.snake.insert(0, self.head)
        game_over = False
        if self.collision():
            game_over = True
            return game_over, self.score
        if self.head == self.food:
            self.score += 1
            self.placeFood()
        else:
            self.snake.pop()
        self.show()
        self.clock.tick(speed)

        return game_over, self.score

    def collision(self):
        if self.head.x > self.width - blockSize or self.head.x < 0 or self.head.y > self.height - blockSize or self.head.y < 0:
            return True
        if self.head in self.snake[1:]:
            return True
        return False

    def show(self):
        self.display.fill((255, 255, 255))

        for pt in self.snake:
            pygame.draw.rect(self.display, snakeColor, pygame.Rect(
                pt.x, pt.y, blockSize, blockSize))
            pygame.draw.rect(self.display,  (255, 255, 255),
                             pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        pygame.draw.rect(self.display, snakeColor, pygame.Rect(
            self.food.x, self.food.y, blockSize, blockSize))
        pygame.draw.rect(self.display,  (255, 255, 255),
                             pygame.Rect(self.food.x+4, self.food.y+4, 12, 12))    

        text = font.render("Score " + str(self.score), True,  (0, 0, 0))
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def moveSnake(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == 1:
            x += blockSize
        elif direction == 2:
            x -= blockSize
        elif direction == 4:
            y += blockSize
        elif direction == 3:
            y -= blockSize

        self.head = Point(x, y)


if __name__ == '__main__':
    game = SnakeGame()

    # Start game.
    while True:
        gameOver, score = game.update()

        if gameOver == True:
            break

    pygame.quit()
