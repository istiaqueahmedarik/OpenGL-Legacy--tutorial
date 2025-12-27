import glfw
from OpenGL.GL import *


def colored(x1, y1, x, y):
    glBegin(GL_POINTS)
    glVertex2f(x1 + x, y1 + y)
    glVertex2f(x1 - x, y1 + y)
    glVertex2f(x1 + x, y1 - y)
    glVertex2f(x1 - x, y1 - y)

    glVertex2f(x1 + y, y1 + x)
    glVertex2f(x1 - y, y1 + x)
    glVertex2f(x1 + y, y1 - x)
    glVertex2f(x1 - y, y1 - x)
    glEnd()


def circle(xc, yc, r):

    x = 0
    y = r
    d = 3 - 2 * r
    colored(xc, yc, x, y)
    while y >= x:
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        x += 1
        colored(xc, yc, x, y)


def main():
    stat = glfw.init()
    assert (stat != None)
    window = glfw.create_window(800, 600, "arik", None, None)
    assert (window != None)

    glfw.make_context_current(window)

    glViewport(0, 0, 800, 600)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400, 400, -300, 300, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(2.0)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        circle(0, 0, 200)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    main()
