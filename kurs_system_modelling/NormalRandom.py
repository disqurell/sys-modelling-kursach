from random import gauss
from RandomDataTracker import tracker


class NormalRandom:
    def __init__(self) -> None:
        self.tracker = tracker

    def from_range(self, a: float, b: float, mean: float | None = None, stddev: float | None = None) -> int:
        """
        Генерирует случайное число из диапазона [a, b] по нормальному распределению.

        :param a: Минимальное значение диапазона.
        :param b: Максимальное значение диапазона.
        :param Optional(mean): Среднее значение нормального распределения.
        :param Optional(stddev): Стандартное отклонение нормального распределения.
        :return: Случайное число из диапазона [a, b].
        """

        if mean is None:
            mean = (a + b) / 2
        if stddev is None:
            stddev = abs(a - b)

        while True:
            # Генерация случайного числа по нормальному распределению
            value = gauss(mean, stddev)

            if a <= value <= b:
                self.tracker.add_entry("from_range", [round(value)])
                return round(value)

    def probability(self, mean: float | None = None, stddev: float | None = None) -> float:
        """
        Генерирует вероятность (число от 0 до 1) по нормальному распределению.

        :param Optional(mean): Среднее значение нормального распределения.
        :param Optional(stddev): Стандартное отклонение нормального распределения.
        :return: Вероятность в диапазоне [0, 1].
        """

        if mean is None:
            mean = 0.5

        if stddev is None:
            stddev = 1

        # Генерация случайного числа по нормальному распределению
        value = gauss(mean, stddev)

        # Приведение значения к диапазону [0, 1]
        # Для этого используется сигмоидная нормализация
        probability = 1 / (1 + abs(value))

        self.tracker.add_entry("probability", [probability])

        return probability


rand = NormalRandom()
