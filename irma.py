import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    file = open("data/irma.csv")
    read = file.readlines()

    for i in range(1, len(read)):
        line = read[i] 
        splitline = line.split(",")
        lat = float(splitline[2])
        lon = float(splitline[3])
        wind = float(splitline[4])
        
        # if statement uses the wind as miles per hour and then goes underneath the category and color of the hurricane.
        # colors of the hurricanes are based on categories 1-5 and changes the size of the turtle.
        if wind < 74:
            cat = 0
            t.pensize(1)
            t.color("white")           
        elif wind >= 74 and wind <= 95:
            t.pensize(2)
            t.color("blue")
            cat = 1           
        elif wind >= 96 and wind <= 110:
            t.pensize(3)
            t.color("green")
            cat = 2           
        elif wind >= 110 and wind <= 129:
            t.pensize(4)
            t.color("yellow")
            cat = 3          
        elif wind >= 130 and wind <= 156:
            t.pensize(5)
            t.color("orange")
            cat = 4         
        elif wind >= 158:
            t.pensize(6)
            t.color("red")
            cat = 5
        t.goto(lon, lat)
        t.write(str(cat))
    turtle.Screen().exitonclick()
        
        
                
if __name__ == "__main__":
    irma()
    
