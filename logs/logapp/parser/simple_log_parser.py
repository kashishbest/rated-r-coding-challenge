from datetime import datetime
from typing import List

from django.utils.timezone import make_aware

from logapp.models.models import Log
from logapp.parser import LogParserInterface


class SimpleLogParser(LogParserInterface):

    def parse_file(self, file_path: str) -> List[Log]:
        with open(file_path, 'r') as file:
            return [self.parse(line) for line in file]

    def parse(self, log_entry: str) -> Log:
        parts = log_entry.split()
        time_stamp = make_aware(datetime.strptime(f"{parts[0]} {parts[1]}", "%Y-%m-%d %H:%M:%S"))
        customer_id = parts[2]
        request_path = parts[3]
        status_code = int(parts[4])
        duration = float(parts[5])

        return Log(
            time_stamp=time_stamp,
            customer_id=customer_id,
            request_path=request_path,
            status_code=status_code,
            duration=duration
        )


