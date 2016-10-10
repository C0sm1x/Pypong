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
pygame.display.set_caption('Pypong')

clock = pygame.time.Clock()

def player1(x,y):
	pygame.draw.rect(gameDisplay, white, [x, y, 3, 50], 5)

def player2(x,y):
	pygame.draw.rect(gameDisplay, white, [x, y, 3, 50], 5)

def lineinthemiddle(startx, starty, endx, endy):
	pygame.draw.line(gameDisplay, white, [startx, starty], [endx, endy], 2)

running = True
# Main game loop
while running:
	# check different events
	for event in pygame.event.get():
		# quiting and exiting the loop and game
		if event.type == pygame.QUIT:
			running = False

	player1(200, 200)
	player2(400, 200)
	lineinthemiddle(300,0, 300, 600)
	# Updating the display
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
