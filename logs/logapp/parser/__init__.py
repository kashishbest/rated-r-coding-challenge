from abc import ABC

from logs.logapp.models.models import Log


class LogParser(ABC):

    def parse_log(self, log_string: str) -> Log:
        pass
