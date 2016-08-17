import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600                                                                                                                                                                                                                                                                                                                                        
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City Scroller")
done = False
clock = pygame.time.Clock()

class Building():
    def __init__(self, x_point, y_point, width, height, color): 
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color
        
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x_point,  self.y_point, self.width, self.height])

    def move(self, speed):
        #self.x_point += speed
        # The speed is - just so it goes right to left with scrolling, this will allow the rest of the functions to work properly, having + cuts off the repeatition 
        self.x_point -= speed 
             
                  
class Scroller(object):
    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.building_list = []
        self.add_buildings()
                   
    def add_buildings(self):
        a = 0
##        while a < self.width:
##            self.add_building(a)
##            a += self.building_list[-1].width

        # I made the while loop be < = instead of just <, so it could go until the full width of the scroller

        while a <= self.width:
            self.add_building(a)
            a += self.building_list[-1].width    

    def add_building(self, x_location):
        w = random.randint(20, 70)
        h = random.randint(100,300)
        y_location = self.base- h
        self.building_list.append(Building(x_location, y_location, w , h , self.color))

    def draw_buildings(self):
        for b in self.building_list:
            b.draw()

    def move_buildings(self):
        for m in self.building_list:
            m.move(self.speed)             
        new_x_loc = self.building_list[-1].x_point + self.building_list[-1].width
        self.add_building(new_x_loc)

             
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here

    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
