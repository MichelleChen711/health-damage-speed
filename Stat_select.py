import turtle


t = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
screen_width, screen_height = 600, 600
wn.setup(screen_width, screen_height)
wn.tracer(0)
t.hideturtle()
wn.update()

TOTAL_POINTS = 20
t.up()
t.goto(0, screen_height // 3  )
t.write("Use the arrow keys to add stats!".format(TOTAL_POINTS), align="center", font=("Helvetica", 16, "normal"))



class health_stat:
    def __init__(self, points_allocated):
        self.points = points_allocated
        self.x = - screen_width // 4
        self.y =  screen_height // 4
        self.width = 360
        self.height = 44

        #draw and label it
        self.draw_empty_rect(t, color = "black")

        self.health_label()

        #for creating and tracking stat meter position
        self.boxwidth = self.get_box_width()
        self.draw_filled_rect(t)

    def health_label(self):
        """draws the points remaining label at x,y"""
        t.up()
        t.goto(self.x - 70, self.y - 30)
        t.write("Health: {}".format(self.points), align="center", font=("Helvetica", 14, "bold"))

    def get_box_width(self):
        return self.width // 18


    def draw_empty_rect(self, t, color="black"):
        """Draws a filled rect with its top left corner at x,y"""
        t.color(color)
        t.up()
        #make the frame a little bigger than the filling
        t.goto(self.x - 1, self.y + 1)
        t.setheading(0)  # Face right
        t.down()
        for side in range(2):
            t.forward(self.width + 2)
            t.right(90)
            t.forward(self.height + 2)
            t.right(90)

    def draw_filled_rect(self, t, color="green"):
        """Draws a filled rect with its top left corner at x,y"""
        t.color(color)
        t.fillcolor(color)
        t.begin_fill()
        t.up()
        t.goto(self.x, self.y)
        t.setheading(0)  # Face right
        t.down()
        for side in range(2):
            t.forward(self.boxwidth * self.points)
            t.right(90)
            t.forward(self.height)
            t.right(90)


        t.end_fill()

class damage_stat():

    def __init__(self, points_allocated):
        self.points = points_allocated
        self.x = - screen_width // 4
        self.y = 0
        self.width = 360
        self.height = 44

        #draw and label it
        self.draw_empty_rect(t, color = "black")
        self.damage_label()

        #for creating and tracking stat meter position
        self.boxwidth = self.get_box_width()
        self.draw_filled_rect(t)


    def damage_label(self):
        """draws the points remaining label at x,y"""
        t.up()
        t.goto(self.x - 70, self.y - 30)
        t.write("Damage: {}".format(self.points), align="center", font=("Helvetica", 14, "bold"))

    def get_box_width(self):
        return self.width // 18


    def draw_empty_rect(self, t, color="black"):
        """Draws a filled rect with its top left corner at x,y"""
        t.color(color)
        t.up()
        #make the frame a little bigger than the filling
        t.goto(self.x - 1, self.y + 1)
        t.setheading(0)  # Face right
        t.down()
        for side in range(2):
            t.forward(self.width + 2)
            t.right(90)
            t.forward(self.height + 2)
            t.right(90)

    def draw_filled_rect(self, t, color="red"):
        """Draws a filled rect with its top left corner at x,y"""
        t.color(color)
        t.fillcolor(color)
        t.begin_fill()
        t.up()
        t.goto(self.x, self.y)
        t.setheading(0)  # Face right
        t.down()
        for side in range(2):
            t.forward(self.boxwidth * self.points)
            t.right(90)
            t.forward(self.height)
            t.right(90)
        t.end_fill()


class speed_stat:
    def __init__(self, points_allocated):
        self.points = points_allocated
        self.x = - screen_width // 4
        self.y = - screen_width // 4
        self.width = 360
        self.height = 44

        #draw and label it
        self.draw_empty_rect(t, color = "black")

        self.speed_label()

        #for creating and tracking stat meter position
        self.boxwidth = self.get_box_width()
        self.draw_filled_rect(t)


    def speed_label(self):
        """draws the points remaining label at x,y"""
        t.up()
        t.goto(self.x - 70, self.y - 30)
        t.write("Speed: {}".format(self.points), align="center", font=("Helvetica", 14, "bold"))

    def get_box_width(self):
        return self.width // 18


    def draw_empty_rect(self, t, color="black"):
        """Draws a filled rect with its top left corner at x,y"""
        t.color(color)
        t.up()
        #make the frame a little bigger than the filling
        t.goto(self.x - 1, self.y + 1)
        t.setheading(0)  # Face right
        t.down()
        for side in range(2):
            t.forward(self.width + 2)
            t.right(90)
            t.forward(self.height + 2)
            t.right(90)

    def draw_filled_rect(self, t, color="blue"):
        """Draws a filled rect with its top left corner at x,y"""
        t.color(color)
        t.fillcolor(color)
        t.begin_fill()
        t.up()
        t.goto(self.x, self.y)
        t.setheading(0)  # Face right
        t.down()
        for side in range(2):
            t.forward(self.boxwidth * self.points)
            t.right(90)
            t.forward(self.height)
            t.right(90)

        t.end_fill()




class selector:
    """selects the stat to be adjusted"""
    def __init__(self, stat):

        self.x = - screen_width // 3 - 80  #initialize it around the health stat
        #the y value depends on the current stat
        if stat == 'health':
            self.y =  screen_width // 3 - 35
        elif stat == 'damage':
            self.y =  15
        else:
            self.y =  - screen_width // 4 + 15

        self.current_stat = stat
        self.width = 510  #must be big enough to frame the stat bars (size 360)
        self.height = 75
        self.draw_empty_rect(t, color = "black")



    def draw_empty_rect(self, t, color="black"):
        """Draws a filled rect with its top left corner at x,y"""
        t.color(color)
        t.up()
        #make the frame a little bigger than the filling
        t.goto(self.x - 1, self.y + 1)
        t.setheading(0)  # Face right
        t.down()
        for side in range(2):
            t.forward(self.width + 2)
            t.right(90)
            t.forward(self.height + 2)
            t.right(90)
        wn.update()




def points_left_label(x , y):
    """draws the points remaining label at x,y"""
    t.up()
    t.goto(x , y )
    t.write("Points remaining:\n            {}".format(TOTAL_POINTS), align="center", font=("Helvetica", 20, "bold"))


my_health = health_stat(0)
my_damage = damage_stat(0)
my_speed = speed_stat(0)
health, damage, speed = 0 , 0 , 0
the_selector = selector('health')



def update_labels():
    global the_selector
    t.clear()
    #update the labels
    my_health = health_stat(health)
    my_damage = damage_stat(damage)
    my_speed = speed_stat(speed)
    the_stat = the_selector.current_stat
    the_selector = selector(the_stat)
    t.color("black")
    points_left_label(0 , screen_height// 2 - 60)
    wn.update()

def add_point():

    global TOTAL_POINTS, health, damage, speed
    if TOTAL_POINTS > 0:
        if the_selector.current_stat == 'health' and health < 18:
            #clear the old turtles

            TOTAL_POINTS -= 1
            health += 1
            #redraw the screen with updated label and health
            update_labels()

        elif the_selector.current_stat == 'damage' and damage < 18:
            #clear the old turtles

            TOTAL_POINTS -= 1
            damage += 1
            #redraw the screen with updated label and health
            update_labels()
        elif the_selector.current_stat == 'speed' and speed < 18:
            #clear the old turtles

            TOTAL_POINTS -= 1
            speed += 1
            #redraw the screen with updated label and health
            update_labels()


def minus_point():
    global TOTAL_POINTS, health, damage, speed

    if the_selector.current_stat == 'health' and health > 0:

        TOTAL_POINTS += 1
        health -= 1
        #redraw the screen with updated labels
        update_labels()

    elif the_selector.current_stat == 'damage' and damage > 0:


        TOTAL_POINTS += 1
        damage -= 1
        #redraw the screen with updated labels
        update_labels()

    elif the_selector.current_stat == 'speed' and speed > 0:
        #clear the old turtles

        TOTAL_POINTS += 1
        speed -= 1
        #redraw the screen with updated label and health
        update_labels()




def move_selector_down():
    global the_selector
    if the_selector.current_stat == 'health':
        #draw the selector at the new pos

        the_selector = selector("damage")
        update_labels()


    elif the_selector.current_stat == 'damage':
        #draw the selector at the new pos

        the_selector = selector("speed")
        update_labels()

    else:
        #there are no stats below speed
        pass



def move_selector_up():
    global the_selector

    if the_selector.current_stat == 'health':
        #there are no stats above health
        pass

    elif the_selector.current_stat == 'damage':
        #draw the selector at the new pos
        the_selector = selector("health")
        update_labels()



    else:
        #draw the selector at the new pos

        the_selector = selector("damage")
        update_labels()




wn.listen()
wn.onkeypress(add_point, 'Right')
wn.onkeypress(minus_point, 'Left')
wn.onkeypress(move_selector_up, 'Up')
wn.onkeypress(move_selector_down, 'Down')
wn.update()

wn.mainloop()