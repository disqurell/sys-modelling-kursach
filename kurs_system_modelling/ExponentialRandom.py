from random import expovariate

from RandomDataTracker import tracker


class ExponentialRandom:
    def __init__(self) -> None:
        self.mean = 10
        self.tracker = tracker

    def from_range(self, a: float, b: float, mean: float | None = None) -> int:
        """
        Генерирует случайное число из диапазона [a, b] по экспоненциальному распределению.

        :param a: Минимальное значение диапазона.
        :param b: Максимальное значение диапазона.
        :param Optional(mean): Среднее значение экспоненциального распределения.
        :return: Случайное число из диапазона [a, b].
        """

        if mean is None:
            mean = self.mean

        while True:
            # Генерация случайного числа по экспоненциальному распределению
            value = expovariate(1 / mean)

            if a <= value <= b:
                self.tracker.add_entry("from_range", [int(value)])

                return int(value)

    def probability(self, mean: float | None = None) -> float:
        """
        Генерирует вероятность (число от 0 до 1) по экспоненциальному закону распределения.

        :param Optional(mean): Среднее значение экспоненциального распределения.
        :return: Вероятность в диапазоне [0, 1].
        """

        if mean is None:
            mean = self.mean

        # Генерация случайного числа по экспоненциальному распределению
        value = expovariate(1 / mean)

        # Приведение значения к диапазону [0, 1]
        # Для этого используется сигмоидная нормализация, чтобы вероятность стремилась к 1
        probability = 1 - (1 / (1 + value))

        self.tracker.add_entry("probability", [probability])

        return probability


rand = ExponentialRandom()
