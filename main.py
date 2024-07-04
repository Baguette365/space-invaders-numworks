from random import *
from time import *
from kandinsky import *
from ion import *
x=50
y=50
fill_rect(0,0,320,222,'black')
class star:
  def __init__(self,x):
    self.x=x
    self.y=0
a=star(10)
b=star(10)
c=star(10)
d=star(10)
e=star(30)
def Stars():
  a.y+=1
  b.y+=1
  c.y+=1
  d.y+=1
  e.y+=1
  fill_rect(randint(1,320),randint(1,222),2,2,color(255,255,255))
  fill_rect(randint(1,320),randint(1,222),2,2,color(255,255,255))
  fill_rect(randint(1,320),randint(1,222),2,2,color(255,255,255))
  fill_rect(randint(1,320),randint(1,222),2,2,color(255,255,255))
  fill_rect(randint(1,320),randint(1,222),2,2,color(255,255,255))
  fill_rect(randint(1,320),randint(1,222),2,2,color(0,0,0))
  fill_rect(randint(1,320),randint(1,222),2,2,color(0,0,0))
  fill_rect(randint(1,320),randint(1,222),2,2,color(0,0,0))
  fill_rect(randint(1,320),randint(1,222),2,2,color(0,0,0))
  fill_rect(randint(1,320),randint(1,222),4,4,color(255,255,255))
  fill_rect(randint(1,320),randint(1,222),2,2,color(0,0,0))
def draw_player():
  fill_rect(x,y-5,25,-10,color(200,200,200))
  fill_rect(x+5,y-15,15,-5,color(200,200,200))
  fill_rect(x+5,y-20,5,-10,color(200,200,200))
  fill_rect(x+15,y-20,5,-10,color(200,200,200))
  fill_rect(x+15,y-25,5,-5,color(255,15,0))
  fill_rect(x+5,y-25,5,-5,color(255,15,0))
def draw_bullet():
  fill_rect(x+5,y-25,5,-500,'red')
  fill_rect(x+15,y-25,5,-500,'red')
def move_player():
  global x
  global y
  if keydown(KEY_LEFT):
    fill_rect(x,y,25,-30,'black')
    x-=5
  if keydown(KEY_UP):
    fill_rect(x,y,25,-30,'black')
    y-=5
  if keydown(KEY_DOWN):
    fill_rect(x,y,25,-30,'black')
    y+=5
  if keydown(KEY_RIGHT):
    fill_rect(x,y,25,-30,'black')
    x+=5
def init_enemy():
  global epv
  global ex
  global ey
  ex=randint(1,44)*5
  ey=-30
  epv=3
def draw_enemy():
  global ex
  global ey
  fill_rect(ex,ey,25,30,color(255,255,255))
  fill_rect(ex+5,ey+5,15,20,color(0,0,0))
  fill_rect(ex+10,ey+10,5,5,color(255,255,255))
  fill_rect(ex+5,ey,5,5,color(255,255,255))
  fill_rect(ex+15,ey+30,5,5,color(255,255,255))
  fill_rect(ex+5,ey+30,5,5,color(255,255,255))
  ey+=7

init_enemy()
def refresh_screen():
  global ey
  global ex
  fill_rect(ex,ey,30,-30,color(0,0,0))
  fill_rect(x+15,y-25,5,-500,'black')
  fill_rect(x+10,y-25,5,-500,'black')
  fill_rect(x+15,y-25,5,-500,'black')
  fill_rect(x+5,y-25,5,-500,'black')
z=1
vie=3
while True:
  if x>320:
    break
  if y>222:
    break
  if y<0:
    break
  if x<0:
    break
  z=str(z)
  draw_enemy()
  if keydown(KEY_OK):
    draw_bullet()
    if x==ex:
      fill_rect(ex,ey,50,50,color(0,0,0))
      fill_rect(ex,ey,50,-50,color(0,0,0))
      ey=-30
      ex=randint(1,44)*5
      z=int(z)
      z+=1
      z=str(z)
  sleep(0.1)
  refresh_screen()
  move_player()
  draw_player()
  print(ex)
  print(x)
  Stars()
  z=str(z)
  vie=str(vie)
  if ey>=222:
    vie=int(vie)
    vie-=1
    vie=str(vie)
    ey=-30
    ex=randint(1,44)*5
  if x==ex and y==ey:
    vie=int(vie)
    vie-=1
    vie=str(vie)
  draw_string("score: "+z,0,0)
  draw_string("vie : "+vie,250,0)
  if vie=="0":
    break
draw_string("perdu !",50,111)