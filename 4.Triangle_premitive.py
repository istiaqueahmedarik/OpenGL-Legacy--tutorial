# use premitive method to draw triangle and interpolation
import glfw
from OpenGL.GL import *


def main():
    stat = glfw.init()
    assert (stat != None)
    window = glfw.create_window(800, 600, "aa", None, None)
    assert (window != None)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex2f(0, 1)
        glColor3f(0, 1, 0)
        glVertex2f(-1, 0)
        glColor3f(0, 0, 1)
        glVertex2f(1, 0)

        glColor3f(1, 0, 0)
        glVertex2f(0, -1)
        glColor3f(0, 1, 0)
        glVertex2f(-1, 0)
        glColor3f(0, 0, 1)
        glVertex2f(1, 0)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
