from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Texture ID
texture_id = 0


def create_cloud_texture():
    """
    Generates a procedural cloud texture (radial gradient with noise).
    Returns raw bytes, width, and height.
    """
    width = 64
    height = 64
    texture_data = []

    center_x = width / 2.0
    center_y = height / 2.0
    max_dist = width / 2.0

    for y in range(height):
        for x in range(width):
            # Calculate distance from center
            dx = x - center_x
            dy = y - center_y
            dist = math.sqrt(dx*dx + dy*dy)

            # Calculate alpha based on distance (1.0 at center, 0.0 at edges)
            alpha = 1.0 - (dist / max_dist)
            if alpha < 0:
                alpha = 0.0

            # Apply a simple curve to make the falloff smoother
            alpha = alpha * alpha

            # Add some random noise to the whiteness
            noise = random.uniform(0.9, 1.0)

            # Color: White with varying alpha
            r = int(255 * noise)
            g = int(255 * noise)
            b = int(255 * noise)
            a = int(255 * alpha)

            texture_data.extend([r, g, b, a])

    return bytes(texture_data), width, height


def init():
    global texture_id
    glClearColor(0.5, 0.7, 1.0, 1.0)  # Sky blue background
    glEnable(GL_DEPTH_TEST)

    # Enable Blending for transparency
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Enable Texturing
    glEnable(GL_TEXTURE_2D)

    # Generate texture data
    texture_content, width, height = create_cloud_texture()

    # Create Texture in OpenGL
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    # Upload texture data
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, texture_content)


def draw_cloud_puff(x, y, scale):
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glScalef(scale, scale, 1.0)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0, 0.0)
    glEnd()

    glPopMatrix()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Move camera back
    glTranslatef(0.0, 0.0, -10.0)

    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Draw a cloud composed of multiple puffs
    # Cloud 1
    glPushMatrix()
    glTranslatef(-2.0, 1.0, 0.0)
    draw_cloud_puff(0.0, 0.0, 1.5)
    draw_cloud_puff(1.0, 0.2, 1.2)
    draw_cloud_puff(-1.0, -0.2, 1.3)
    draw_cloud_puff(0.5, 0.8, 1.0)
    glPopMatrix()

    # Cloud 2
    glPushMatrix()
    glTranslatef(2.0, -1.0, 0.0)
    draw_cloud_puff(0.0, 0.0, 1.4)
    draw_cloud_puff(0.8, 0.1, 1.1)
    draw_cloud_puff(-0.9, -0.1, 1.2)
    glPopMatrix()

    glutSwapBuffers()


def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Cloud with Texture")

    init()

    glutDisplayFunc(draw)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
