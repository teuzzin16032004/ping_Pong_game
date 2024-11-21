import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações de tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (0, 0, 0)
FPS = 60

# Cores
WHITE = (255, 0, 0)

# Configurações da raquete
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Configurações da bola
BALL_WIDTH, BALL_HEIGHT = 10, 10
BALL_SPEED_X, BALL_SPEED_Y = 6, 6

# Inicializando tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Raquetes
player1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Bola
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y

# Pontuação
player1_score, player2_score = 0, 0
font = pygame.font.Font(None, 74)

def draw_objects():
    screen.fill(SCREEN_COLOR)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    score_text = font.render(f"{player1_score}  {player2_score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 50, 10))

def handle_ball_movement():
    global ball_speed_x, ball_speed_y, player1_score, player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Rebater nas paredes superiores e inferiores
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Detectar colisão com as raquetes
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Pontuação
    if ball.left <= 0:
        player2_score += 1
        reset_ball()
    if ball.right >= SCREEN_WIDTH:
        player1_score += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_x *= -1

def handle_player_movement(keys):
    # Jogador 1
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
        player1.y += PADDLE_SPEED

    # Jogador 2
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
        player2.y += PADDLE_SPEED

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    handle_player_movement(keys)
    handle_ball_movement()
    draw_objects()

    pygame.display.flip()
    clock.tick(FPS)
