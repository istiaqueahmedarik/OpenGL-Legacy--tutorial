import glfw
from OpenGL.GL import *
import random
import time


def main():
    stat = glfw.init()

    assert (stat != None)

    window = glfw.create_window(800, 600, "a", None, None)

    assert (window != None)

    glfw.make_context_current(window)
    move = 0
    dir = 1
    while not glfw.window_should_close(window):

        glBegin(GL_TRIANGLES)
        glColor3f(random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1))
        glVertex2f(0+move, 0.5)
        glColor3f(random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1))
        glVertex2f(-0.5+move, 0)
        glColor3f(random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1))
        glVertex2f(0.5+move, 0)
        glEnd()
        move += dir*0.01
        if (dir == 1 and 0.5+move > 1):
            dir = -1
        if (dir == -1 and -0.5+move < -1):
            dir = 1
        glfw.swap_buffers(window)
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

    glfw.terminate()


if __name__ == "__main__":
    main()
