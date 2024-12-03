from typing import List


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


tracker = RandomDataTracker()
