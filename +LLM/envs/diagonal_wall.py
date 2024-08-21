import polytope as pc
import numpy as np

title = 'Diagonal Wall'
A = np.array([[-1, 0],
              [1, 0],
              [0, -1],
              [0, 1]])

b0 = np.array([0, 1, 0, 1])
Theta = pc.Polytope(A, b0)

b1 = np.array([-4, 5, -4, 5])
G = pc.Polytope(A, b1)

b2 = np.array([-4, 6, 2, 0])

o2_vertices = [[3, -1], [5, 1], [-2, 4], [0, 6]]
O2 = pc.qhull(np.array(o2_vertices))

O1 = pc.Polytope(A, b2)

O = [O1, O2]

workspace = pc.Polytope(A, np.array([5, 7, 5, 7]))

if __name__ == "__main__":
    from plot_env import plot_env

    plot_env(title, workspace, G, Theta, O, show=True)
