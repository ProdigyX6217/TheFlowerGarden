import turtle as t

# draw a simple rectangle car with two wheels.
def draw_flower(x,y):
  
  t.penup()
  t.setheading(90)
  t.goto(x,y)
  t.pendown()
  
  t.pencolor("green")
  t.pensize(10)
  t.left(90)
  t.backward(150)
  t.forward(150)
  
  t.pencolor("black")
  t.pensize(15)
  
  num_petals = 8
  num_degrees = int(360/8)
  
  for i in range(num_petals):
    t.forward(50)
    t.backward(50)
    t.left(num_degrees)
    
  t.pencolor("orange")
  t.dot(20)
  
  t.penup()
  t.setheading(90)
  t.goto(x+200,y)
  t.pendown()

  t.pencolor("black")
  t.pensize(15)

  num_petals = 8
  num_degrees = int(360/8)
  
  for i in range(num_petals):
    t.forward(50)
    t.backward(50)
    t.left(num_degrees)
    
  t.pencolor("orange")
  t.dot(20)

#call draw_flower
draw_flower(0,0)