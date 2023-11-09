import turtle
import time

wn=turtle.Screen()
wn.title('Apasa pe Prajitura')
wn.bgcolor('grey')

wn.register_shape('cookieGIF.gif')

cookie = turtle.Turtle()
cookie.shape('cookieGIF.gif')
cookie.speed(0)

clicks = 0 

pen = turtle.Turtle()
pen.hideturtle()
pen.color('white')
pen.penup()
pen.goto(0,450)
pen.write(f'Clicks: {clicks}', align='center', font=('Courier New', 32, 'normal'))

def clicked(x,y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f'Clicks: {clicks}', align='center', font=('Courier New', 32, 'normal'))
    
    cookie.hideturtle()
    time.sleep(0.01)
    cookie.showturtle()

    
cookie.onclick(clicked)

wn.mainloop()