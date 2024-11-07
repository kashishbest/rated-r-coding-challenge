import os

import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'logs_project.settings')

# Initialize Django
django.setup()

from logapp.models import Log
from logapp.parser.log_file_processor import LogFileProcessor
from logapp.parser.simple_log_parser import SimpleLogParser


# Initialize the parser and processor
parser = SimpleLogParser()
processor = LogFileProcessor(parser, 'api_requests.log')

# Define a batch size for bulk inserts
batch_size = 1000
logs_batch = []

# Process the file and perform batch inserts
for log in processor.process_file():
    logs_batch.append(log)
    if len(logs_batch) >= batch_size:
        # Bulk insert the current batch of logs
        Log.objects.bulk_create(logs_batch)
        logs_batch = []  # Clear the batch list

# Insert any remaining logs in the final batch
if logs_batch:
    Log.objects.bulk_create(logs_batch)

print("Data loading complete.")
