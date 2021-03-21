from Simulator import Simulator
from GoodPlayer import GoodPlayer
from BadPlayer import BadPlayer
from params import n, f
from matplotlib import pyplot as plt


def main():
    sim = Simulator(n, f, GoodPlayer, BadPlayer)
    y = []
    for i in range(1, 100, 2):
        y.append(sim.simulate(i))
    plt.plot(range(1, 100, 2), y, 'o')
    plt.show()


if __name__ == '__main__':
    main()
