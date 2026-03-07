import numpy as np
import matplotlib.pyplot as plt

def calc_euler(f, x_start, y_start, h, n):
    x_list = [x_start]
    y_list = [y_start]

    curr_x = x_start
    curr_y = y_start

    for _ in range(n):
        curr_y += h * f(curr_x, curr_y)
        curr_x += h
        x_list.append(curr_x)
        y_list.append(curr_y)

    return x_list, y_list

def d1(x, y): return (y - x) / (y + x)
def d2(x, y): return x + y
def d3(x, y): return 1 + x + y**2
def d4(x, y): return x**2 + y**3
def d5(x, y): return y**2 + (y / x)
def d6(x, y): return ((x + y) * (1 + x * y)) / (x + 2 * y)

def show_res(num, func, x0, y0, steps, limit_one=False):
    print(f"\n--- Задача {num} ---")
    plt.figure()

    for h in steps:
        n_steps = int(1/h) if limit_one else 10

        xs, ys = calc_euler(func, x0, y0, h, n_steps)

        print(f"Шаг {h}:")
        print(f"X: {[round(i, 2) for i in xs]}")
        print(f"Y: {[round(i, 4) for i in ys]}")

        plt.plot(xs, ys, marker='.', label=f'h={h}')

    plt.title(f"График №{num}")
    plt.legend()
    plt.show()

show_res(1, d1, 0, 1, [0.1, 0.05])
show_res(2, d2, 0, 1, [0.1, 0.05])
show_res(3, d3, 0, 1, [0.1, 0.05])
show_res(4, d4, 0, 0, [0.1, 0.05])
show_res(5, d5, 2, 4, [0.1, 0.05])
show_res(6, d6, 0, 1, [0.2, 0.1], limit_one=True)

