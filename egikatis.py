from visual import *
from math import sin, cos
initialHeight = 4.6
initialVelocity = 16  # Atis hizi
Angle = 80  # Atis Acisi
scene1 = display(title="Calisma",
                 x=0, y=0, width=800, height=600,
                 range=10, background=color.yellow,
                 center=(10, 10, 0))
ball = sphere(pos=(0, initialHeight, 0), radius=0.35, color=color.green, make_trail=true)  # Top
floor = box(pos=(0, 0, 0), size=(200,10, 10))  # Zemin
t = 0
dt = 0.0001
g = -9.8  # Yer cekimi ivmesi
Fgrav = vector(0, g * dt, 0)
ballv = vector(initialVelocity * cos(Angle * pi / 180), initialVelocity * sin(Angle * pi / 180), 0)
s = 0
while s < 6:
    while ball.y >= 0:
        rate(10000)  # Topun hizi
        ballv = ballv + Fgrav
        ball.pos += ballv * dt
        if (ball.y<4.6) :
            print s+1,"Topun Pozisyonu=", ball.pos, "t= ", t
            kova=ball.x
            break
    initialVelocity = initialVelocity * 0.75
    if initialVelocity < 50:
        initialHeight = (2 * (initialVelocity * sin(Angle * pi / 180)) / g)
    ball = sphere(pos=(0, initialHeight, 0), radius=0.35, color=color.green, make_trail=true)  # Top
    floor = box(pos=(0, 0, 0), size=(200,10, 10))  # Zemin
    Fgrav = vector(0, g * dt, 0)
    ballv = vector(initialVelocity * cos(Angle * pi / 180), initialVelocity * sin(Angle * pi / 180), 0)
    ball.y=4.6
    ball.x=kova
    s += 1
