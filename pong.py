import pygame, sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_START_X1 = 10
PADDLE_START_Y1 = 20
PADDLE_START_X2 = SCREEN_WIDTH - 20
PADDLE_START_Y2 = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED = 10
BALL_WIDTH_HEIGHT = 16

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# This is a rect that contains the ball at the beginning it is set in the center of the screen
ball_rect = pygame.Rect((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT))

# Speed of the ball (x, y)
ball_speed = [BALL_SPEED, BALL_SPEED]

# Your paddle vertically centered on the left side
paddle_rect1 = pygame.Rect((PADDLE_START_X1, PADDLE_START_Y1), (PADDLE_WIDTH, PADDLE_HEIGHT))
paddle_rect2 = pygame.Rect((PADDLE_START_X2, PADDLE_START_Y2), (PADDLE_WIDTH, PADDLE_HEIGHT))

# Scoring: 1 point if you hit the ball, -5 point if you miss the ball
score1 = 0
score2 = 0

# Rect for clearing score
clear_rect1 = pygame.Rect((SCREEN_WIDTH/4, 5), (20, 20))
clear_rect2 = pygame.Rect((SCREEN_WIDTH*3/4, 5), (20, 20))

# Center Line
center_line = pygame.Rect((SCREEN_WIDTH/2, 0), (10, SCREEN_HEIGHT))

# Load the font for displaying the score
font = pygame.font.Font(None, 30)

# Rematch text
rematch = font.render("Rematch? (press any key)", True, (0, 0, 0))

# Render Starting
screen.fill((255, 255, 255))
pygame.draw.rect(screen, (255, 0, 0), paddle_rect1) # Player 1 paddle
pygame.draw.rect(screen, (0, 0, 255), paddle_rect2) # Player 2 paddle
pygame.draw.circle(screen, (0, 255, 0), ball_rect.center, ball_rect.width / 2) # The ball
pygame.draw.rect(screen, (255, 255, 0), center_line) # Center line
score_text1 = font.render(str(score1), True, (0, 0, 0))
score_text2 = font.render(str(score2), True, (0, 0, 0))
screen.blit(score_text1, ((SCREEN_WIDTH / 4) - font.size(str(score1))[0] / 2, 5)) # Score 1
screen.blit(score_text2, ((SCREEN_WIDTH * 3 / 4) - font.size(str(score2))[0] / 2, 5)) # Score 2
get_ready = font.render("Get Ready!", True, (0, 0, 0))
screen.blit(get_ready, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT/2 - 50)) # Get Ready!
pygame.display.flip()
pygame.time.delay(1000)

# Game loop
while True:
	# Event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
			pygame.quit()
		# Control the paddle with the mouse - DELETED FOR 2-PLAYER
		'''elif event.type == pygame.MOUSEMOTION:
			paddle_rect1.centery = event.pos[1]
			# correct paddle position if it's going out of window
			if paddle_rect1.top < 0:
				paddle_rect1.top = 0
			elif paddle_rect1.bottom >= SCREEN_HEIGHT:
				paddle_rect1.bottom = SCREEN_HEIGHT'''

	# This test if up or down keys are pressed; if yes, move the paddle
	if pygame.key.get_pressed()[pygame.K_UP] and paddle_rect2.top > 0:
		paddle_rect2.top -= BALL_SPEED
	elif pygame.key.get_pressed()[pygame.K_DOWN] and paddle_rect2.bottom < SCREEN_HEIGHT:
		paddle_rect2.top += BALL_SPEED
	elif pygame.key.get_pressed()[pygame.K_w] and paddle_rect1.top > 0:
		paddle_rect1.top -= BALL_SPEED
	elif pygame.key.get_pressed()[pygame.K_s] and paddle_rect1.bottom < SCREEN_HEIGHT:
		paddle_rect1.top += BALL_SPEED
	elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
		sys.exit(0)
		pygame.quit()
		
	# Update ball position
	ball_rect.left += ball_speed[0]
	ball_rect.top += ball_speed[1]

	# Ball collision with rails
	if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
		ball_speed[1] = -ball_speed[1]
	# Player 1 scores
	if ball_rect.right >= SCREEN_WIDTH:
		score1 += 1
		pygame.time.delay(500)
		ball_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
		if score1 == 11:
		    pygame.draw.rect(screen, (255, 255, 255), clear_rect1) # Clears score of 10
		    score_text1 = font.render(str(score1), True, (0, 0, 0))
		    screen.blit(score_text1, ((SCREEN_WIDTH / 4) - font.size(str(score1))[0] / 2, 5))
		    win_text1 = font.render("Player 1 Wins!", True, (0, 0, 0))
		    screen.blit(win_text1, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT/2 - 50))
		    screen.blit(rematch, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT/2))
		    pygame.display.flip()
		    loopy = True
		    while loopy:
		        for event in pygame.event.get():
		            if event.type == pygame.QUIT:
		                pygame.quit()
		                sys.exit()
		            elif event.type == pygame.KEYDOWN:
		                loopy = False
		    score1 = 0
		    score2 = 0
		    
	# Player 2 scores
	if ball_rect.left <= 0:
	    score2 += 1
	    pygame.time.delay(500)
	    ball_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	    if score2 == 11:
	        pygame.draw.rect(screen, (255, 255, 255), clear_rect2) # Clears score of 10
	        score_text2 = font.render(str(score2), True, (0, 0, 0))
	        screen.blit(score_text2, ((SCREEN_WIDTH*3 / 4) - font.size(str(score2))[0] / 2, 5))
	        win_text2 = font.render("Player 2 Wins!", True, (0, 0, 0))
	        screen.blit(win_text2, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT/2 - 50))
	        screen.blit(rematch, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT/2))
	        pygame.display.flip()
	        loopy = True
	        while loopy:
	            for event in pygame.event.get():
	                if event.type == pygame.QUIT:
	                    pygame.quit()
	                    sys.exit()
	                elif event.type == pygame.KEYDOWN:
		                loopy = False
		    score1 = 0
		    score2 = 0
		    
	# Test if the ball is hit by the paddle; if yes reverse speed and add a point
	if paddle_rect1.colliderect(ball_rect) or paddle_rect2.colliderect(ball_rect):
		ball_speed[0] = -ball_speed[0]
		pygame.mixer.Sound("Funk.wav").play()
	
	# Clear screen
	screen.fill((255, 255, 255))

	# Render the ball, the paddle, and the score
	pygame.draw.rect(screen, (255, 0, 0), paddle_rect1) # Player 1 paddle
	pygame.draw.rect(screen, (0, 0, 255), paddle_rect2) # Player 2 paddle
	pygame.draw.circle(screen, (0, 255, 0), ball_rect.center, ball_rect.width / 2) # The ball
	pygame.draw.rect(screen, (255, 255, 0), center_line) # Center line
	score_text1 = font.render(str(score1), True, (0, 0, 0))
	score_text2 = font.render(str(score2), True, (0, 0, 0))
	screen.blit(score_text1, ((SCREEN_WIDTH / 4) - font.size(str(score1))[0] / 2, 5)) # Score 1
	screen.blit(score_text2, ((SCREEN_WIDTH * 3 / 4) - font.size(str(score2))[0] / 2, 5)) # Score 2
	
	# Update screen and wait 20 milliseconds
	pygame.display.flip()
	pygame.time.delay(20)
