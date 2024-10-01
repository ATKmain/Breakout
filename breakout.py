import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_COLOR = WHITE
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_RADIUS = 10
BALL_COLOR = WHITE
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed = [random.choice([-4, 4]), -4]

# Bricks
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_COLOR = RED
bricks = [pygame.Rect(10 + i * (BRICK_WIDTH + 10), 10 + j * (BRICK_HEIGHT + 10), BRICK_WIDTH, BRICK_HEIGHT) for i in range(10) for j in range(5)]

# Game variables
lives = 3
score = 0

# Main game loop
def main():
    global lives, score, ball_speed

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-6, 0)
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.move_ip(6, 0)

        # Ball movement
        ball.move_ip(ball_speed)
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]
        if ball.bottom >= SCREEN_HEIGHT:
            lives -= 1
            ball.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            ball_speed = [random.choice([-4, 4]), -4]
            if lives == 0:
                running = False

        # Brick collision
        for brick in bricks[:]:
            if ball.colliderect(brick):
                ball_speed[1] = -ball_speed[1]
                bricks.remove(brick)
                score += 10
                break

        # Drawing
        SCREEN.fill(BLACK)
        pygame.draw.rect(SCREEN, PADDLE_COLOR, paddle)
        pygame.draw.ellipse(SCREEN, BALL_COLOR, ball)
        for brick in bricks:
            pygame.draw.rect(SCREEN, BRICK_COLOR, brick)

        # Display score and lives
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        SCREEN.blit(score_text, (10, SCREEN_HEIGHT - 40))
        SCREEN.blit(lives_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
