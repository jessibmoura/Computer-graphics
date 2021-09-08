import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = ((1,1),(1,-1),(-1,-1),(-1,1))
edges = ((0,1),(1,2),(2,3),(3,0))

def square():
  glBegin(GL_LINE_STRIP)
  # GL_POLYGON -> preencher com a cor
  # GL_LINE_STRIP -> só os traços mesmo
  for e in edges:
    for v in e:
      glVertex2iv(vertices[v])
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
    square()
    pygame.display.flip() #use to update

main()
# encerrando os módulos de PyGame

