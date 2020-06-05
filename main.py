import turtle as t

def draw_flower():
    #changes pen color
    t.pencolor("green")

    #changes pen thickness 
    t.pensize(20)

    t.right(90)
    t.forward(150)
    t.backward(150)

    #decide the values for num_petals and num_degrees
    t.pencolor("purple")
    t.pensize(30)

    num_petals = 8
    num_degrees = int(360/8)

    #petal movement based on number of degrees
    for i in range(num_petals):
        t.forward(50)
        t.backward(50)
        t.right(num_degrees)

    t.pencolor("orange")
    t.dot(30)

draw_flower()