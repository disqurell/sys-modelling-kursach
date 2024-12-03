from collections import deque
from CommunicationChannel import CommunicationChannel
from Request import Request
from NormalRandom import rand

import params


class Computer:
    def __init__(self, computer_id: int) -> None:
        self.id = computer_id
        self.queue = deque()
        self.processing_time = params.PROCESSING_TIME
        self.busy_until_time = -1
        self.channel = CommunicationChannel()

    def is_queue_empty(self) -> bool:
        return not (len(self.queue) >= 1)

    def is_busy(self, current_time: int) -> bool:
        return current_time <= self.busy_until_time

    def add_request_to_queue(self, request: Request) -> None:
        self.queue.append(request)

    def update_being_busy(self, current_time: int, time_being_busy: int) -> None:
        self.busy_until_time = current_time + time_being_busy

    def process_request(self, request: Request, current_time: int):
        request.start_time = current_time
        processing_time = self.processing_time

        found_data_chance = self.get_found_data_chance()

        if found_data_chance > float(params.SUCCESS_PROBABILITY) or self.id == 2:
            time_to_return_answer = self.get_time_to_return_answer()

            processing_time += time_to_return_answer

            if self.id == 2:
                processing_time += self.channel.transmit_request()
                processing_time -= self.processing_time

            request.end_time += current_time + processing_time
            request.total_time = request.end_time - request.start_time

        else:
            processing_time += self.channel.transmit_request()

            request.end_time = processing_time
            request.pk_index = 2

        self.update_being_busy(
            current_time=current_time,
            time_being_busy=processing_time,
        )

        return request

    def get_request(self):
        return self.queue.popleft()

    def get_found_data_chance(self) -> float:
        return rand.probability()

    def get_time_to_return_answer(self) -> int:
        return rand.from_range(params.RESPONSE_TIME_MIN, params.RESPONSE_TIME_MAX)
