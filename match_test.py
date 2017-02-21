from elo_file import new_rating
import numpy  as np
import random
import json
import os

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def match_sim():

    while True:
        cont_1 = random.choice(ag_num)
        cont_2 = random.choice(ag_num)

        if cont_1 != cont_2:
            fname1 = base + str(int(cont_1)) + ".json"
            fname2 = base + str(int(cont_2)) + ".json"
            f1 = open(fname1, "r")
            f2 = open(fname2, "r")

            data1 = json.load(f1)
            data2 = json.load(f2)

            rating_1 = data1["info"]["rating"]
            rating_2 = data2["info"]["rating"]

            delta =  rating_1 - rating_2 
            E =  1 / (1 + 10**(-delta/400.)) #prob of 1 winning

            rand_num = random.random()

            result1 = E > rand_num
            result2 = not result1
            new_1, new_2 = new_rating(rating_1, rating_2, result1, result2)

            data1["info"]["rating"] = new_1
            data2["info"]["rating"] = new_2

            data1["matches"].append([base + str(int(cont_2)), result1])
            data2["matches"].append([base + str(int(cont_1)), result2])

            for file, data in zip([fname1, fname2], [data1, data2]):
                os.remove(file)
                with open(file, "w") as f:
                    json.dump(data, f, indent = 4)



            yield delta, E



base = "actor_"
ag_num = np.linspace(0, 299, 300, endpoint = True)
i = 1


def init():
    ax.set_ylim(0, 1.1)
    ax.set_xlim(-300, 300)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], "o",lw=2)
ax.grid()
plt.title(r"Win chance as a function of ELO $\Delta$")
plt.xlabel(r"ELO $ \Delta $")
plt.ylabel("Win, %")
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if abs(t) >= xmax:
        ax.set_xlim(xmin-50, xmax+50)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, match_sim, blit=True, save_count = 200, interval=10, repeat=False, init_func=init)
ani.save('prob_plot.gif', dpi=80, writer='imagemagick')