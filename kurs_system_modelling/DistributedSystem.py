from collections import deque
from typing import List

import params
from GenerateStatistic import GenerateStatistic
from ExponentialRandom import rand

from Request import Request
from Computer import Computer


class DistributedSystem:
    def __init__(self, num_requests: int = params.NUM_REQUESTS):
        self.computer1 = Computer(1)
        self.computer2 = Computer(2)

        self.generated_requests = 0
        self.next_time_to_gen_request = 1
        self.current_time = 0

        self.request_queue = deque()
        self.num_requests = num_requests
        self.completed_requests: List[Request] = []
        self.max_queue_sizes = [0, 0]

    def mainloop(self):
        while (
            self.generated_requests < self.num_requests
            or not self.computer1.is_queue_empty()
            or not self.computer2.is_queue_empty()
        ):
            request = self.create_request()

            if request is not None:
                self.computer1.add_request_to_queue(request=request)

            is_pc1_queue_empty = self.computer1.is_queue_empty()

            if not is_pc1_queue_empty:
                if not self.computer1.is_busy(current_time=self.current_time):
                    self.max_queue_sizes[0] = max(self.max_queue_sizes[0], len(self.computer1.queue))
                    request_to_process = self.computer1.get_request()

                    processed_request: Request = self.computer1.process_request(
                        request=request_to_process, current_time=self.current_time
                    )

                    if processed_request.pk_index == 2:
                        self.computer2.add_request_to_queue(request=processed_request)
                    else:
                        self.completed_requests.append(processed_request)

            if not self.computer2.is_queue_empty():
                if not self.computer2.is_busy(current_time=self.current_time):
                    self.max_queue_sizes[1] = max(self.max_queue_sizes[1], len(self.computer2.queue))
                    request_to_process = self.computer2.get_request()

                    processed_request: Request = self.computer2.process_request(
                        request=request_to_process, current_time=self.current_time
                    )

                    self.completed_requests.append(processed_request)

            self.current_time += 1

    def create_request(self) -> Request:
        if self.current_time >= self.next_time_to_gen_request and self.generated_requests < self.num_requests:
            self.generated_requests += 1

            request = Request(
                id=self.generated_requests,
                arrival_time=self.current_time,
            )

            self.next_time_to_gen_request = self.current_time + rand.from_range(
                params.REQUEST_ARRIVAL_MIN, params.REQUEST_ARRIVAL_MAX
            )

            return request

        return None

    def generate_statistics(self):
        """
        Создает объект GenerateStatistic для генерации статистики.
        """
        return GenerateStatistic(self.completed_requests, self.max_queue_sizes)
