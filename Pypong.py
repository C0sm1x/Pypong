import pygame
import random 
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
red = (255, 0, 0)

clock = pygame.time.Clock()

def player1(p1_X, p1_Y):
	pygame.draw.rect(gameDisplay, white, [p1_X, p1_Y, 3, 50], 5)

def player2(p2_X, p2_Y):
	pygame.draw.rect(gameDisplay, white, [p2_X, p2_Y, 3, 50], 5)

def lineinthemiddle(start_X, start_Y, end_X, end_Y):
	pygame.draw.line(gameDisplay, white, [start_X, start_Y], [end_X, end_Y], 2)

def circle(circle_X, circle_Y, circle_Radius, circle_Thickness):
    pygame.draw.circle(gameDisplay, red, (circle_X, circle_Y), circle_Radius, circle_Thickness)

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

    start_X = display_Width/2
    start_Y = 0
    end_X = display_Width/2
    end_Y = 600
    left_Boundery = 6
    bottom_Boundery = 425
    top_Boundery = 3
    right_Boundery = 630
    circle_X = start_X
    circle_Y = 200
    circle_Thickness = 0
    circle_Radius = 10
    random_X_Num = random.randint(0,1)
    random_Y_Num = random.randint(0,1) 

    
    

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
	    lineinthemiddle(start_X, start_Y, end_X, end_Y,)
            circle(circle_X, circle_Y, circle_Radius, circle_Thickness)
            
            if random_X_Num == 0:
                circle_X += 4
            elif random_X_Num == 1:
                circle_X -= 4
            
            if random_Y_Num == 0:
                circle_Y += 4
            elif random_Y_Num == 1:
                circle_Y -=4
            # Player 1 bounderies
            # Left and right bounderies
            if p1_X > start_X - 10:
                p1_X = start_X -10
            elif p1_X < left_Boundery:
                 p1_X = left_Boundery
            # Top and bottom bounderies
            if p1_Y > bottom_Boundery: 
                p1_Y = bottom_Boundery
            elif p1_Y < top_Boundery:
                p1_Y = top_Boundery

            #Player 2 bounderies

            # Left and right bounderies
            if p2_X > right_Boundery:
                p2_X = right_Boundery
            elif p2_X < start_X + 10:
                p2_X = start_X + 10
            # Top and bottom bounderies
            if p2_Y < top_Boundery:
                p2_Y = top_Boundery
            elif p2_Y > bottom_Boundery:
                p2_Y = bottom_Boundery
            # Bounderies for the ball
            # Top and bottom bounderies
            if circle_Y <  top_Boundery + 7:
                circle_Y += 8
            elif circle_Y > bottom_Boundery + 45:
                circle_Y -= 8
	    # Updating the display
	    pygame.display.update()
	    clock.tick(60)

gameloop()

pygame.quit()
quit()
