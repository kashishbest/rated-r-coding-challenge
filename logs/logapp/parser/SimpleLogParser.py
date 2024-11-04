from datetime import datetime

from logs.logapp.models.models import Log
from logs.logapp.parser import LogParser


class SimpleLogParser(LogParser):

    @staticmethod
    def parse(log_entry: str) -> Log:
        parts = log_entry.split()
        time_stamp = datetime.strptime(f"{parts[0]} {parts[1]}", "%Y-%m-%d %H:%M:%S")
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
