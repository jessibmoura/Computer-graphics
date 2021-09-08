import pygame
from pygame.locals import *
from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

def circle():
  posx, posy = 0,0    
  sides = 32    
  radius = 0.5    
  glBegin(GL_POLYGON)    
  for i in range(100):    
      cosine= radius * cos(i*2*pi/sides) + posx    
      sine  = radius * sin(i*2*pi/sides) + posy    
      glVertex2f(cosine,sine)
  glEnd()

def main():
  pygame.init()
  display = (500,500)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

  gluPerspective(40,display[0]/display[1],1,10)
  glTranslatef(0.0,0.0,-5)

  while True:
  #checando eventos
    for event in pygame.event.get():
    #se for um evento quit
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    circle()
    pygame.display.flip() #use to update

main()
# encerrando os módulos de PyGame