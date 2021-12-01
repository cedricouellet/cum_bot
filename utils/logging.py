"""
Logging functions
"""

from datetime import datetime

LOG_FILE = "logfile.txt"


def write_log(log: str) -> None:
    """
    Write a line into the log file

    :param log: The log to write
    """
    curr_datetime = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')

    line = f"[{curr_datetime}] {log}\n"
    with open(LOG_FILE, 'a+') as f:
        # only keep first 100 chars (for performance reasons)
        # remove line endings (for better readability)
        f.write(line.replace('\n', '')[:100])
