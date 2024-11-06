from abc import ABC, abstractmethod
from typing import List

from logs.logapp.models.models import Log


class LogParserInterface(ABC):

    @abstractmethod
    def parse(self, log_entry: str) -> Log:
        """Parses a single log entry string and returns a structured object."""
        pass

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Log]:
        """Parses a log file and returns a list of structured log objects."""
        pass