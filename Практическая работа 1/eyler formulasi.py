import numpy as np
import matplotlib.pyplot as plt
def euler_method(f, x0, y0, h, num_points):
    x_values = np.zeros(num_points)
    y_values = np.zeros(num_points)
    x_values[0] = x0
    y_values[0] = y0
    for i in range(1, num_points):
        x_values[i] = x_values[i - 1] + h
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])
    return x_values, y_values
def main():
    try:
        equation_str = input("Введите дифференциальное уравнение (используйте переменные x и y): ")
        exec(f"def f(x, y): return {equation_str}", globals())
        x0 = float(input("Введите начальное значение x: "))
        y0 = float(input("Введите начальное значение y: "))
        h = float(input("Введите шаг интегрирования: "))
        num_points = int(input("Введите количество точек: "))
        x_values, y_values = euler_method(f, x0, y0, h, num_points)
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label='Численное решение')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Численное решение дифференциального уравнения методом Эйлера')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное числовое значение.")
    except Exception as e:
        print(f"Произошлаошибка: {e}")
if __name__ == "__main__":
    main()
