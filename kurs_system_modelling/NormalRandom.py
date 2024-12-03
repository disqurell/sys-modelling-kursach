from random import gauss
from RandomDataTracker import tracker


class NormalRandom:
    def __init__(self) -> None:
        self.tracker = tracker

    def from_range(self, a: float, b: float) -> int:
        """
        Генерирует случайное число из диапазона [a, b] по нормальному распределению.

        :param a: Минимальное значение диапазона.
        :param b: Максимальное значение диапазона.
        :param Optional(mean): Среднее значение нормального распределения.
        :param Optional(stddev): Стандартное отклонение нормального распределения.
        :return: Случайное число из диапазона [a, b].
        """

        while True:
            # Генерация случайного числа по нормальному распределению
            value = gauss(a, b)

            if a <= value <= b:
                self.tracker.add_entry("from_range", [round(value)])
                return round(value)

    def probability(self) -> float:
        """
        Генерирует вероятность (число от 0 до 1) по нормальному распределению.

        :param Optional(mean): Среднее значение нормального распределения.
        :param Optional(stddev): Стандартное отклонение нормального распределения.
        :return: Вероятность в диапазоне [0, 1].
        """

        # Генерация случайного числа по нормальному распределению
        value = gauss(0, 1)

        # Приведение значения к диапазону [0, 1]
        # Для этого используется сигмоидная нормализация
        probability = 1 / (1 + abs(value))

        self.tracker.add_entry("probability", [probability])

        return probability


rand = NormalRandom()
