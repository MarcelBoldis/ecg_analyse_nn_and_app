try:
    import sys
    import matplotlib.pyplot as plt
    import numpy as np
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def plot_graph(data, good_signal, bad_signal):
    x = np.arange(len(data))
    left = 0
    right = 2200

    max_data = max(data[left:right]) + 0.1
    min_data = min(data[left:right]) - 0.1

    plt.ylabel('EKG signál')
    plt.xlabel('Časový index')

    plt.plot(x[left:right], data[left:right], color='black')
    plt.scatter(x[good_signal], data[good_signal], color='green')
    plt.scatter(x[bad_signal], data[bad_signal], color='red')

    plt.xlim(left, right)
    plt.ylim(min_data, max_data)
    plt.show()

