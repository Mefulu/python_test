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


def func(x, y):
    # cx = 0.5 #корды центра
    # cy = 0.5
    # r = 0.5
    # d = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    # if d < r: #если пиксель внутри круга, то вернет корды, а если нет, то просто вернет черный цвет
    #     return x, y, 0
    # else:
    #     return 0, 0, 0
    r1 = 1 - (2 * x - 1.1) ** 2 - (2 * y - 1.1) ** 2
    r2 = 1 - (2 * x - 0.9) ** 2 - (2 * y - 0.9) ** 2
    return r1, r2, 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()