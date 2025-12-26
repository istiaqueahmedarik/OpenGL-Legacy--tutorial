# detect keyboard and mouse event
import glfw
from OpenGL.GL import *


def main():
    stat = glfw.init()

    assert (stat != None)

    window = glfw.create_window(800, 600, "arik", None, None)

    assert (window != None)
    glfw.make_context_current(window)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        if (glfw.get_key(window, glfw.KEY_W) == glfw.PRESS):
            glClearColor(1, 0, 0, 1)
        if (glfw.get_key(window, glfw.KEY_S) == glfw.PRESS):
            glClearColor(0, 1, 0, 1)
        if (glfw.get_key(window, glfw.KEY_A) == glfw.PRESS):
            glClearColor(0, 0, 1, 1)

        if (glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS):
            glClearColor(1, 1, 0, 1)  # Yellow for left click
        if (glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_RIGHT) == glfw.PRESS):
            glClearColor(0, 1, 1, 1)  # Cyan for right click

        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
