import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avatar Customization Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game states
CUSTOMIZING = "customizing"
PLAYING = "playing"
game_state = CUSTOMIZING

# Load avatar parts (for now, just colored rectangles)
avatar_parts = [
    pygame.Rect(50, 100, 50, 50),  # Head
    pygame.Rect(50, 200, 50, 100),  # Body
    pygame.Rect(50, 350, 40, 40),  # Left Eye
    pygame.Rect(110, 350, 40, 40),  # Right Eye
]

# Avatar position for customization
assembled_avatar = {
    "head": pygame.Rect(350, 150, 50, 50),
    "body": pygame.Rect(350, 200, 50, 100),
    "left_eye": pygame.Rect(340, 170, 20, 20),
    "right_eye": pygame.Rect(390, 170, 20, 20),
}

# Player position for movement phase
player_x, player_y = 350, 200
player_speed = 5

# Dragging state
dragging = None

# Font
font = pygame.font.Font(None, 36)

# Button
start_button = pygame.Rect(300, 500, 200, 50)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle dragging parts during customization
        if game_state == CUSTOMIZING:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, part in enumerate(avatar_parts):
                    if part.collidepoint(mouse_x, mouse_y):
                        dragging = i  # Start dragging this part
            
            if event.type == pygame.MOUSEBUTTONUP:
                if dragging is not None:
                    # Snap to assembled avatar position
                    keys = list(assembled_avatar.keys())
                    avatar_parts[dragging].topleft = assembled_avatar[keys[dragging]].topleft
                    dragging = None
            
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(mouse_x, mouse_y):
                # Start the game after customization
                game_state = PLAYING
        
        # Handle movement during gameplay
        elif game_state == PLAYING:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_x += player_speed
            if keys[pygame.K_UP]:
                player_y -= player_speed
            if keys[pygame.K_DOWN]:
                player_y += player_speed

    # --- DRAWING ---
    
    if game_state == CUSTOMIZING:
        # Draw draggable parts
        pygame.draw.rect(screen, BLUE, avatar_parts[0])  # Head
        pygame.draw.rect(screen, RED, avatar_parts[1])  # Body
        pygame.draw.rect(screen, GREEN, avatar_parts[2])  # Left Eye
        pygame.draw.rect(screen, GREEN, avatar_parts[3])  # Right Eye
        
        # Draw start button
        pygame.draw.rect(screen, BLACK, start_button)
        screen.blit(font.render("START", True, WHITE), (330, 515))
    
    elif game_state == PLAYING:
        # Draw avatar moving in the blank level
        pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))  # Head
        pygame.draw.rect(screen, RED, (player_x, player_y + 50, 50, 100))  # Body
        pygame.draw.rect(screen, GREEN, (player_x + 10, player_y + 10, 20, 20))  # Left Eye
        pygame.draw.rect(screen, GREEN, (player_x + 30, player_y + 10, 20, 20))  # Right Eye
    
    # Update screen
    pygame.display.flip()

pygame.quit()