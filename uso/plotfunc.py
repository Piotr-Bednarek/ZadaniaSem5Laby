import matplotlib.pyplot as plt

def plot_sets(name,*data_sets):
    plt.figure(figsize=(10, 6))
    plt.title(name)
    for t, x, title in data_sets:
        plt.plot(t, x, label=title)
    plt.xlabel("Time[s]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.xlim(left=0)
    plt.show()