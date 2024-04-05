import matplotlib.pyplot as plt

fig, ax = plt.subplots()
xdata = [1, 2, 3, 4, 5]
ydata = [5, 4, 3, 2, 1]
y = [2, 3, 2, 4, 1]


def f(x, a, b, c):
    return a*x**2 + b*x + c

beta_opt = [1, 2, 3]
ax.scatter(xdata, ydata)
ax.plot(xdata, y, 'r', lw=2)
ax.plot(xdata, [f(x, *beta_opt) for x in xdata], 'b', lw=2)  # Исправлено
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
plt.show()