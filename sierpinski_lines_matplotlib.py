import matplotlib.pyplot as plt
import numpy as np
import sys

def draw_sierpinski(ax, points, depth):
    if depth == 0:
        triangle = plt.Polygon(points, edgecolor='k', fc='k')
        ax.add_patch(triangle)
    else:
        # Calculate midpoints
        p0, p1, p2 = points
        p3 = (p0 + p1) / 2
        p4 = (p1 + p2) / 2
        p5 = (p2 + p0) / 2
        # Recursively draw smaller triangles
        draw_sierpinski(ax, [p0, p3, p5], depth - 1)
        draw_sierpinski(ax, [p3, p1, p4], depth - 1)
        draw_sierpinski(ax, [p5, p4, p2], depth - 1)
if __name__=="__main__":
    # Initial points of the triangle
    if sys.argv ==1:
        depth = 6
    else:
        try:
            depth = int(sys.argv[1])
        except:
            print("Merci de rentrer un int")
    points = np.array([[0, 1], [1, 1], [0.5, np.sqrt(3)/2 + 1]])
    # Create plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    draw_sierpinski(ax, points, depth=depth)

    # Set plot limits and display
    ax.set_xlim(0, 1)
    ax.set_ylim(1, 1 + np.sqrt(3) / 2)
    ax.axis('off')  # Hide the axes
    plt.show()
