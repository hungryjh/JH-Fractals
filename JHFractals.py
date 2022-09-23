############################################################################################
# By Jack Harris (@hungryjh), 2022 - For free use, but recognition would be appreciated :) #
############################################################################################


# Standard Imports
import sys
import math
import colorsys


# Requires Pygame
import pygame
pygame.init()


#Variables to change
fps = 60
width, height = 600, 400
backgroundColour = (0,0,0)
mouse_visible = True
max_iterations = 10 #Wouldn't suggest more than ~15, gets exponentially more intensive


#Pygame Window Init
screen = pygame.display.set_mode((width, height))
fpsClock = pygame.time.Clock()
pygame.mouse.set_visible(mouse_visible)


#Function to Colour the fractal
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))


#Recursive Fractal function
def fractal(iteration, angle, angle_diff, start_pos, max_iterations):

    #Get the attributes of this branch
    colour = hsv2rgb(iteration / max_iterations,1,1)
    length = height / max_iterations
    angle = angle + angle_diff
    
    #End pos is the branch length at an angle
    end_pos = (start_pos[0] + math.cos(math.radians(angle)) * length, start_pos[1] + math.sin(math.radians(angle)) * length)

    #Draw the branch
    pygame.draw.line(screen, colour, start_pos, end_pos)
    
    #Call the function recursively twice one for each branch
    #Note: Can call it with angle-angle_diff for a third branch, I imagine you could use a scalar there for n number of braches, but I like 2 :)
    iteration += 1
    if iteration < max_iterations:
        fractal(iteration, angle, angle_diff, end_pos, max_iterations)
        fractal(iteration, angle - angle_diff * 2, angle_diff, end_pos, max_iterations)



#Main loop
while True:
    x, y = pygame.mouse.get_pos()
    screen.fill(backgroundColour)

    #Mouse y -> Number of iterations
    number_of_iterations = (height - y) / height * max_iterations + 1 #Make this an int to have size snap not shrink and grow
 
    #Mouse x -> angle between each pair of 'branches'
    angle_diff = (x / width - 0.5)* 360


    #Make a fractal with the angle and iterations, centered at the bottom middle of the screen
    #Note: 270 - angle_diff keeps it facing upright
    fractal(1, 270 - angle_diff, angle_diff, (width/2, height), number_of_iterations)

    #Make the exit button... exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
  
    pygame.display.flip()
    fpsClock.tick(fps)
