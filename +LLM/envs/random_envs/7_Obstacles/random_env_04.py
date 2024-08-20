import polytope as pc
import numpy as np

title = '2D Random Obstacle Environment 8'

A = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
b_init = np.array([0.0, 2.0, 0.0, 2.0])
Theta = pc.Polytope(A, b_init)

b_goal = np.array([-18.0, 20.0, -18.0, 20.0])
G = pc.Polytope(A, b_goal)

A1 = np.array([[0.768221279597376, -0.6401843996644798], [-0.07124704998790939, -0.9974586998307351], [0.33633639699815626, 0.9417419115948374], [-0.982338566422475, -0.18711210788999494]])
b1 = np.array([3.6362473900942485, -11.962379692970025, 17.967090327641507, -12.999613695657416])
O1 = pc.Polytope(A1, b1)
A2 = np.array([[-0.883787916347062, -0.4678877204190327], [0.06293803653600313, 0.9980174364994797], [0.396911150685467, -0.9178570359601426], [0.768221279597376, -0.6401843996644797]])
b2 = np.array([-10.459889927589932, 16.662395615503026, -8.161485535969918, 0.7938286555839573])
O2 = pc.Polytope(A2, b2)
A3 = np.array([[0.5665288228870651, 0.824041924199368], [-0.39391929857916785, 0.9191450300180579], [0.07669649888473744, -0.9970544855015816], [-0.1699069165076462, -0.9854601157443481]])
b3 = np.array([24.05687392459529, 12.369065975385862, -15.922193168471406, -18.710149645822])
O3 = pc.Polytope(A3, b3)
A4 = np.array([[0.39872611141445075, -0.9170700562532348], [-0.5174193389091942, -0.8557319835805908], [0.8804710999221753, 0.47409982303501735], [-0.18884739365012448, 0.9820064469806475]])
b4 = np.array([-7.906738789348529, -20.63110110181391, 22.777110069525197, 15.379731738866141])
O4 = pc.Polytope(A4, b4)
A5 = np.array([[2.4424906541753475e-16, 1.0], [-0.9486832980505139, 0.3162277660168378], [0.945945945945946, 0.32432432432432423], [-0.07974522228288997, -0.9968152785361252]])
b5 = np.array([18.800000000000004, -9.708192416716928, 21.894594594594594, -16.678713240466443])
O5 = pc.Polytope(A5, b5)
A6 = np.array([[0.9813926548600209, 0.19201160638565637], [0.994505452921406, -0.10468478451804328], [0.970142500145332, 0.2425356250363333], [-0.994309153919809, -0.10653312363426518]])
b6 = np.array([17.716270882516554, 16.037708988164145, 18.093157627710443, -16.583656245733955])
O6 = pc.Polytope(A6, b6)
A7 = np.array([[0.6121731929914164, 0.7907237076139136], [0.9946917938265515, 0.10289915108550515], [-0.9837002310416287, -0.17981617126567398], [-0.6163082616581105, -0.787505001007586]])
b7 = np.array([24.002290608538463, 20.32601231109015, -18.716747944388835, -17.732558261818635])
O7 = pc.Polytope(A7, b7)
O = [O1, O2, O3, O4, O5, O6, O7]

b_workspace = np.array([2.0, 22.0, 2.0, 22.0])
workspace = pc.Polytope(A, b_workspace)

if __name__ == "__main__":
    from envs.plot_env import plot_env
    plot_env(title, workspace, G, Theta, O)
