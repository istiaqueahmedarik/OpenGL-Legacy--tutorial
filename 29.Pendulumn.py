from OpenGL.GL import *
from OpenGL.GLUT import *
import math
angle = 90
dir = 1
global_x = 0


# Pendulum configuration
angle = math.pi / 3  # Initial angle (60 degrees)
a_vel = 0.0          # Angular velocity
a_acc = 0.0          # Angular acceleration
length = 150         # Length of the string
pivot_x = 0          # Pivot point X
pivot_y = 90         # Pivot point Y (near the top)
gravity = 0.003      # Gravity constant (affects speed)


def draw():
    global angle, length, pivot_x, pivot_y
    glClear(GL_COLOR_BUFFER_BIT)

    # Calculate the position of the bob using trigonometry
    # x = pivot_x + length * sin(angle)
    # y = pivot_y - length * cos(angle)
    bob_x = pivot_x + length * math.sin(angle)
    bob_y = pivot_y - length * math.cos(angle)

    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(pivot_x, pivot_y)
    glVertex2f(bob_x, bob_y)
    glEnd()

    # Draw the bob
    glColor3f(1, 0, 0)  # Red bob
    glPointSize(15)    # Make it visible as a large point
    glBegin(GL_POINTS)
    glVertex2f(bob_x, bob_y)
    glEnd()

    glutSwapBuffers()


def animate():
    global angle, a_vel, a_acc, gravity

    # Physics calculation for pendulum motion
    # Angular acceleration is proportional to the negative sine of the angle
    a_acc = -gravity * math.sin(angle)

    a_vel += a_acc
    angle += a_vel

    a_vel *= 0.995

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"ar")

    glMatrixMode(GL_PROJECTION)
    glOrtho(-100, 100, -100, 100, 1, -1)
    glMatrixMode(GL_MODELVIEW)

    glutIdleFunc(animate)
    glutDisplayFunc(draw)
    glutMainLoop()


if __name__ == "__main__":
    main()
