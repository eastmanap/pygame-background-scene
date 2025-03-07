import pygame
import sys
import colors
import config  # Import the config module
import shapes

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object
    
    running = True
    while running:
        running = handle_events()
        screen.fill(colors.WEIRDLY_SATURATED_SKY_BLUE)  # Use color from config
        
        # Draw on the screen
        # Hills
        shapes.draw_background(screen)

        # Truman show
        shapes.draw_staircase(screen, 180, 330, 5)

        # Cloud 1
        shapes.draw_cloud(screen, 100, 100, 25)
        shapes.draw_cloud(screen, 110, 120, 25)
        shapes.draw_cloud(screen, 140, 115, 25)

        # Cloud 2
        shapes.draw_cloud(screen, 430, 150, 40)
        shapes.draw_cloud(screen, 400, 170, 30)

        # Cloud 3
        shapes.draw_cloud(screen, 650, 110, 30)
        shapes.draw_cloud(screen, 650, 130, 30)
        shapes.draw_cloud(screen, 680, 120, 30)

        # House
        shapes.draw_house(screen, 520, 250, 100)

        # Trees
        shapes.draw_tree(screen, 100, 400, 150)
        shapes.draw_tree(screen, 730, 450, 150)
        shapes.draw_tree(screen, 300, 300, 100)
        shapes.draw_tree(screen, 630, 280, 100)
        shapes.draw_tree(screen, 350, 490, 200)


        pygame.display.flip()
        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
