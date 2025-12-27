# OpenGL Legacy Tutorial Syllabus

Welcome to the OpenGL Legacy Tutorial! This syllabus is designed to guide you from the absolute basics of setting up an OpenGL window to creating complex animations and mini-games. Follow the modules in order to build a strong foundation in computer graphics concepts.

## Module 1: The Basics - Setup and Interaction
**Goal:** Learn how to initialize OpenGL, manage windows, and handle user input.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 1 | [`1. create_window.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/1.%20create_window.py) | How to initialize GLUT, set display modes, and create a window. |
| 2 | [`2. add_color_on_the_background.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/2.%20add_color_on_the_background.py) | `glClearColor` and clearing buffers to change background colors. |
| 3 | [`3. Detect_keyboard_press.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/3.%20Detect_keyboard_press.py) | Registering callback functions to detect and respond to keyboard input. |
| 4 | [`3.1PrintCoordinate.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/3.1PrintCoordinate.py) | Understanding the coordinate system and mapping mouse clicks to world coordinates. |
| 5 | [`30. glut_testing.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/30.%20glut_testing.py) | General testing of GLUT functionality. |
| 6 | [`30.1.GlutMouseKeyboard.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/30.1.GlutMouseKeyboard.py) | Advanced input handling combining mouse and keyboard interactions. |
| 7 | [`30.2GLUT_PREDEFINED.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/30.2GLUT_PREDEFINED.py) | Using GLUT's built-in shapes (Teapot, Sphere, Cube, etc.) for quick testing. |

## Module 2: 2D Primitives - Drawing Shapes
**Goal:** Master the fundamental building blocks of graphics: points, lines, and polygons.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 8 | [`7.points.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/7.points.py) | `GL_POINTS`: Drawing individual pixels on the screen. |
| 9 | [`8.Line.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/8.Line.py) | `GL_LINES`: Drawing unconnected line segments. |
| 10 | [`9.Line_connected.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/9.Line_connected.py) | `GL_LINE_STRIP`: Drawing connected lines. |
| 11 | [`10.Line_connected_loop.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/10.Line_connected_loop.py) | `GL_LINE_LOOP`: Closing a shape automatically. |
| 12 | [`4.Triangle_premitive.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/4.Triangle_premitive.py) | `GL_TRIANGLES`: The most important primitive in graphics. |
| 13 | [`5.Square.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/5.Square.py) | `GL_QUADS`: Drawing four-sided shapes. |
| 14 | [`6.Polygon.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/6.Polygon.py) | `GL_POLYGON`: Drawing arbitrary convex polygons. |
| 15 | [`13.Circle.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/13.Circle.py) | Using trigonometry (sin/cos) to approximate circles with points/lines. |

## Module 3: Algorithms - How Graphics Work
**Goal:** Implement fundamental rasterization algorithms from scratch to understand how OpenGL works under the hood.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 16 | [`16.dda.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/16.dda.py) | Digital Differential Analyzer (DDA) algorithm for line drawing. |
| 17 | [`14.bresman_line.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/14.bresman_line.py) | Bresenham's Line Algorithm (integer math optimization). |
| 18 | [`15.breseman_circle.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/15.breseman_circle.py) | Bresenham's Circle Algorithm (midpoint circle algorithm). |

## Module 4: Transformations - Moving the World
**Goal:** Learn how to manipulate objects in space using matrix transformations.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 19 | [`17.Translation.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/17.Translation.py) | `glTranslate`: Moving objects along X, Y, and Z axes. |
| 20 | [`18.Rotation.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/18.Rotation.py) | `glRotate`: Rotating objects around an axis. |
| 21 | [`19.Scaling.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/19.Scaling.py) | `glScale`: Resizing objects (making them bigger or smaller). |

## Module 5: 3D Basics and Projection
**Goal:** Transition from 2D to 3D rendering and understand perspective.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 22 | [`4.1Pyramid.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/4.1Pyramid.py) | Constructing a 3D object using triangles. |
| 23 | [`5.1Cube.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/5.1Cube.py) | Constructing a 3D cube using quads. |
| 24 | [`6.13dPolygon.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/6.13dPolygon.py) | Working with complex 3D polygons. |
| 25 | [`20.Perspective.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/20.Perspective.py) | Orthographic vs. Perspective projection (`gluPerspective`). |
| 26 | [`20.1Control3dWithMouse.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/20.1Control3dWithMouse.py) | Implementing a camera system controlled by the mouse. |

## Module 6: Animation and Physics
**Goal:** Bring static scenes to life with movement and math-based animations.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 27 | [`11.Triangle_moving.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/11.Triangle_moving.py) | Basic animation loop using `glutIdleFunc` or `glutTimerFunc`. |
| 28 | [`11.1PyramidRotate.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/11.1PyramidRotate.py) | Animating 3D objects (rotating pyramid). |
| 29 | [`12.SineWave.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/12.SineWave.py) | Plotting mathematical functions. |
| 30 | [`12.1.SineWaveAnimation.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/12.1.SineWaveAnimation.py) | Animating waves using phase shifts. |
| 31 | [`13.1BallNormal.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/13.1BallNormal.py) | Simple physics simulation (bouncing ball). |
| 32 | [`29.Pendulumn.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/29.Pendulumn.py) | Simulating harmonic motion (pendulum physics). |

## Module 7: Advanced Effects and Scenes
**Goal:** Create complex scenes and visual effects.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 33 | [`21.Snoflake.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/21.Snoflake.py) | Procedural generation and fractal-like patterns (Koch snowflake). |
| 34 | [`24.Snowflake_animation.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/24.Snowflake_animation.py) | Animating complex procedural shapes. |
| 35 | [`22.Rainbow.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/22.Rainbow.py) | Using color gradients and arcs. |
| 36 | [`23.Rainbow_animation.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/23.Rainbow_animation.py) | Animating color transitions. |
| 37 | [`27.Mirror.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/27.Mirror.py) | Creating reflection effects using scaling or stencil buffers. |
| 38 | [`32.Cloud.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/32.Cloud.py) | Drawing organic shapes using overlapping circles/ellipses. |

## Module 8: Projects
**Goal:** Combine everything you've learned into complete applications.

| Order | File | What You Will Learn |
|-------|------|---------------------|
| 39 | [`25.House_rainbow_snowflake.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/25.House_rainbow_snowflake.py) | Scene composition: Combining multiple objects into one coherent scene. |
| 40 | [`26.Fighting_game.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/26.Fighting_game.py) | Game logic: Collision detection, state management, and user interaction. |
| 41 | [`31. ModelOpengl.py`](https://github.com/istiaqueahmedarik/OpenGL-Legacy--tutorial/blob/master/31.%20ModelOpengl.py) | Advanced structure or model loading concepts. |

---

### How to Run
To run any of these files, ensure you have Python and PyOpenGL installed:
```bash
pip install PyOpenGL PyOpenGL_accelerate
```
Then run a file using python:
```bash
python <filename>.py
```
