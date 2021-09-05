import matplotlib.pyplot as plt

x = [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
y = [1, 3, 2, 3, 9, 12, 26, 18, 35, 77, 53, 108, 238, 163, 327, 715]

plt.yscale("log")
plt.xlabel("# of Stones")
plt.ylabel("Runtime (log scale)")
plt.title("Nim runtime in comparison to number of stones.")
plt.plot(x, y)
plt.show()
