import numpy as np
import matplotlib.pyplot as plt
import Helper


B = np.zeros(3)
E = np.zeros(3)
r1 = np.zeros(3)
v1 = np.zeros(3)
v2 = np.zeros(3)
r2 = np.zeros(3)
v1[0] = Helper.v0
v2[0] = Helper.v0

t = 0.0
maxt = 10
B[0] = B[1] = 0
B[2] = Helper.B0
E[0] = E[1] = E[2] = 0.0


# сам пушер для эйлера
def pusher1(dt):
    k = 0
    vec = np.zeros(3)
    vec[0] = v1[1] * B[2] - v1[2] * B[1]
    vec[1] = v1[2] * B[0] - v1[0] * B[2]
    vec[2] = v1[0] * B[1] - v1[1] * B[2]
    while k < 3:
        r1[k] = r1[k] + v1[k] * dt
        v1[k] = v1[k] + Helper.qm * (E[k] + (vec[k]) / Helper.cs) * dt
        k += 1


N = int(maxt / Helper.dt)

plot_pusher1_x = np.zeros(N)
plot_pusher1_y = np.zeros(N)

t = 0
i = 0
while (i < N):
    plot_pusher1_x[i] = plot_pusher1_x[i] + r1[0]
    plot_pusher1_y[i] = plot_pusher1_y[i] + r1[1]
    # print(t, i, "x=", plot_pusher1_x[i], "y=", plot_pusher1_y[i], "r_x=", r1[0], "r_y=", r1[1])
    pusher1(Helper.dt)
    t += Helper.dt
    i += 1

plt.plot(plot_pusher1_x, plot_pusher1_y)
plt.show()

