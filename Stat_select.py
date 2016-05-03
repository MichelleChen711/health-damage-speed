import turtle


t = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
screen_width, screen_height = 600, 600
wn.setup(screen_width, screen_height)
wn.tracer(1)
t.hideturtle()
wn.update()

TOTAL_POINTS = 20


def points_left_label(x , y):
    """draws the points remaining label at x,y"""
    t.up()
    t.goto(x , y )
    t.write("Points remaining:\n {}".format(TOTAL_POINTS), align="center", font=("Arial", 14, "normal"))


class health_stat:

    def __init__(self, points_allocated):
        self.points = points_allocated
        self.x = - screen_width // 4
        self.y =  screen_height // 4
        self.width = 360
        self.height = 44
        self.boxwidth = self.get_box_width()
        self.draw_empty_rect(t, color = "black")

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
            t.forward(self.boxwidth)
            t.right(90)
            t.forward(self.height)
            t.right(90)
        self.x += self.boxwidth

        t.end_fill()

my_health = health_stat(5)

def add_point():
    my_health.points += 1
    my_health.draw_filled_rect(t)
    print("called")

wn.listen()
wn.onkeypress(add_point, 'space')
wn.update()

wn.mainloop()