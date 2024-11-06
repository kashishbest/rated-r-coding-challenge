from typing import List

from logs.logapp.models.models import Log
from logs.logapp.parser import LogParserInterface


class LogFileProcessor:
    def __init__(self, parser: LogParserInterface, file_path: str):
        self.parser = parser
        self.file_path = file_path

    def process_file(self) -> List[Log]:
        logs = []

        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    log = self.parser.parse(line)
                    logs.append(log)

        return logs
