import turtle

n = int(input("n: "))		# Enter number of digits of pi you want
velocity = float(input("Enter the velocity of the big block: "))
collisions = 0

# Set up the screen
wn = turtle.Screen()
wn.setup(width=800, height=500)
wn.bgcolor("black")
wn.title("Pie")
wn.tracer(0)
#turtle.delay(0.00000001)

# Set up the pen to draw
pen = turtle.Turtle()
pen.setposition(-230,100)
pen.hideturtle()
pen.speed(0)

pen.color('white')
pen.right(90)
pen.fd(110)
pen.left(90)
pen.fd(700)

blocks = []
for _ in range(2):
	blocks.append(turtle.Turtle())

mass1 = 1
mass2 = 100**(n-1)

# Setting up the score bar
collisions_pen = turtle.Turtle()
collisions_pen.speed(0)
collisions_pen.color("white")
collisions_pen.penup()
collisions_pen.setposition(-290, 200)
scorestring = "Collisions: %s" %collisions
collisions_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))
collisions_pen.hideturtle()

# Setting up the smaller block
blocks[0].shape('square')
blocks[0].color('yellow')
blocks[0].shapesize(1, 1)
blocks[0].penup()
blocks[0].setposition(0, 0)
blocks[0].speed(0)
blocks[0].dx = 0.0

# Setting up the bigger block
blocks[1].shape('square')
blocks[1].shapesize(n, n)
blocks[1].color('green')
blocks[1].penup()
blocks[1].speed(0)
blocks[1].setposition(100, 10*(n-1))
blocks[1].dx = velocity

# Create a function to determine the coliisions
def isCollision(t1, t2):
	distance = abs(t1.xcor()-t2.xcor())

	if distance <= 10*(n+1):
		return True
	else:
		return False

# Updating the positions of the blocks
while True:
	wn.update()

	blocks[0].setx(blocks[0].xcor() + blocks[0].dx)
	blocks[1].setx(blocks[1].xcor() + blocks[1].dx)

	if blocks[0].xcor() < -220:
		blocks[0].dx *= -1
		collisions += 1
		scorestring = "Collisions: %s" %collisions
		collisions_pen.clear()
		collisions_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))

	# Set the velocities of the blocks after each collision
	M = mass1 + mass2
	vel1 = (mass1 - mass2)/M * blocks[0].dx
	vel1 += 2*mass2/M * blocks[1].dx

	vel2 = (mass2 - mass1)/M * blocks[1].dx
	vel2 += 2*mass1/M * blocks[0].dx

	if isCollision(blocks[0], blocks[1]):
		blocks[0].dx = vel1
		blocks[1].dx = vel2
		collisions += 1

		scorestring = "Collisions: %s" %collisions
		collisions_pen.clear()
		collisions_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))

turtle.exitonclick(0)
