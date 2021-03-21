from Simulator import Simulator
from GoodPlayer import GoodPlayer
from BadPlayer import BadPlayer
from params import n, f
from matplotlib import pyplot as plt


def main(i):
    sim = Simulator(n, f, GoodPlayer, BadPlayer)
    res_lst = sim.simulate(i)
    plt.xlabel("Number of turns")
    plt.ylabel("Percentage of good policies")
    plt.plot(range(1, i+1), res_lst, 'o')
    plt.show()


if __name__ == '__main__':
    main(6000)
