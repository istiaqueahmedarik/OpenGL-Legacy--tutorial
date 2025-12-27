import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *

angle = 0


def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glPushMatrix()
    glRotatef(angle, 1, 1, 0)

    glBegin(GL_QUADS)

    glColor3f(1, 0, 0)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glColor3f(0, 1, 0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    glColor3f(0, 0, 1)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glColor3f(1, 0, 1)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)

    glColor3f(0, 1, 1)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    glColor3f(1, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()


def keyboard(key, x, y):
    global angle
    if (key == GLUT_KEY_LEFT):
        angle -= 1
    elif (key == GLUT_KEY_RIGHT):
        angle += 1
    print(x, y)
    glutPostRedisplay()


prevX = 0
mouseClicks = False


def mouse_click(button, state, x, y):
    global prevX, mouseClicks
    if (button == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
        mouseClicks = True
        prevX = x
    else:
        mouseClicks = False


def mouse_motion(x, y):
    global prevX, angle, mouseClicks
    if (mouseClicks == False):
        pass
    dx = x-prevX

    angle += dx*0.5

    prevX = x

    glutPostRedisplay()


def animate(value):
    global angle
    angle += 1
    glutPostRedisplay()

    glutTimerFunc(5000, animate, 0)


def idle():
    global angle
    angle += 0.1
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"arik")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(draw)
    glutSpecialFunc(keyboard)
    glutMouseFunc(mouse_click)
    glutMotionFunc(mouse_motion)
    # glutTimerFunc(5000, animate, 0)
    glutIdleFunc(idle)
    glutMainLoop()


if __name__ == "__main__":
    main()


# export PYOPENGL_PLATFORM=egl or glx
