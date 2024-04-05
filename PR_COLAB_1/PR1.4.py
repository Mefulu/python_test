import math
import tkinter as tk

def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0) for c in func(x / w, y / h)]

    return bytes(f'P6\n{w} {h}\n255\n', 'ascii') + scr

def noise(x, y):
    # Простой алгоритм генерации псевдослучайных значений
    seed = int(x * 100000) ^ int(y * 100000)
    val = (seed * 9301 + 49297) % 233280 / 233280  # Простой линейный конгруэнтный генератор
    return val, val, val

label = tk.Label()
img = tk.PhotoImage(data=pyshader(noise, 256, 256)).zoom(2, 2)  # Создаем изображение шума
label.pack()
label.config(image=img)
tk.mainloop()
