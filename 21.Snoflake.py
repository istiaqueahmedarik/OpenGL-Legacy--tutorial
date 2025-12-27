import random
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def snowFlake(x1, y1, x2, y2, d=5):
    # tin vage vag korbo
    # ax2+bx1
    if d == 0:
        glBegin(GL_LINES)
        glColor3f(1, 1, 1)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        return
    x13 = 2*x1+x2
    x13 /= 3
    y13 = 2*y1+y2
    y13 /= 3

    x23 = 1*x1+2*x2
    x23 /= 3
    y23 = 1*y1+2*y2
    y23 /= 3

    dx = x23-x13
    dy = y23-y13
    angle = math.pi/3

    xPeak = x13+dx*math.cos(angle)-dy*math.sin(angle)
    yPeak = y13+dx*math.sin(angle)+dy*math.cos(angle)

    snowFlake(x1, y1, x13, y13, d-1)
    snowFlake(x13, y13, xPeak, yPeak, d-1)
    snowFlake(xPeak, yPeak, x23, y23, d-1)
    snowFlake(x23, y23, x2, y2, d-1)


snowflakes = []


def init_snowflakes():
    for _ in range(30):
        snowflakes.append([
            random.uniform(0, 100),
            random.uniform(0, 100),
            random.uniform(0.1, 0.25),
            random.uniform(0.1, 0.3)
        ])


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if not snowflakes:
        init_snowflakes()

    for flake in snowflakes:
        glPushMatrix()
        glTranslatef(flake[0], flake[1], 0)
        glScalef(flake[2], flake[2], 1)
        glTranslatef(-50, -50, 0)

        x1, y1 = 20, 70
        x2, y2 = 80, 70
        x3, y3 = 50, 18

        snowFlake(x1, y1, x2, y2, 2)
        snowFlake(x2, y2, x3, y3, 2)
        snowFlake(x3, y3, x1, y1, 2)
        glPopMatrix()

        flake[1] -= flake[3]
        if flake[1] < -20:
            flake[1] = 120
            flake[0] = random.uniform(0, 100)

    glutSwapBuffers()
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGBA)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"arik")
    glutDisplayFunc(draw)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(0, 100, 0, 100, 1, -1)
    glMatrixMode(GL_MODELVIEW)
    glutMainLoop()


if __name__ == "__main__":
    main()
