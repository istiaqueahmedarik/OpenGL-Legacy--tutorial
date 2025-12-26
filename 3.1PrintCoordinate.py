import glfw
from OpenGL.GL import *


def mouse_button_callback(window, button, action, mods):
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        # Get the current cursor position
        xpos, ypos = glfw.get_cursor_pos(window)

        # Get the current window size
        width, height = glfw.get_window_size(window)

        # Convert to OpenGL Normalized Device Coordinates (-1 to 1)
        # X: 0 -> -1, width -> 1
        ndc_x = (2.0 * xpos) / width - 1.0

        # Y: 0 -> 1, height -> -1 (Flip Y axis)
        ndc_y = 1.0 - (2.0 * ypos) / height

        print(f"Clicked at coordinate: ({ndc_x:.3f}, {ndc_y:.3f})")


def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Click for Coordinates", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the mouse button callback
    glfw.set_mouse_button_callback(window, mouse_button_callback)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here
        glClear(GL_COLOR_BUFFER_BIT)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
