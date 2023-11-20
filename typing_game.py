import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_NAME = 'Arial'
FONT_SIZE = 36
WORD_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")

# Load background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load words from a file
with open("words.txt", "r") as file:
    words = file.read().splitlines()

# Initialize variables
score = 0
word_x, word_y = random.randint(50, WIDTH - 200), 0
current_word = random.choice(words)
font = pygame.font.Font(pygame.font.match_font(FONT_NAME), FONT_SIZE)
clock = pygame.time.Clock()

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def main():
    global word_y, current_word, score

    running = True
    word_speed = WORD_SPEED

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        # Clear the screen
        screen.blit(background, (0, 0))

        # Move the word downwards
        word_y += word_speed

        # Draw the current word
        draw_text(current_word, word_x, word_y)

        # Check if the word has reached the bottom
        if word_y > HEIGHT:
            current_word = random.choice(words)
            word_x, word_y = random.randint(50, WIDTH - 200), 0

        # Check for user input
        input_text = ""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text == current_word:
                        score += 1
                        current_word = random.choice(words)
                        word_x, word_y = random.randint(50, WIDTH - 200), 0
                    input_text = ""
                else:
                    input_text += event.unicode

        # Draw user input
        draw_text(input_text, word_x, word_y + FONT_SIZE)

        # Update the screen
        pygame.display.update()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
