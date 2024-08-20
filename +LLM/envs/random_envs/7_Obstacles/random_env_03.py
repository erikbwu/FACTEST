import polytope as pc
import numpy as np

title = '2D Random Obstacle Environment 8'

A = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
b_init = np.array([0.0, 2.0, 0.0, 2.0])
Theta = pc.Polytope(A, b_init)

b_goal = np.array([-18.0, 20.0, -18.0, 20.0])
G = pc.Polytope(A, b_goal)

A1 = np.array([[0.1737853339090473, -0.9847835588179369], [0.09545257331431285, 0.9954339788492635], [-0.0, -1.0], [-0.5299989400031797, -0.8479983040050884]])
b1 = np.array([-3.979684146517199, 9.336625278330008, -7.2, -13.472573054880835])
O1 = pc.Polytope(A1, b1)
A2 = np.array([[-0.9867568184814637, -0.16220660029832287], [0.38745961773206905, -0.921886676672854], [-1.0, -0.0], [0.5686817997598991, 0.8225576032241402]])
b2 = np.array([-7.758882380936441, -5.7250498689031595, -5.2, 17.269647654851514])
O2 = pc.Polytope(A2, b2)
A3 = np.array([[0.9486832980505137, -0.3162277660168385], [0.31977864415817986, -0.9474922789871991], [-0.4625660066950196, 0.886584846165455], [-0.5547001962252291, 0.8320502943378437]])
b3 = np.array([7.5894663844040995, -10.307531630031992, 9.043165430887644, 7.654862707908162])
O3 = pc.Polytope(A3, b3)
A4 = np.array([[0.12797133763019644, 0.9917778666340253], [-0.9333456062030596, 0.3589790793088694], [0.2911616157826961, -0.9566738804288584], [0.1520571842539418, -0.988371697650617]])
b4 = np.array([18.910964418302328, -9.613459743891509, -9.991002873000513, -12.940066380010371])
O4 = pc.Polytope(A4, b4)
A5 = np.array([[0.053975258015000735, 0.9985422732775083], [-0.5665288228870653, -0.8240419241993677], [0.4678877204190326, -0.8837879163470621], [0.0, -1.0]])
b5 = np.array([17.846919062659904, -20.261130811251952, -6.5140368187227615, -15.1])
O5 = pc.Polytope(A5, b5)
A6 = np.array([[0.9954954725939523, -0.09480909262799571], [0.9863939238321437, 0.1643989873053573], [-0.970142500145332, -0.24253562503633305], [-0.9372218510575616, 0.34873371202141873]])
b6 = np.array([18.28393351330892, 20.105996147445197, -18.287186127739506, -12.186063649448432])
O6 = pc.Polytope(A6, b6)
A7 = np.array([[-0.4355609281042812, 0.9001592514155133], [-0.5299989400031797, 0.8479983040050881], [0.15205718425394146, 0.9883716976506173], [0.1766640627937741, -0.9842712069938843]])
b7 = np.array([10.601552990058186, 9.041781916454255, 18.573785056618913, -13.608180379771856])
O7 = pc.Polytope(A7, b7)
O = [O1, O2, O3, O4, O5, O6, O7]

b_workspace = np.array([2.0, 22.0, 2.0, 22.0])
workspace = pc.Polytope(A, b_workspace)

if __name__ == "__main__":
    from envs.plot_env import plot_env
    plot_env(title, workspace, G, Theta, O)
