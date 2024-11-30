import matplotlib.pyplot as plt
import numpy as np


class GenerateStatistic:
    def __init__(self, completed_requests: list, max_queue_sizes: list):
        self.completed_requests = completed_requests
        self.max_queue_sizes = max_queue_sizes

    def analyze_results(self):
        """
        Анализирует и возвращает результаты функции распределения времени обслуживания.
        """
        pc1_completed = len([req for req in self.completed_requests if req.pk_index == 1])
        pc2_completed = len(self.completed_requests) - pc1_completed

        analysis_result = (
            f"Максимальная очередь для ПК1: {self.max_queue_sizes[0]}\n"
            f"Максимальная очередь для ПК2: {self.max_queue_sizes[1]}\n\n"
            f"Заявки, завершенные ПК1: {pc1_completed}\n"
            f"Заявки, завершенные ПК2: {pc2_completed}\n"
        )

        print(f"Максимальная очередь для ПК1: {self.max_queue_sizes[0]}")
        print(f"Максимальная очередь для ПК2: {self.max_queue_sizes[1]}\n")

        print(f"Заявки, завершенные ПК1: {pc1_completed}")
        print(f"Заявки, завершенные ПК2: {pc2_completed}\n")
        return analysis_result

    def plot_distribution_function(self):
        """
        Строит функцию распределения времени обслуживания заявок.
        """
        service_times = [req.total_time for req in self.completed_requests]
        service_times.sort()

        # Вычисление частот
        counts, bin_edges = np.histogram(service_times, bins=100, density=True)
        cumulative_distribution = np.cumsum(counts * np.diff(bin_edges))

        # Построение графика
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(
            bin_edges[:-1],
            cumulative_distribution,
            marker="o",
            linestyle="-",
            color="green",
            label="Функция распределения",
        )
        ax.set_title("Функция распределения времени обслуживания заявок")
        ax.set_xlabel("Время обслуживания (секунды)")
        ax.set_ylabel("Накопленная вероятность")
        ax.grid(True)
        ax.legend()

        return fig
