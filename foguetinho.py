from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import pygame

def bico():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,1.0,0.0) #cor amarela
    glVertex3f(0.3, 0.6, 0.0)
    glVertex3f(0.4, 0.8, 0.0)
    glVertex3f(0.5, 0.6, 0.0)
    glEnd()

def tronco():
    glBegin(GL_QUADS)
    glColor3f(0,0,1.0) #cor azul escuro
    glVertex3f(0.3, 0.1, 0.0)
    glVertex3f(0.5, 0.1, 0.0)
    glVertex3f(0.5, 0.6, 0.0)
    glVertex3f(0.3, 0.6, 0.0)
    glEnd()

def asaEsqueda():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.15, 0.1, 0.0)
    glVertex3f(0.3, 0.1, 0.0)
    glVertex3f(0.3, 0.3, 0.0)
    glEnd()

def asaDireita():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.5, 0.1, 0.0)
    glVertex3f(0.65, 0.1, 0.0)
    glVertex3f(0.5, 0.3, 0.0)
    glEnd()

def foguete():
    bico()
    tronco()
    asaEsqueda()
    asaDireita()

def main():
    pygame.init() #inicializa o pygame
    tela = pygame.display.set_mode([700,600],DOUBLEBUF | OPENGL) #two images at any given time - one that we can see and one that we can transform as we see fit
    pygame.display.set_caption("Foguetinho maneiro")
    relogio = pygame.time.Clock() #atualiza a minha tela no tempo que eu passo

    glTranslatef(-0.50,-1,0.0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        relogio.tick(30)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #isso aqui é para limpar o antigo desenho assim que "atualizar" a nova posição dele
        glTranslatef(0,0.1,0) #movimenta o foguetinho
        foguete() #chama o foguetinho aí
        pygame.display.flip() #updates the window with the active buffer content
        pygame.time.wait(100) #function that pauses the program for a period of time

    pygame.quit()

if __name__ == "__main__":
    main()
