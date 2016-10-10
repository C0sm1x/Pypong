import pygame

pygame.init()
# Screen dimensions
display_Width = 640

display_Height = 480

# Creating the game window
gameDisplay = pygame.display.set_mode((display_Width,display_Height))

# Window title
pygame.display.set_caption('Pypong')

#defing RGB colors. Red, Blue, Green I might not use them though.
black = (0, 0, 0)
white = (255, 255, 255)

# Variable declaration
x_pos = 0
y_pos = 0
p1_X = 100
p1_Y = 200

p2_X = 500
p2_Y = 200

clock = pygame.time.Clock()

def player1(p1_X, p1_Y):
	pygame.draw.rect(gameDisplay, white, [p1_X, p1_Y, 3, 50], 5)

def player2(p2_X, p2_Y):
	pygame.draw.rect(gameDisplay, white, [p2_X, p2_Y, 3, 50], 5)

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
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_pos = -4
			elif event.key == pygame.K_RIGHT:
				x_pos = 4
			if event.key == pygame.K_DOWN:
				y_pos = 4
			elif event.key == pygame.K_UP:
				y_pos = -4	
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_pos = 0
			if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
				y_pos = 0

	gameDisplay.fill(black)
	
	p1_X += x_pos	
	p1_Y += y_pos

	player1(p1_X, p1_Y)
	player2(p2_X, p2_Y)
	lineinthemiddle(300,0, 300, 600)

	# Updating the display
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
