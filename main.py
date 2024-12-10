import pygame
import random
from pygame.locals import *
from ScoreBoard import ScoreBoard  # Import ScoreBoard

# Initialize pygame
pygame.init()
pygame.font.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game with Player, Apples, Strawberries, and Bombs")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
background_image = pygame.image.load('background.jpg')  # Load your background image
player_image = pygame.image.load('player.png')  # Load your player image
apple_image = pygame.image.load('apple.png')  # Load your apple image
strawberry_image = pygame.image.load('strawberry.png')  # Load your strawberry image
bomb_image = pygame.image.load('bomb.png')  # Load your bomb image

# Scale images to fit
background_image = pygame.transform.scale(background_image, (800, 600))
player_image = pygame.transform.scale(player_image, (50, 50))
apple_image = pygame.transform.scale(apple_image, (30, 30))
strawberry_image = pygame.transform.scale(strawberry_image, (30, 30))
bomb_image = pygame.transform.scale(bomb_image, (30, 30))

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  # Use player image
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Define the Apple class
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = apple_image  # Use apple image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = random.randint(0, 570)

    def update(self):
        # Move the apple randomly on the screen
        self.rect.x += random.randint(-2, 2)
        self.rect.y += random.randint(-2, 2)
        # Keep the apple inside the window bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 770:
            self.rect.x = 770
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 570:
            self.rect.y = 570

# Define the Strawberry class
class Strawberry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = strawberry_image  # Use strawberry image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = random.randint(0, 570)

    def update(self):
        # Move the strawberry randomly on the screen
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)
        # Keep the strawberry inside the window bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 770:
            self.rect.x = 770
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 570:
            self.rect.y = 570

# Define the Bomb class
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bomb_image  # Use bomb image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = random.randint(0, 570)

    def update(self):
        # Move the bomb randomly on the screen
        self.rect.x += random.randint(-4, 4)
        self.rect.y += random.randint(-4, 4)
        # Keep the bomb inside the window bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 770:
            self.rect.x = 770
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 570:
            self.rect.y = 570

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create player and add to sprite group
player = Player()
all_sprites.add(player)

# Create multiple apples, strawberries, and bombs and add them to sprite group
apples = pygame.sprite.Group()
strawberries = pygame.sprite.Group()
bombs = pygame.sprite.Group()

for _ in range(5):  # Create 5 apples
    apple = Apple()
    apples.add(apple)
    all_sprites.add(apple)

for _ in range(5):  # Create 5 strawberries
    strawberry = Strawberry()
    strawberries.add(strawberry)
    all_sprites.add(strawberry)

for _ in range(5):  # Create 5 bombs
    bomb = Bomb()
    bombs.add(bomb)
    all_sprites.add(bomb)

# Create an instance of ScoreBoard
score_board = ScoreBoard(30, 30, 0)

# Set up the game loop
running = True
game_over = False
victory = False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over and not victory:
        # Update all sprites
        keys = pygame.key.get_pressed()
        player.update(keys)  # Pass 'keys' to the player update method
        apples.update()
        strawberries.update()
        bombs.update()

        # Check for collisions
        if pygame.sprite.spritecollideany(player, apples):
            score_board.update(10)  # Update score by 10 for each apple
            apple = pygame.sprite.spritecollideany(player, apples)
            apple.kill()

        if pygame.sprite.spritecollideany(player, strawberries):
            score_board.update(20)  # Update score by 20 for each strawberry
            strawberry = pygame.sprite.spritecollideany(player, strawberries)
            strawberry.kill()

        if pygame.sprite.spritecollideany(player, bombs):
            game_over = True  # End the game if the player hits a bomb
        
        # Check for victory
        if not apples and not strawberries:
            victory = True  # Set victory to True if all apples and strawberries are collected

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    if victory:
        victory_text = pygame.font.Font(None, 74).render("Victory!", True, WHITE)
        screen.blit(victory_text, (screen.get_width() // 2 - victory_text.get_width() // 2, screen.get_height() // 2 - victory_text.get_height() // 2))
    elif game_over:
        game_over_text = pygame.font.Font(None, 74).render("Game Over!", True, WHITE)
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 - game_over_text.get_height() // 2))
    else:
        # Draw all the sprites (player, apples, strawberries, bombs)
        all_sprites.draw(screen)
        # Render the scoreboard
        score_board.render(screen)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
