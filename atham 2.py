from turtle import *
sc=Screen()
sc.setup(800,600)
sc.bgcolor("black")
color("red")
up()
ht()
sety(-250)
setx(0)
st()
down()
fillcolor("#ff0000")
begin_fill()
speed(0)
r = 270
circle(r)
end_fill()
#2nd
up()
ht()
sety(-220)
setx(0)
st()
down()
color("yellow")

fillcolor("yellow")
begin_fill()
r = 240
circle(r)
end_fill()
#3rd
#star
window = Screen()
window.bgcolor('black')
up()
ht()
sety(20)
setx(0)
st()
down()
speed(0)
for j in range(10):
	begin_fill()  
	right(360/10)
	color('#008000')
	for i in range(4):
		forward(180)
		left(90)
	end_fill()
#4th
up()
ht()
sety(-183)
setx(0)
st()
down()
fillcolor("white")
begin_fill()
r = 203
circle(r)
end_fill()
#5th
up()
ht()
sety(-125)
setx(2)
st()
down()
fillcolor("#d4fc79")
begin_fill()
r = 144
circle(r)
end_fill()

def draw_petal(radius,c):   
    head = heading()
    fillcolor(c)
    begin_fill()
    circle(radius, 90)
    left(120)
    circle(radius, 90)
    setheading(head)
    end_fill()
my_radius = 143
my_petals = 12
a=["#ff6a18","#800080","blue","#ff6a18","#800080","blue","#ff6a18","#800080","blue","#ff6a18","#800080","blue"]
up()
ht()
sety(-123)
setx(-142)
st()
down()
for _ in range(my_petals):
    draw_petal( my_radius,a[_])
    left(360 / my_petals)
up()
ht()
sety(3)
setx(0)
st()
down()
fillcolor("white")
begin_fill()
r = 16
circle(r)
end_fill()
hideturtle()




