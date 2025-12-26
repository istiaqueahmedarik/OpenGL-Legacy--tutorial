import glfw
from OpenGL.GL import *


def main():
    stat = glfw.init()
    assert (stat != None)

    window = glfw.create_window(800, 600, "arik", None, None)
    assert (window != None)

    angle = 0
    sc = 0
    dir = 1
    step = 0.01
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(angle, 0, 1, 0)
        glScalef(sc, sc, sc)
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)
        glVertex3f(-0.25, 0.5, 0.25)
        glVertex3f(-0.25, 0.5, -0.25)
        glVertex3f(-0.25, -0.5, -0.25)
        glVertex3f(-0.25, -0.5, 0.25)

        glColor3f(0, 1, 0)
        glVertex3f(0.25, 0.5, 0.25)
        glVertex3f(0.25, 0.5, -0.25)
        glVertex3f(0.25, -0.5, -0.25)
        glVertex3f(0.25, -0.5, 0.25)

        glColor3f(1, 1, 0)
        glVertex3f(-0.25, 0.5, 0.25)
        glVertex3f(0.25, 0.5, 0.25)
        glVertex3f(0.25, -0.5, 0.25)
        glVertex3f(-0.25, -0.5, 0.25)

        glColor3f(1, 1, 1)
        glVertex3f(-0.25, 0.5, -0.25)
        glVertex3f(0.25, 0.5, -0.25)
        glVertex3f(0.25, -0.5, -0.25)
        glVertex3f(-0.25, -0.5, -0.25)
        glEnd()

        glBegin(GL_TRIANGLES)

        glColor3f(0, 0, 1)
        glVertex3f(-0.25, 0.5, 0.25)
        glVertex3f(0, 1, 0)
        glVertex3f(-0.25, 0.5, -0.25)

        glColor3f(1, 0, 1)
        glVertex3f(0.25, 0.5, 0.25)
        glVertex3f(0, 1, 0)
        glVertex3f(0.25, 0.5, -0.25)

        glColor3f(1, 0, 0)
        glVertex3f(-0.25, 0.5, 0.25)
        glVertex3f(0, 1, 0)
        glVertex3f(0.25, 0.5, 0.25)

        glColor3f(1, 1, 0)
        glVertex3f(-0.25, 0.5, -0.25)
        glVertex3f(0, 1, 0)
        glVertex3f(0.25, 0.5, -0.25)

        glEnd()

        glPopMatrix()
        angle += 1
        sc += dir*step
        if (sc > 2):
            dir = -1
        if (sc < 0):
            dir = 1
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
