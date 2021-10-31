# Import and initialize pygame library
import pygame
pygame.init() 

# RGB color combinations
DARKBLUE = (36,90,190)
WHITE = (255,255,255)

# Create a screen of size (400, 200)
screen = pygame.display.set_mode((400, 200))


# While loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False
    screen.fill(DARKBLUE)
    
    # Code to display text "First Name: John" at location (20,10)
    font = pygame.font.Font(None, 34)
    text = font.render("First Name: John" , 1, WHITE)
    screen.blit(text, (20,10))
    
    # Code to display text "Country: India" at location (20,40)
    text = font.render("Country: India" , 1, WHITE)
    screen.blit(text, (20,50))
    
    # Code to display text "State: Bengal" at location (20,70)
    text = font.render("State: Bengal" , 1, WHITE)
    screen.blit(text, (20,90))
    pygame.display.flip() 
pygame.quit()
    