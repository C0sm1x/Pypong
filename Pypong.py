import pygame, random 

pygame.init()
# Screen dimensions
display_Radius = 640

display_Thickness = 480

# Creating the game window
gameDisplay = pygame.display.set_mode((display_Radius,display_Thickness))

# Window title
pygame.display.set_caption('Pypong')

#defing RGB colors. Red, Blue, Green I might not use them though.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

def player1(p1_X, p1_Y, p1_Radius, p1_Thickness):
	pygame.draw.rect(gameDisplay, white, [p1_X, p1_Y, p1_Radius, p1_Thickness], )

def player2(p2_X, p2_Y, p2_Radius, p2_Thickness):
	pygame.draw.rect(gameDisplay, white, [p2_X, p2_Y, p2_Radius, p2_Thickness], )

def lineinthemiddle(start_X, start_Y, end_X, end_Y):
	pygame.draw.line(gameDisplay, white, [start_X, start_Y], [end_X, end_Y], 2)

def ball(ball_X, ball_Y, ball_Radius, ball_Thickness):
    pygame.draw.circle(gameDisplay, red, (ball_X, ball_Y), ball_Radius, ball_Thickness)

# Main game loop
def gameloop():
    running = True
    # Variable declaration
    
    x_pos = 0
    y_pos = 0 

    start_X = display_Radius/2
    start_Y = 0
    end_X = display_Radius/2
    end_Y = 600

    ball_X = start_X
    ball_Y = 200
    ball_Thickness = 0
    ball_Radius = 8

    p1_X = ball_X /2
    p1_Y = ball_Y + 3
    p1_Radius = 3
    p1_Thickness = 50

    p2_X = ball_X * 1.5
    p2_Y = p1_Y 
    p2_Radius = p1_Radius
    p2_Thickness = p1_Thickness 

    left_Boundery = 6
    bottom_Boundery = 460
    top_Boundery = 3
    right_Boundery = 630 
    top_Boundery_Collide = False
    bottom_Boundery_Collide = False
    # Random numers for X and Y of the ball
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

            p2_Y = ball_Y - 5

	    player1(p1_X, p1_Y, p1_Radius, p1_Thickness)
	    player2(p2_X, p2_Y, p2_Radius, p2_Thickness)
	    lineinthemiddle(start_X, start_Y, end_X, end_Y,)
            
            # Player 1 bounderies
            # Left and right bounderies
            if p1_X > start_X - 10:
                p1_X = start_X - 10
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
            # Ball goes in a random direction at the start of the game
            if random_X_Num == 0:
                ball_X += 4
            elif random_X_Num == 1:
                 ball_X -= 4
            
            if random_Y_Num == 0:
                ball_Y -= 4
            elif random_Y_Num == 1:
                ball_Y +=4
               
            # Bounderies for the ball
            # Top and bottom bounderies
            if ball_Y <  top_Boundery:
                top_Boundery_Collide = True
                bottom_Boundery_Collide = False
            if top_Boundery_Collide == True:
                random_Y_Num = 1
            if ball_Y > bottom_Boundery:
                bottom_Boundery_Collide = True
                top_Boundery_Collide = False
            if bottom_Boundery_Collide == True:
                random_Y_Num = 0 
            
            # Player collisons with the ball
            if ball_Y >  p1_Y  and ball_Y  < p1_Y + p1_Thickness   and ball_X == p1_X:
                random_X_Num = 0
            if ball_Y >  p2_Y   and ball_Y  < p2_Y + p2_Thickness  and ball_X == p2_X:
                random_X_Num = 1

            # If the ball goes off the right or left side of the screen
            if ball_X < left_Boundery:
               ball_X = start_X 
               random_X_Num = random.randint(0,1)
               random_Y_NUM = random.randint(0,1)
            if ball_X > right_Boundery:
               ball_X = start_X
               random_X_Num = random.randint(0,1)
               random_Y_Num = random.randint(0,1)

            ball(ball_X, ball_Y, ball_Radius, ball_Thickness)

	    # Updating the display
	    pygame.display.update()
            clock.tick(60) 
gameloop()

pygame.quit()
quit()
