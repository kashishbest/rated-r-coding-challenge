from typing import Iterator

from logapp.models.models import Log
from logapp.parser import LogParserInterface


class LogFileProcessor:
    def __init__(self, parser: LogParserInterface, file_path: str):
        self.parser = parser
        self.file_path = file_path

    def process_file(self) -> Iterator[Log]:
        logs = []

        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    log = self.parser.parse(line)
                    yield log
