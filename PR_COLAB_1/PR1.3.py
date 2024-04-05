import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def func(x, y):
    t = 0.6 * x + 0.2 < y or 0.6 * x + 0.2 < 1 - y
    b = ((x - 0.5) ** 2 + (y - 0.5) ** 2) < 0.1
    e = ((x - 0.6) ** 2 + (y - 0.3) ** 2) > 0.003
    a = int(b and e and t)
    return a, a, 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()