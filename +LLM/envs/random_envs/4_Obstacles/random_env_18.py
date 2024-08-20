import polytope as pc
import numpy as np

title = '2D Random Obstacle Environment 5'

A = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
b_init = np.array([0.0, 2.0, 0.0, 2.0])
Theta = pc.Polytope(A, b_init)

b_goal = np.array([-18.0, 20.0, -18.0, 20.0])
G = pc.Polytope(A, b_goal)

A1 = np.array([[0.8919700836007997, -0.45209442593465193], [-0.5812381937190965, -0.813733471206735], [-0.14778453506138003, 0.9890195807953915], [-0.919145030018058, -0.3939192985791676]])
b1 = np.array([1.629983687018448, -12.810489789568885, 16.092599064068466, -8.561179422453911])
O1 = pc.Polytope(A1, b1)
A2 = np.array([[0.2747211278973779, -0.9615239476408233], [-0.7739572992033213, -0.6332377902572626], [0.9225798771450628, 0.38580613044248113], [-0.8221921916437784, 0.5692099788303089]])
b2 = np.array([-7.58230312996764, -22.085926929083865, 22.975593776828962, -3.2191986580513947])
O2 = pc.Polytope(A2, b2)
A3 = np.array([[-0.9899494936611666, 0.1414213562373093], [0.9615239476408232, -0.274721127897378], [0.9805806756909201, 0.19611613513818454], [0.9689177106244632, -0.24738324526582028]])
b3 = np.array([-14.014856403117376, 12.51354737572557, 20.337243213829694, 12.948451362621817])
O3 = pc.Polytope(A3, b3)
A4 = np.array([[-0.10151368801339453, -0.994834142531266], [0.37570510873921825, -0.926739268223405], [-0.316227766016837, 0.9486832980505141], [-0.099503719020999, 0.9950371902099892]])
b4 = np.array([-17.649169798008767, -13.948678337124711, 16.665203269087364, 17.711661985737802])
O4 = pc.Polytope(A4, b4)
O = [O1, O2, O3, O4]

b_workspace = np.array([2.0, 22.0, 2.0, 22.0])
workspace = pc.Polytope(A, b_workspace)

if __name__ == "__main__":
    from envs.plot_env import plot_env
    plot_env(title, workspace, G, Theta, O)
