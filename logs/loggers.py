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

    line = f"[{curr_datetime}] {log}"
    with open(LOG_FILE, 'w+') as f:
        f.writelines([line])
