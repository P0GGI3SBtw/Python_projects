import turtle as trt

screen = trt.Screen()
screen.setup(800, 600)
trt.bgcolor('black')
trt.color('blue')
trt.speed(150)
trt.right(45)

for i in range(150):
    trt.circle(25)
    if 7 < i < 62:
        trt.left(5)
    if 80 < i < 133:
        trt.right(5)
    if i < 80:
        trt.forward(10)
    else:
        trt.forward(5)
