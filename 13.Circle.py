import glfw
from OpenGL.GL import *
import math


def circle(x, y, r):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        theta = math.radians(i)
        xt = x+r*math.cos(theta)
        yt = y+r*math.sin(theta)
        glColor3f(1, 0, 0)
        glVertex2f(xt, yt)
    glEnd()


def main():
    stat = glfw.init()
    assert (stat != None)
    window = glfw.create_window(800, 600, "arik", None, None)
    assert (window != None)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        circle(0, 0, 0.5)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    main()
