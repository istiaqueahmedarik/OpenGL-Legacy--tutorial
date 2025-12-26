# just create a window
import glfw


def main():

    state = glfw.init()
    assert (state != None)

    window = glfw.create_window(800, 600, "test", None, None)

    assert (window != None)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
