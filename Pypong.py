import pygame

pygame.init()
# Screen dimensions
display_Width = 640

display_Height = 480

#defing RGB colors. Red, Blue, Green I might not use them though.
black = (0, 0, 0)
white = (255, 255, 255)

# Creating the game window
gameDisplay = pygame.display.set_mode((display_Width,display_Height))
# Window title
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

running = True
# Main game loop
while running:
	# check different events
	for event in pygame.event.get():
		# quiting and exiting the loop and game
		if event.type == pygame.QUIT:
			running = False
	# Updating the display
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
