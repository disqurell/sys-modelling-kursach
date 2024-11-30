class Request:
    def __init__(self, id: int, arrival_time: int):
        self.id = id
        self.arrival_time = arrival_time
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0  # Полное время обработки
        self.pk_index = 1  # индекс компа (1 или 2)
