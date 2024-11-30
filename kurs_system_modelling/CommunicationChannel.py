import params


class CommunicationChannel:
    def __init__(self):
        self.transmission_time = params.TRANSMISSION_TIME

    def transmit_request(self) -> int:
        """
        Учитывает время передачи запроса/ответа.
        """
        return self.transmission_time
