import numpy as np
import matplotlib.pyplot as plt

# Метод Эйлера
def euler_method(f, x0, y0, h, num_points):
    x_values = np.zeros(num_points)
    y_values = np.zeros(num_points)
    x_values[0], y_values[0] = x0, y0
    for i in range(1, num_points):
        x_values[i] = x_values[i - 1] + h
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])
    return x_values, y_values

# Метод Рунге-Кутты 4-го порядка
def runge_kutta_method(f, x0, y0, h, num_points):
    x_values = np.zeros(num_points)
    y_values = np.zeros(num_points)
    x_values[0], y_values[0] = x0, y0
    for i in range(1, num_points):
        x = x_values[i - 1]
        y = y_values[i - 1]
        
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        x_values[i] = x + h
        y_values[i] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    return x_values, y_values

def main():
    try:
        equation_str = input("Введите уравнение (например, x + y): ")
        # Используем безопасный словарь для exec
        namespace = {"np": np}
        exec(f"def f(x, y): return {equation_str}", namespace)
        f = namespace["f"]

        x0 = float(input("Начальное x: "))
        y0 = float(input("Начальное y: "))
        h = float(input("Шаг (h): "))
        num_points = int(input("Кол-во точек: "))

        # Расчет обоими методами
        x_e, y_e = euler_method(f, x0, y0, h, num_points)
        x_rk, y_rk = runge_kutta_method(f, x0, y0, h, num_points)

        # Визуализация
        plt.figure(figsize=(10, 6))
        plt.plot(x_e, y_e, 'r--', label='Метод Эйлера', alpha=0.8)
        plt.plot(x_rk, y_rk, 'b-', label='Метод Рунге-Кутты (RK4)', linewidth=2)
        
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'{equation_str}')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
