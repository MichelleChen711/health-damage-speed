import turtle



def main():
    mt = turtle.Turtle()
    mwn = turtle.Screen()
    mscreen_width, mscreen_height = 600, 600
    mwn.setup(mscreen_width, mscreen_height)
    mt.speed(speed=0)
    mwn.tracer(0, 0)
    mt.hideturtle()
    mwn.update()
    mt.write("Welcome to HDS! \nPress Enter to input Player 1's stats then enter Player 2's!",align="center", font=("Helvetica", 22, "normal") )
    mwn.listen()

    def exit_screen():
        turtle.bye()

    mwn.onkeypress(exit_screen, 'Return')
    mwn.mainloop()

    def stat_chooser():
        t = turtle.Turtle()
        wn = turtle.Screen()

        screen_width, screen_height = 600, 600
        wn.setup(screen_width, screen_height)
        t.speed(speed=0)
        wn.tracer(0, 0)
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


        def points_left_label(x , y):
            """draws the points remaining label at x,y"""
            t.up()
            t.goto(x , y )
            t.write("Points remaining:\n            {}".format(TOTAL_POINTS), align="center", font=("Helvetica", 20, "bold"))

        def enter_label(x, y):
            """draws the press enter when finished label at x,y"""
            t.up()
            t.goto(x , y )
            t.write("Press enter when finished!", align="center", font=("Helvetica", 16, "normal"))

        my_health = health_stat(0)
        my_damage = damage_stat(0)
        my_speed = speed_stat(0)
        health, damage, speed = 0 , 0 , 0
        the_selector = selector('health')



        def update_labels():
            nonlocal the_selector
            t.clear()
            #update the labels
            my_health = health_stat(health)
            my_damage = damage_stat(damage)
            my_speed = speed_stat(speed)
            the_stat = the_selector.current_stat
            the_selector = selector(the_stat)
            t.color("black")
            points_left_label(0 , screen_height// 2 - 60)
            enter_label(0, screen_height // 3)
            #wn.update()

        def add_point():

            nonlocal TOTAL_POINTS, health, damage, speed
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
                wn.update()


        def minus_point():
            nonlocal TOTAL_POINTS, health, damage, speed

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
            wn.update()



        def move_selector_down():
            nonlocal the_selector
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
            wn.update()



        def move_selector_up():
            nonlocal the_selector

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
            wn.update()

        def done_choosing():
            nonlocal TOTAL_POINTS, health, damage, speed

            if TOTAL_POINTS == 0 and health != 0 and damage != 0 and speed != 0:
                turtle.bye()


            elif health == 0 or damage == 0 or speed == 0:
                t.up()
                update_labels()
                t.goto(0,  screen_height // 4 + 20)
                t.write("You can't have 0 points in a stat!", align="center", font=("Helvetica", 14, "bold"))

            elif TOTAL_POINTS != 0:
                t.up()
                update_labels()
                t.goto(0,  screen_height // 4 + 20)
                t.write("You still have stat points remaining!", align="center", font=("Helvetica", 14, "bold"))




        wn.listen()
        wn.onkeypress(add_point, 'Right')
        wn.onkeypress(minus_point, 'Left')
        wn.onkeypress(move_selector_up, 'Up')
        wn.onkeypress(move_selector_down, 'Down')
        wn.onkeypress(done_choosing, 'Return')


        wn.mainloop()

        return health, damage, speed

    player1_health, player1_damage, player1_speed = stat_chooser()

    #print(player1_health, player1_damage, player1_speed)

    player2_health, player2_damage, player2_speed = stat_chooser()

    #choose your character sprite
    player1_char = ""
    player2_char = ""
    ct = turtle.Turtle()
    cwn = turtle.Screen()
    cscreen_width, cscreen_height = 600, 600
    cwn.setup(cscreen_width, cscreen_height)
    ct.hideturtle()
    ct.speed(speed=0)
    cwn.tracer(0, 0)

    ct.write("Click to choose your character!\n Press enter when done!",align="center", font=("Helvetica", 22, "normal") )

    bunny_t, monkey_t, pig_t, cat_t, dog_t, chicken_t = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()

    cwn.register_shape("resources/bunny.gif")
    cwn.register_shape("resources/monkey.gif")
    cwn.register_shape("resources/pig.gif")
    cwn.register_shape("resources/cat.gif")
    cwn.register_shape("resources/dog.gif")
    cwn.register_shape("resources/chicken.gif")


    bunny_t.shape(name="resources/bunny.gif")
    monkey_t.shape(name="resources/monkey.gif")
    pig_t.shape(name="resources/pig.gif")
    cat_t.shape(name="resources/cat.gif")
    dog_t.shape(name="resources/dog.gif")
    chicken_t.shape(name="resources/chicken.gif")

    done = False
    def exit_charscreen():
        if done == True:
            turtle.bye()

        elif player1_char == '':
            ct.up()
            ct.goto(0,150)
            ct.write("Hey player1 still needs to choose a char!".format(player2_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()
        elif player2_char == '':
            ct.up()
            ct.goto(0,-150)
            ct.write("Hey player2 still needs to choose a char".format(player2_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()

    def chose_bunny(x,y):

        nonlocal player1_char, done
        if player1_char == '':
            player1_char = "bunny"
            bunny_t.goto(-cscreen_width // 3, 0)
            cwn.update()
        else:
            ct.up()
            ct.goto(0,100)
            ct.write("Hey player1 its not nice to return an adopted {}".format(player1_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()

        if player2_char != "":
            done = True

    def chose_cat(x,y):
        nonlocal player1_char, done
        if player1_char == '':
            player1_char = "cat"
            cat_t.goto(-cscreen_width // 3, 0)
            cwn.update()
        else:
            ct.up()
            ct.goto(0,100)
            ct.write("Hey player1 its not nice to return an adopted {}".format(player1_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()

        if player2_char != "":
            done = True

    def chose_chicken(x,y):
        nonlocal player1_char, done
        if player1_char == '':
            player1_char = "chicken"
            chicken_t.goto(-cscreen_width // 3, 0)
            cwn.update()
        else:
            ct.up()
            ct.goto(0,100)
            ct.write("Hey player1 its not nice to return your adopted {}".format(player1_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()

        if player2_char != "":
            done = True

    def chose_monkey(x,y):
        nonlocal player2_char, done
        if player2_char == '':
            player2_char = "monkey"
            monkey_t.goto(cscreen_width // 3, 0)
            cwn.update()
        else:
            ct.up()
            ct.goto(0,-100)
            ct.write("Hey player2 its not nice to return your adopted {}".format(player2_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()

        if player1_char != "":
            done = True

    def chose_dog(x,y):
        nonlocal player2_char, done
        if player2_char == '':
            player2_char = "dog"
            dog_t.goto(cscreen_width // 3, 0)
            cwn.update()
        else:
            ct.up()
            ct.goto(0,-100)
            ct.write("Hey player2 its not nice to return your adopted {}".format(player2_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()

        if player1_char != "":
            done = True

    def chose_pig(x,y):
        nonlocal player2_char, done
        if player2_char == '':
            player2_char = "pig"
            pig_t.goto(cscreen_width // 3, 0)
            cwn.update()
        else:
            ct.up()
            ct.goto(0,-100)
            ct.write("Hey player2 its not nice to return your adopted {}".format(player2_char), align="center", font=("Helvetica", 14, "normal"))
            cwn.update()

        if player1_char != "":
            done = True

    cwn.listen()

    #position the image turtles
    bunny_t.up()
    bunny_t.goto(-cscreen_width // 3, cscreen_height // 2 - 100)
    bunny_t.onrelease(chose_bunny)

    cat_t.up()
    cat_t.goto(0 , cscreen_height // 2 - 100)
    cat_t.onrelease(chose_cat)

    chicken_t.up()
    chicken_t.goto(cscreen_width // 3, cscreen_height // 2 - 100)
    chicken_t.onrelease(chose_chicken)

    monkey_t.up()
    monkey_t.goto(-cscreen_width // 3, -cscreen_height // 2 + 100)
    monkey_t.onrelease(chose_monkey)
    print("after monkey onrelease")

    dog_t.up()
    dog_t.goto(0, -cscreen_height // 2 + 100)
    dog_t.onrelease(chose_dog)

    pig_t.up()
    pig_t.goto(cscreen_width // 3, -cscreen_height // 2 + 100)
    pig_t.onrelease(chose_pig)

    cwn.update()
    print("after cwn.update")

    cwn.onkeypress(exit_charscreen, 'Return')
    cwn.mainloop()
    print("after cwn.mainloop")

    return player1_char, player1_health, player1_damage, player1_speed,player2_char, player2_health, player2_damage, player2_speed

print(main())