import numpy as np
import matplotlib.pyplot as plt

def plot_points(dataset_path, output_path='points_plot.png'):
    # Зчитування даних з файлу
    try:
        data = np.loadtxt(dataset_path, dtype=int)
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return

    # Розподіл координат X та Y
    x_coords = data[:, 0]
    y_coords = data[:, 1]

    # Налаштування графіку
    plt.figure(figsize=(16, 9), dpi=60)  # 960x540 пікселів
    plt.scatter(x_coords, y_coords, color='blue', marker='.')
    plt.title('Графік точок з датасету')
    plt.xlabel('X координата')
    plt.ylabel('Y координата')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Збереження графіку
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"Графік збережено в {output_path}")

# Приклад використання
dataset_path = 'DS0.txt'
plot_points(dataset_path)