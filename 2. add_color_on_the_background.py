# add some color on the window

import glfw
from OpenGL.GL import *


def main():
    stat = glfw.init()
    assert (stat != None)

    window = glfw.create_window(800, 600, "arik", None, None)

    assert (window != None)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):

        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
