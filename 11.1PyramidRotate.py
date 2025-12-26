# use premitive method to draw triangle and interpolation
import glfw
from OpenGL.GL import *

# without push and pop the transformation would apply to whole scene(matrix)


def main():
    stat = glfw.init()
    assert (stat != None)
    window = glfw.create_window(800, 600, "aa", None, None)
    assert (window != None)
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    angle = 0
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glPushMatrix()
        glRotatef(angle, 1, 0, 0)
        angle += 1
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0.5, 0)
        glColor3f(1, 0, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glColor3f(1, 0, 0)
        glVertex3f(-0.5, -0.5, 0.5)

        glColor3f(0, 1, 0)
        glVertex3f(0, 0.5, 0)
        glColor3f(0, 1, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glColor3f(0, 1, 0)
        glVertex3f(0.5, -0.5, 0.5)

        glColor3f(0, 0, 1)
        glVertex3f(0, 0.5, 0)
        glColor3f(0, 0, 1)
        glVertex3f(-0.5, -0.5, 0.5)
        glColor3f(0, 0, 1)
        glVertex3f(0.5, -0.5, 0.5)

        glColor3f(1, 1, 0)
        glVertex3f(0, 0.5, 0)
        glColor3f(1, 1, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glColor3f(1, 1, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glColor3f(0, 1, 0)
        glVertex3f(-0.5, -0.5, 0.5)
        glColor3f(0, 0, 1)
        glVertex3f(0.5, -0.5, 0.5)
        glColor3f(0, 0, 1)
        glVertex3f(0.5, -0.5, -0.5)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        # glRotatef(angle, 0, 1, 0)
        glScalef(0.5, 0.5, 0.5)
        glTranslatef(1.5, 0, 0)
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0.5, 0)
        glColor3f(1, 0, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glColor3f(1, 0, 0)
        glVertex3f(-0.5, -0.5, 0.5)

        glColor3f(0, 1, 0)
        glVertex3f(0, 0.5, 0)
        glColor3f(0, 1, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glColor3f(0, 1, 0)
        glVertex3f(0.5, -0.5, 0.5)

        glColor3f(0, 0, 1)
        glVertex3f(0, 0.5, 0)
        glColor3f(0, 0, 1)
        glVertex3f(-0.5, -0.5, 0.5)
        glColor3f(0, 0, 1)
        glVertex3f(0.5, -0.5, 0.5)

        glColor3f(1, 1, 0)
        glVertex3f(0, 0.5, 0)
        glColor3f(1, 1, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glColor3f(1, 1, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glColor3f(0, 1, 0)
        glVertex3f(-0.5, -0.5, 0.5)
        glColor3f(0, 0, 1)
        glVertex3f(0.5, -0.5, -0.5)
        glColor3f(0, 0, 1)
        glVertex3f(0.5, -0.5, 0.5)
        glEnd()

        glPopMatrix()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
