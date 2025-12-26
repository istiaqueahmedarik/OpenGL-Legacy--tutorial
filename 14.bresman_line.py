import glfw
from OpenGL.GL import *


def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINE_STRIP)
    # kottuk jaite hobe
    dx = abs(x1-x2)
    dy = abs(y1-y2)

    # decision parameter
    p = 2*dy-dx

    dirx = 1 if x2 > x1 else -1
    diry = 1 if y2 > y1 else -1

    glColor3f(1, 0, 0)
    glVertex2f(x1, y1)
    st = 0
    while (st < dx):
        st += 1
        x1 += dirx
        if (p < 0):
            p += 2*dy
        else:
            y1 += diry
            p += 2*(dy-dx)
        glColor3f(1, 0, 0)
        glVertex2f(x1, y1)
    glEnd()


def main():
    stat = glfw.init()
    assert (stat != None)

    window = glfw.create_window(800, 600, "arik", None, None)
    assert (window != None)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        draw_line(0, 0, -0.5, 0.5)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
