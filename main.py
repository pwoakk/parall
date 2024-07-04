import json
import os
import math


# Функция для расчета углов между диагональю и сторонами
def calculate_angles(diag, a, b, c):
    alpha = math.degrees(math.acos(a / diag))
    beta = math.degrees(math.acos(b / diag))
    gamma = math.degrees(math.acos(c / diag))
    return alpha, beta, gamma


# Функция для расчета характеристик параллелепипеда
def calculate_characteristics(figure):
    a = float(figure['a'])
    b = float(figure['b'])
    c = float(figure['c'])

    diag = math.sqrt(a ** 2 + b ** 2 + c ** 2)
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + c * a)
    alpha, beta, gamma = calculate_angles(diag, a, b, c)
    radius_described_sphere = diag / 2
    volume_described_sphere = (4 / 3) * math.pi * (radius_described_sphere ** 3)

    return {
        "diag": str(diag),
        "volume": str(volume),
        "surface_area": str(surface_area),
        "alpha": str(alpha),
        "beta": str(beta),
        "gamma": str(gamma),
        "radius_described_sphere": str(radius_described_sphere),
        "volume_described_sphere": str(volume_described_sphere)
    }


# Путь к исходному файлу
input_file_path = 'parallelepipeds.json'

# Проверка существования файла
if not os.path.exists(input_file_path):
    print(f"Файл {input_file_path} не найден.")
else:
    try:
        # Чтение исходного файла
        with open(input_file_path, 'r') as file:
            data = json.load(file)

        figures = list(data.values())
        count = len(figures)

        characteristics = {}
        total_diag = total_volume = total_surface_area = 0
        total_alpha = total_beta = total_gamma = 0
        total_radius_described_sphere = total_volume_described_sphere = 0

        for i, figure in enumerate(figures, start=1):
            char = calculate_characteristics(figure)
            characteristics[f"figure_{i}"] = char

            total_diag += float(char["diag"])
            total_volume += float(char["volume"])
            total_surface_area += float(char["surface_area"])
            total_alpha += float(char["alpha"])
            total_beta += float(char["beta"])
            total_gamma += float(char["gamma"])
            total_radius_described_sphere += float(char["radius_described_sphere"])
            total_volume_described_sphere += float(char["volume_described_sphere"])

        avg_diag = total_diag / count
        avg_volume = total_volume / count
        avg_surface_area = total_surface_area / count
        avg_alpha = total_alpha / count
        avg_beta = total_beta / count
        avg_gamma = total_gamma / count
        avg_radius_described_sphere = total_radius_described_sphere / count
        avg_volume_described_sphere = total_volume_described_sphere / count

        statistics = {
            "avg_diag": str(avg_diag),
            "avg_volume": str(avg_volume),
            "avg_surface_area": str(avg_surface_area),
            "avg_alpha": str(avg_alpha),
            "avg_beta": str(avg_beta),
            "avg_gamma": str(avg_gamma),
            "avg_radius_described_sphere": str(avg_radius_described_sphere),
            "avg_volume_described_sphere": str(avg_volume_described_sphere)
        }

        # Сохранение нового JSON файла characteristics.json
        output_file_path1 = 'characteristics.json'
        with open(output_file_path1, 'w') as file1:
            json.dump(characteristics, file1, indent=4)

        # Сохранение нового JSON файла statistics.json
        output_file_path2 = 'statistics.json'
        with open(output_file_path2, 'w') as file2:
            json.dump(statistics, file2, indent=4)

        # Вывод количества фигур
        print(f"Total number of figures {count}.")

        # Красивый вывод усредненных значений
        print(f"Average Diagonal: {avg_diag:.2f}")
        print(f"Average Volume: {avg_volume:.2f}")
        print(f"Average Surface Area: {avg_surface_area:.2f}")
        print(f"Average Alpha: {avg_alpha:.2f}")
        print(f"Average Beta: {avg_beta:.2f}")
        print(f"Average Gamma: {avg_gamma:.2f}")
        print(f"Average Radius of Described Sphere: {avg_radius_described_sphere:.2f}")
        print(f"Average Volume of Described Sphere: {avg_volume_described_sphere:.2f}")

    except json.JSONDecodeError:
        print("Ошибка при чтении JSON файла. Проверьте правильность формата файла.")
