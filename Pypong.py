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


clock = pygame.time.Clock()

def player1(p1_X, p1_Y):
	pygame.draw.rect(gameDisplay, white, [p1_X, p1_Y, 3, 50], 5)

def player2(p2_X, p2_Y):
	pygame.draw.rect(gameDisplay, white, [p2_X, p2_Y, 3, 50], 5)

def lineinthemiddle(start_X, start_Y, end_X, end_Y):
	pygame.draw.line(gameDisplay, white, [start_X, start_Y], [end_X, end_Y], 2)
# Main game loop
def gameloop():
    running = True
    # Variable declaration
    x_pos = 0
    y_pos = 0
    p1_X = 100
    p1_Y = 200

    p2_X = 500
    p2_Y = 200

    start_X = 300
    start_Y = 0
    end_X = 300
    end_Y = 600
    left_Boundery = 6
    bottom_Boundery = 425
    top_Boundery = 3
    right_Boundery = 630
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
	    lineinthemiddle(start_X, start_Y, end_X, end_Y)
            # Player 1 bounderies 
            if p1_X > start_X - 10:
                p1_X = start_X -10
           # Can't move off the screen to the left
            if p1_X < left_Boundery:
                 p1_X = left_Boundery
            # Can't move off the bottom of the screen
            if p1_Y > bottom_Boundery: 
                p1_Y = bottom_Boundery
            # Cant't move off the top of the screen
            if p1_Y < top_Boundery:
                p1_Y = top_Boundery
            #Player 2 bounderies
            # Can't move off the screen to the right for player 2
            if p2_X > right_Boundery:
                p2_X = right_Boundery
            # Player 2 can't pass that middle line 
            if p2_X < start_X + 10:
                p2_X = start_X + 10
            if p2_Y < top_Boundery:
                p2_Y = top_Boundery
            if p2_Y > bottom_Boundery:
                p2_Y = bottom_Boundery
	    # Updating the display
	    pygame.display.update()
	    clock.tick(60)

gameloop()

pygame.quit()
quit()
