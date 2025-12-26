import glfw
from OpenGL.GL import *
import random


def main():
    stat = glfw.init()
    assert (stat != None)
    window = glfw.create_window(800, 600, "arik", None, None)
    assert (window != None)
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    pos = 0
    dir = 1
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glPushMatrix()
        glTranslatef(pos, 0, 0)

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
        pos += dir*.01
        if (pos > 1):
            dir = -1
        elif (pos < -1):
            dir = 1

        glfw.swap_buffers(window)
        glfw.poll_events()


if __name__ == "__main__":
    main()
