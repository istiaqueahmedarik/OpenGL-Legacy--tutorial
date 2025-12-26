import glfw
from OpenGL.GL import *


def dda(x1, y1, x2, y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)

    max_step = max(dx, dy)

    x_inc = dx/max_step
    y_inc = dx/max_step

    st = 0
    glBegin(GL_LINE_STRIP)
    while (st <= max_step):
        glColor(1, 1, 0)
        glVertex2f(x1, y1)
        x1 += x_inc
        y1 += y_inc
        st += 1
    glEnd()


def main():
    stat = glfw.init()
    assert (stat != None)

    window = glfw.create_window(800, 600, "arik", None, None)
    assert (window != None)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        dda(0, 0, 1, 1)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
