import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(" Rock, Paper, Scissors ")

# Colors
pink = (255, 182, 193)
white = (173, 216, 230)
black = (0, 0, 0)

# Font
title_font = pygame.font.Font(None, 60)  # Big font for the title
text_font = pygame.font.Font(None, 40)  # Medium font for instructions and results

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Load and resize images (Ensure these files exist in your directory)
rock_img = pygame.image.load(r"C:\Users\zunai\OneDrive\Desktop\Python\ppp.jpg")
paper_img = pygame.image.load(r"C:\Users\zunai\OneDrive\Desktop\Python\pinkpaper.jpg")
scissors_img = pygame.image.load(r"C:\Users\zunai\OneDrive\Desktop\Python\pinkscissors.jpg")

rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Game logic function
def game_logic(player_choice):
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return computer_choice, " It's a Tie! "
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return computer_choice, " You Win! :) "
    else:
        return computer_choice, " You Lose! :("

# Centered display helper function
def draw_centered_text(text, font, color, y_pos):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen_width // 2, y_pos))
    screen.blit(text_surface, text_rect)

running = True
result = ""
computer_choice_img = None

while running:
    # Fill the background with a cute color
    screen.fill(pink)

    # Draw the title at the top
    draw_centered_text(" Let's Play Rock, Paper, Scissors ", title_font, black, 50)

    screen.blit(rock_img, (100, 200))      # Rock: Positioned farther left
    screen.blit(paper_img, (325, 200))     # Paper: Positioned center
    screen.blit(scissors_img, (550, 200))  # Scissors: Positioned farther right


    # Display the result text
    draw_centered_text(result, text_font, black, 500)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 100 <= x <= 250 and 200 <= y <= 350:  # Rock
                result = f"You chose Rock. {game_logic('Rock')[1]}"
            elif 325 <= x <= 475 and 200 <= y <= 350:  # Paper
                result = f"You chose Paper. {game_logic('Paper')[1]}"
            elif 550 <= x <= 700 and 200 <= y <= 350:  # Scissors
                result = f"You chose Scissors. {game_logic('Scissors')[1]}"

    
    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
