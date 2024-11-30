from typing import List
import matplotlib.pyplot as plt


class RandomDataTracker:
    def __init__(self):
        self.data = []

    def add_entry(self, method_name: str, values: List[float]):
        """
        Добавляет данные о случайных величинах.
        :param method_name: Имя метода, сгенерировавшего данные.
        :param values: Список сгенерированных случайных величин.
        """
        self.data.append({"method": method_name, "values": values})

    def get_all_values(self) -> List[float]:
        """
        Возвращает все сохраненные случайные величины.
        """
        return [value for entry in self.data for value in entry["values"]]

    def generate_histogram(self):
        """
        Генерирует гистограмму распределения случайных величин.
        :return: matplotlib.figure.Figure
        """

        all_values = self.get_all_values()
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(all_values, bins=50, color="blue", edgecolor="black", alpha=0.7)
        ax.set_title("Распределение случайных величин")
        ax.set_xlabel("Значения случайных величин")
        ax.set_ylabel("Частота")
        ax.grid(True)
        return fig


tracker = RandomDataTracker()
