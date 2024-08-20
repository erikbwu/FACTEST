import polytope as pc
import numpy as np

title = '2D Random Obstacle Environment 7'

A = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
b_init = np.array([0.0, 2.0, 0.0, 2.0])
Theta = pc.Polytope(A, b_init)

b_goal = np.array([-18.0, 20.0, -18.0, 20.0])
G = pc.Polytope(A, b_goal)

A1 = np.array([[0.6846754616640485, -0.7288480720939874], [-0.042215852683817605, 0.9991085135170145], [0.1543768802736099, -0.9880120337511015], [-0.8253072612498317, 0.5646839155919904]])
b1 = np.array([-3.1296294489611567, 18.990097732270577, -14.378662628683998, 3.279510432861178])
O1 = pc.Polytope(A1, b1)
A2 = np.array([[-0.9544799780350299, 0.29827499313594674], [1.0, -0.0], [0.7399400733959436, -0.6726727939963126], [1.0, 0.0]])
b2 = np.array([-10.242763264288413, 16.7, 0.9215617277749429, 16.7])
O2 = pc.Polytope(A2, b2)
A3 = np.array([[-0.8682431421244594, 0.4961389383568338], [-0.2459381198822544, -0.9692855313006493], [0.5199469468957456, 0.8541985556144384], [0.9557790087219501, 0.2940858488375233]])
b3 = np.array([-3.063657944353451, -15.184508860494951, 22.328007462408717, 20.115472060486585])
O3 = pc.Polytope(A3, b3)
A4 = np.array([[0.9312427797057534, 0.36439934858051237], [0.9962405881956831, 0.08662961636484168], [-0.9928768384869221, -0.11914522061843025], [-0.9620639325477691, -0.2728241002747406]])
b4 = np.array([21.353801826818017, 18.326495341982323, -17.5143474309093, -19.646207052415786])
O4 = pc.Polytope(A4, b4)
A5 = np.array([[0.4355609281042807, 0.9001592514155137], [-0.8443294201829337, 0.5358244397314768], [0.7071067811865479, 0.7071067811865471], [0.09305244937160387, -0.9956612082761612]])
b5 = np.array([16.79232564818037, -3.3578331556505936, 19.86970055134199, -6.74816362842871])
O5 = pc.Polytope(A5, b5)
A6 = np.array([[0.9158691540042249, 0.4014768894265094], [-0.7127408280944526, 0.7014274816167628], [-0.10093121512748268, -0.9948934062566149], [-0.11914522061843058, -0.9928768384869222]])
b6 = np.array([20.107719083870837, -2.5692609850833374, -7.539561770022955, -7.756353862259835])
O6 = pc.Polytope(A6, b6)
O = [O1, O2, O3, O4, O5, O6]

b_workspace = np.array([2.0, 22.0, 2.0, 22.0])
workspace = pc.Polytope(A, b_workspace)

if __name__ == "__main__":
    from envs.plot_env import plot_env
    plot_env(title, workspace, G, Theta, O)
