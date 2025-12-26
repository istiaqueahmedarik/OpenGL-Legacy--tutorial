import glfw
from OpenGL.GL import *
import math
import random


def circle(x, y, z, r):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        theta = math.radians(i)
        xt = x+r*math.cos(theta)
        yt = y+r*math.sin(theta)
        glColor3f(random.randint(0, 1), random.randint(
            0, 1), random.randint(0, 1))
        glVertex3f(xt, yt, z)
    glEnd()


def main():
    stat = glfw.init()
    assert (stat != None)
    window = glfw.create_window(1460, 780, "arik", None, None)
    assert (window != None)

    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    angle = 0
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glPushMatrix()
        glRotatef(angle, 1, 1, 0)

        radius = 0.5
        step = 0.019
        z = -radius
        while z <= radius:
            r = math.sqrt(max(0, radius**2 - z**2))
            # circle(random.randint(-100, 100)/100,
            #        random.randint(-100, 100)/100, z, r)
            circle(0,
                   0, z, r)
            z += step

        glPopMatrix()
        angle += 1
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    main()
