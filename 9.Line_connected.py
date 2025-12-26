import glfw
from OpenGL.GL import *


def main():
    stat = glfw.init()

    assert (stat != None)

    window = glfw.create_window(800, 600, "a", None, None)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):

        glBegin(GL_LINE_STRIP)
        glColor3f(1, 0, 0)
        glVertex2f(-0.5, 0.5)
        glColor3f(0, 1, 0)
        glVertex2f(0.5, 0.5)
        glColor3f(0, 0, 1)
        glVertex2f(0.5, -0.5)
        glColor3f(1, 1, 1)
        glVertex2f(-0.5, -0.5)

        glColor3f(1, 1, 1)
        glVertex2f(-0.7, -0.6)

        glEnd()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
