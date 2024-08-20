import polytope as pc
import numpy as np

title = '2D Random Obstacle Environment 8'

A = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
b_init = np.array([0.0, 2.0, 0.0, 2.0])
Theta = pc.Polytope(A, b_init)

b_goal = np.array([-18.0, 20.0, -18.0, 20.0])
G = pc.Polytope(A, b_goal)

A1 = np.array([[-0.1414213562373094, -0.9899494936611667], [0.3780319566234552, 0.9257925468329514], [-0.29000739528287073, -0.9570244044334736], [-0.6931087162517845, -0.7208330649018561]])
b1 = np.array([-8.485281374238571, 11.155028695548037, -9.78194944289123, -9.124083140738495])
O1 = pc.Polytope(A1, b1)
A2 = np.array([[-0.3830150227004329, -0.9237421135716325], [0.7189883760491118, 0.6950220968474752], [-0.7071067811865474, -0.7071067811865477], [0.3336927099773762, 0.9426819056860881]])
b2 = np.array([-16.266873317041917, 20.76917755613868, -15.556349186104045, 17.328662429125153])
O2 = pc.Polytope(A2, b2)
A3 = np.array([[0.7808688094430305, -0.6246950475544241], [-0.21871145691738092, -0.9757895770160065], [0.4573480126207612, 0.8892878023181474], [-0.9531242671445428, 0.30257913242683904]])
b3 = np.array([-1.702294004585802, -13.447389808774036, 19.211157352364317, 2.4342491203739214])
O3 = pc.Polytope(A3, b3)
A4 = np.array([[-0.3589790793088693, 0.9333456062030595], [-0.1762991002830991, -0.9843366432473039], [0.20260560403595226, 0.979260419507103], [0.7808688094430313, -0.6246950475544233]])
b4 = np.array([12.269904930777143, -18.933054211235827, 19.882363276061454, 3.6076138996268305])
O4 = pc.Polytope(A4, b4)
A5 = np.array([[0.8282834131279636, 0.5603093677042099], [-0.7071067811865467, 0.7071067811865485], [0.9005516363645787, -0.4347490658311753], [-0.9997232982791523, -0.02352290113598016]])
b5 = np.array([24.56347545461545, 1.9091883092037112, 10.107915780574848, -16.333126403767753])
O5 = pc.Polytope(A5, b5)
A6 = np.array([[-0.984892321570454, 0.17316788071568437], [0.43381561877289987, 0.9010016697591], [0.015149776296267235, -0.9998852355536476], [0.9980525784828888, -0.062378286155180346]])
b6 = np.array([-6.205903925148332, 22.181326292180508, -10.674532378350005, 14.091254842455289])
O6 = pc.Polytope(A6, b6)
A7 = np.array([[0.5854905538443586, -0.8106792283998812], [0.9848923215704541, -0.1731678807156844], [-0.9486832980505132, 0.3162277660168396], [-0.911767746590707, 0.4107061921579761]])
b7 = np.array([8.386026240447658, 17.440170186578346, -13.787530598334124, -13.165597695816084])
O7 = pc.Polytope(A7, b7)
O = [O1, O2, O3, O4, O5, O6, O7]

b_workspace = np.array([2.0, 22.0, 2.0, 22.0])
workspace = pc.Polytope(A, b_workspace)

if __name__ == "__main__":
    from envs.plot_env import plot_env
    plot_env(title, workspace, G, Theta, O)
