import polytope as pc
import numpy as np

title = '2D Random Obstacle Environment 10'

A = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
b_init = np.array([0.0, 2.0, 0.0, 2.0])
Theta = pc.Polytope(A, b_init)

b_goal = np.array([-18.0, 20.0, -18.0, 20.0])
G = pc.Polytope(A, b_goal)

A1 = np.array([[0.01030873055283992, 0.9999468636254575], [-0.9892034623538709, 0.1465486610894625], [0.9701425001453315, -0.2425356250363344], [0.1025492707375549, -0.9947279261542805]])
b1 = np.array([17.86503004807132, -3.722335991672343, 11.326413689196722, -14.405096060504306])
O1 = pc.Polytope(A1, b1)
A2 = np.array([[-0.10653312363426422, 0.9943091539198091], [-0.8524856460542565, 0.5227506320144025], [0.9892034623538709, 0.1465486610894625], [0.009173925859236005, -0.999957918656745]])
b2 = np.array([15.575142675329596, -2.4842718496807525, 18.575042793089356, -6.436426382840115])
O2 = pc.Polytope(A2, b2)
A3 = np.array([[-0.6656148469584019, 0.7462954344685109], [0.371390676354104, 0.9284766908852593], [0.1240347345892086, -0.9922778767136676], [0.6431920864232732, -0.7657048647896113]])
b3 = np.array([2.46075791905833, 21.89348037107442, -12.403473458920843, -1.2496303393366492])
O3 = pc.Polytope(A3, b3)
A4 = np.array([[-0.5436466818877441, 0.8393141755459909], [-0.23162052730603971, -0.972806214685367], [0.7880243737245634, -0.6156440419723151], [0.5812381937190964, -0.8137334712067351]])
b4 = np.array([-0.9957318173522897, -4.01629994348673, 6.491350778556091, 2.917815732469863])
O4 = pc.Polytope(A4, b4)
A5 = np.array([[0.8528513040762654, 0.5221538596385297], [-0.9971641204866133, -0.0752576694706875], [0.9922778767136679, 0.12403473458920806], [-0.1465486610894623, -0.989203462353871]])
b5 = np.array([18.400702013661792, -12.093907483939523, 15.26867582793156, -13.808547591154593])
O5 = pc.Polytope(A5, b5)
A6 = np.array([[-0.9805806756909203, 0.1961161351381841], [-0.22903933372554658, -0.9734171683335762], [0.8574929257125442, 0.5144957554275265], [0.7999999999999983, -0.6000000000000024]])
b6 = np.array([-12.159200378567414, -19.657300816995086, 23.666804749666216, 4.259999999999929])
O6 = pc.Polytope(A6, b6)
A7 = np.array([[0.8900433648586652, -0.45587586980565775], [-0.9191450300180579, -0.39391929857916763], [0.9149178015729322, 0.4036402065762936], [-0.13756837127468796, 0.9904922731777516]])
b7 = np.array([4.500146086224421, -14.850757556434623, 18.494794265325773, 17.50695092841676])
O7 = pc.Polytope(A7, b7)
A8 = np.array([[-0.38805700005813276, 0.9216353751380654], [0.999915679412979, 0.012985917914454461], [-0.566528822887066, 0.8240419241993671], [-0.6726727939963123, -0.739940073395944]])
b8 = np.array([6.213762713430852, 17.17907080903156, 2.6575352055429446, -16.090333232391792])
O8 = pc.Polytope(A8, b8)
A9 = np.array([[0.9061831399952656, -0.42288546533112403], [-0.8899332505568759, -0.45609079091039884], [0.8294369271052774, 0.5586003794790644], [0.045407660918649076, 0.9989685402102997]])
b9 = np.array([4.869224072241226, -14.54150931409935, 17.88536851386604, 19.47534576800897])
O9 = pc.Polytope(A9, b9)
O = [O1, O2, O3, O4, O5, O6, O7, O8, O9]

b_workspace = np.array([2.0, 22.0, 2.0, 22.0])
workspace = pc.Polytope(A, b_workspace)

if __name__ == "__main__":
    from envs.plot_env import plot_env
    plot_env(title, workspace, G, Theta, O)
