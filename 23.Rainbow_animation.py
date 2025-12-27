from OpenGL.GL import *
from OpenGL.GLUT import *
import math
points = []
R = 40


def rain(points, x, y, z):
    glBegin(GL_LINE_STRIP)

    glColor3f(x, y, z)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global points
    st = 0
    for j in range(8):
        tmp = [(i[0]-st, i[1]-st) for i in points]
        bit0 = j & 1
        bit1 = (j >> 1) & 1
        bit2 = (j >> 2) & 1
        rain(tmp, bit0, bit1, bit2)
        st += 0.5
    glutSwapBuffers()


def addPoints():
    global points
    if (len(points) == 91):
        points.clear()
    angle = len(points)
    x = 50+R*math.cos(math.radians(angle))
    y = 50+R*math.sin(math.radians(angle))
    points.append((x, y))
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"aa")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 100, 0, 100, 1, -1)
    glMatrixMode(GL_MODELVIEW)
    glLineWidth(10.0)
    glutDisplayFunc(draw)
    glutIdleFunc(addPoints)

    glutMainLoop()


if __name__ == "__main__":
    main()
