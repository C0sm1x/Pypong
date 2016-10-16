import pygame, random 

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

def player1(p1_X, p1_Y, p1_Width, p1_Height):
	pygame.draw.rect(gameDisplay, white, [p1_X, p1_Y, p1_Width, p1_Height], )

def player2(p2_X, p2_Y, p2_Width, p2_Height):
	pygame.draw.rect(gameDisplay, white, [p2_X, p2_Y, p2_Width, p2_Height], )

def lineinthemiddle(start_X, start_Y, end_X, end_Y):
	pygame.draw.line(gameDisplay, white, [start_X, start_Y], [end_X, end_Y], 2)

def square(square_X, square_Y, square_Width, square_Height):
    pygame.draw.rect(gameDisplay, red, [square_X, square_Y, square_Width, square_Height])

# Main game loop
def gameloop():
    running = True
    # Variable declaration
    
    x_pos = 0
    y_pos = 0 

    start_X = display_Width/2
    start_Y = 0
    end_X = display_Width/2
    end_Y = 600

    square_X = start_X
    square_Y = 200
    square_Height = 10
    square_Width = 10

    p1_X = square_X /2
    p1_Y = square_Y
    p1_Width = 3
    p1_Height = 50

    p2_X = square_X * 1.5
    p2_Y = square_Y
    p2_Width = p1_Width
    p2_Height = p1_Height 

    left_Boundery = 6
    bottom_Boundery = 425
    top_Boundery = 3
    right_Boundery = 630 
    top_Boundery_Collide = False
    bottom_Boundery_Collide = False
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

            p2_Y = square_Y + 5

	    player1(p1_X, p1_Y, p1_Width, p1_Height)
	    player2(p2_X, p2_Y, p2_Width, p2_Height)
	    lineinthemiddle(start_X, start_Y, end_X, end_Y,)
            
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
            if random_X_Num == 0:
                square_X += 4
            elif random_X_Num == 1:
                 square_X -= 4
            
            if random_Y_Num == 0:
                square_Y -= 4
            elif random_Y_Num == 1:
                square_Y +=4
               
            # Bounderies for the ball
            # Top and bottom bounderies
            if square_Y <  top_Boundery + 7:
                top_Boundery_Collide = True
                bottom_Boundery_Collide = False
            if top_Boundery_Collide == True:
                random_Y_Num = 1
            if square_Y > bottom_Boundery + 40:
                bottom_Boundery_Collide = True
                top_Boundery_Collide = False
            if bottom_Boundery_Collide == True:
                random_Y_Num = 0 
            
            # Player collisons with the ball
            if p1_Y < square_Y + square_Height:
                if p1_X < square_X and p1_X > square_X + square_Width or p1_X + p1_Width > square_X and p1_X + square_Width > square_X + square_Width:
                    random_X_Num = 0
            if p1_Y < square_Y + square_Height:
                if p2_X > square_X and p2_X < square_X + square_Width or p2_X + p2_Width > square_X and p2_X + square_Width < square_X + square_Width:
                    random_X_Num = 1

            # If the ball goes off the right or left side of the screen
            if square_X < left_Boundery:
               square_X = start_X 
               random_X_Num = random.randint(0,1)
               random_Y_NUM = random.randint(0,1)
            if square_X > right_Boundery:
               square_X = start_X
               random_X_Num = random.randint(0,1)
               random_Y_Num = random.randint(0,1)

            square(square_X, square_Y, square_Width, square_Height)
            print(square_X, square_Y)
	    # Updating the display
	    pygame.display.update()
            clock.tick(60) 
gameloop()

pygame.quit()
quit()
