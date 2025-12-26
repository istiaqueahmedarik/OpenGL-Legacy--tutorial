import glfw
from OpenGL.GL import *
import math
# import numpy as np
# sinwave = Asin(b(x-c))+D c is upside change d is left right change


def sinWave(startX, endX,  amp, freq=2*math.acos(-1), smoothness=0.1, phase=0, vertical_shift=0):

    glBegin(GL_LINE_STRIP)
    # for i in np.arange(startX, endX, smoothness):
    #     theta = freq*(i-phase)
    #     y = amp*math.sin(theta)+vertical_shift
    #     glColor3f(1, 0, 0)
    #     glVertex2f(i, y)

    st = startX

    while (st < endX):
        theta = freq*(st-phase)
        y = amp*math.sin(theta)+vertical_shift
        glColor3f(1, 0, 0)
        glVertex2f(st, y)
        st += smoothness

    glEnd()


def main():
    stat = glfw.init()

    assert (stat != None)

    window = glfw.create_window(800, 600, "arik", None, None)

    assert (window != None)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        sinWave(-1, 1, 0.5, smoothness=0.00001)
        glfw.swap_buffers(window)
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.poll_events()


if __name__ == "__main__":
    main()
