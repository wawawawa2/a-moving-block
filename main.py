import pygame

# initialize pygame and start the music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(.25)
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

# define the window
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('a moving block')

# make a surface
surface = pygame.Surface((win_width, win_height), pygame.SRCALPHA)

# define the font
font = pygame.font.SysFont(None, 55)

# define a function that pauses the game
def pause():
    pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, win_width, win_height])
    win.blit(surface, (0, 0))
    pygame.display.update()  # Update the display after drawing the pause overlay
    pygame.mixer.music.pause()
    
    text = font.render('PAUSE', True, (255, 255, 255))
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(text, text_rect)
    
    pygame.display.update()  # Update the display after drawing the pause overlay
    pygame.mixer.music.pause()


# define the player
player_width = 50
player_height = 50
player = pygame.Rect((400, 300, player_width, player_height))

running = True

# make a clock
clock = pygame.time.Clock()

paused = False

while running:

    # fill the screen with black
    win.fill('black')
    
    # limit the FPS to 60
    clock.tick(60)
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Corrected event key check
                paused = not paused
                if paused:
                    pause()
                else:
                    pygame.mixer.music.unpause()

    # check which keys are being pressed
    key = pygame.key.get_pressed()

    # move the player if specific keys are pressed
    if (key[pygame.K_UP] or key[pygame.K_w]) and player.y != 0 and not paused:
        player.move_ip(0, -5)
    if (key[pygame.K_LEFT] or key[pygame.K_a]) and player.x != 0 and not paused:
        player.move_ip(-5, 0)
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and player.y != win_height - player_height and not paused:
        player.move_ip(0, 5)
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and player.x != win_width - player_width and not paused:
        player.move_ip(5, 0)
    
    # draw the player
    pygame.draw.rect(win, (0, 0, 255), player)

    if paused:
        pause()  # Draw the pause overlay

    pygame.display.update()

pygame.quit()
