"""
Logging functions
"""

from datetime import datetime

LOG_FILE = "logfile.txt"

MAX_LOG_LENGTH = 100


def write_log(log: str) -> None:
    """
    Write a line into the log file

    :param log: The log to write
    """
    curr_datetime = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')

    # only keep first 100 chars (for performance reasons)
    # remove line endings (for better readability)
    log = log.replace('\n', '')[:MAX_LOG_LENGTH]

    line = f"[{curr_datetime}] {log}\n"
    with open(LOG_FILE, 'a+') as f:
        f.write(line)
