import os

import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logs_project.settings')
django.setup()

from logs.logapp.parser.SimpleLogParser import SimpleLogParser
from logs.logapp.runner import LogFileProcessor

parser = SimpleLogParser()
processor = LogFileProcessor(parser, 'api_requests.log')

# Process the file to get a list of LogFormat objects
logs = processor.process_file()


# Output the logs
for log in logs:
    log.save()
    # print(log.__dict__)
