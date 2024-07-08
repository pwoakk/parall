import json
import math


# Функция для расчета характеристик параллелепипеда
def calculate_characteristics(a, b, c):
    diag = math.sqrt(a ** 2 + b ** 2 + c ** 2)
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + c * a)
    alpha = math.degrees(math.acos(a / diag))
    beta = math.degrees(math.acos(b / diag))
    gamma = math.degrees(math.acos(c / diag))
    radius_described_sphere = diag / 2
    volume_described_sphere = (4 / 3) * math.pi * (radius_described_sphere ** 3)
    return diag, volume, surface_area, alpha, beta, gamma, radius_described_sphere, volume_described_sphere


def check_characteristics():
    try:
        with open('parallelepipeds.json', 'r') as file:
            original_data = json.load(file)

        with open('characteristics.json', 'r') as file:
            characteristics = json.load(file)

        for figure_key, figure_data in original_data.items():
            a = float(figure_data['a'])
            b = float(figure_data['b'])
            c = float(figure_data['c'])

            diag, volume, surface_area, alpha, beta, gamma, radius_described_sphere, volume_described_sphere = calculate_characteristics(
                a, b, c)

            char = characteristics[figure_key]

            assert math.isclose(float(char["diag"]), diag), f"Diag mismatch in {figure_key}"
            assert math.isclose(float(char["volume"]), volume), f"Volume mismatch in {figure_key}"
            assert math.isclose(float(char["surface_area"]), surface_area), f"Surface area mismatch in {figure_key}"
            assert math.isclose(float(char["alpha"]), alpha), f"Alpha mismatch in {figure_key}"
            assert math.isclose(float(char["beta"]), beta), f"Beta mismatch in {figure_key}"
            assert math.isclose(float(char["gamma"]), gamma), f"Gamma mismatch in {figure_key}"
            assert math.isclose(float(char["radius_described_sphere"]),
                                radius_described_sphere), f"Radius mismatch in {figure_key}"
            assert math.isclose(float(char["volume_described_sphere"]),
                                volume_described_sphere), f"Volume of described sphere mismatch in {figure_key}"

        print("All characteristics are correct.")

    except (json.JSONDecodeError, AssertionError, KeyError) as e:
        print(f"Error in characteristics: {e}")


def check_statistics():
    try:
        with open('statistics.json', 'r') as file:
            statistics = json.load(file)

        with open('characteristics.json', 'r') as file:
            characteristics = json.load(file)

        count = len(characteristics)

        total_diag = total_volume = total_surface_area = 0
        total_alpha = total_beta = total_gamma = 0
        total_radius_described_sphere = total_volume_described_sphere = 0

        for char in characteristics.values():
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

        assert math.isclose(float(statistics["avg_diag"]), avg_diag), "Avg diag mismatch"
        assert math.isclose(float(statistics["avg_volume"]), avg_volume), "Avg volume mismatch"
        assert math.isclose(float(statistics["avg_surface_area"]), avg_surface_area), "Avg surface area mismatch"
        assert math.isclose(float(statistics["avg_alpha"]), avg_alpha), "Avg alpha mismatch"
        assert math.isclose(float(statistics["avg_beta"]), avg_beta), "Avg beta mismatch"
        assert math.isclose(float(statistics["avg_gamma"]), avg_gamma), "Avg gamma mismatch"
        assert math.isclose(float(statistics["avg_radius_described_sphere"]),
                            avg_radius_described_sphere), "Avg radius mismatch"
        assert math.isclose(float(statistics["avg_volume_described_sphere"]),
                            avg_volume_described_sphere), "Avg volume of described sphere mismatch"

        print("All statistics are correct.")

    except (json.JSONDecodeError, AssertionError, KeyError) as e:
        print(f"Error in statistics: {e}")


check_characteristics()
check_statistics()
