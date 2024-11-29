import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def load_dataset(filename):
    """
    Завантаження координат точок з текстового файлу.
    """
    try:
        points = np.loadtxt(filename, dtype=int)
        return points
    except Exception as e:
        print(f"Помилка завантаження файлу: {e}")
        return None

def compute_convex_hull(points):
    """
    Обчислення опуклої оболонки.
    """
    hull = ConvexHull(points)
    return hull, hull.vertices

def save_convex_hull_dataset(points, hull_vertices, output_filename):
    """
    Збереження координат точок опуклої оболонки.
    """
    hull_points = points[hull_vertices]
    np.savetxt(output_filename, hull_points, fmt='%d')

def visualize_convex_hull(points, hull):
    """
    Візуалізація точок та опуклої оболонки.
    """
    plt.figure(figsize=(9.6, 5.4), dpi=100)
    plt.title('Опукла оболонка')
    
    # Всі точки
    plt.scatter(points[:, 0], points[:, 1], color='red', label='Точки')
    
    # Точки опуклої оболонки
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'b-', linewidth=2)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Збереження зображення
    plt.savefig('convex_hull.png')
    plt.close()

def main(input_filename='DS0.txt', output_hull_filename='convex_hull_dataset.txt'):
    """
    Основна функція для обробки датасету та виведення результатів.
    """
    # Завантаження точок
    points = load_dataset(input_filename)
    
    if points is not None:
        # Обчислення опуклої оболонки
        hull, hull_vertices = compute_convex_hull(points)
        
        # Збереження точок опуклої оболонки
        save_convex_hull_dataset(points, hull_vertices, output_hull_filename)
        
        # Візуалізація
        visualize_convex_hull(points, hull)
        
        print(f"Опукла оболонка збережена у {output_hull_filename}")
        print(f"Зображення збережене як convex_hull.png")

if __name__ == "__main__":
    main()