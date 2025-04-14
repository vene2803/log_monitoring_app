#!/usr/bin/env python3 

import logging
from datetime import datetime
from collections import defaultdict

log_file_path = "./logs.log"  # Expecting the log file to be in the same directory as the .py script
output_file = "./job_warnings_errors.txt"  # Output log file (text format)

WARNING_THRESHOLD = 300  # 5 minutes in seconds
ERROR_THRESHOLD = 600    # 10 minutes in seconds

formatter = logging.Formatter('%(levelname)s: %(message)s') #here can be edited as prefence, it can be added to display the time of the job as well;
# cli output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) # Log all levels (INFO, WARNING, ERROR) to this file
console_handler.setFormatter(formatter)

# file output
file_handler = logging.FileHandler(output_file, mode='w') #write output file;
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s', handlers=[console_handler, file_handler])

# The logs.log file is a raw file with strings; we need to convert the string time to datetime object using the specific library;
def parse_time(time_str):
    return datetime.strptime(time_str.strip(), "%H:%M:%S")

def monitor_logs(log_file_path):
    job_events = defaultdict(dict) #using dictionary to store for each PID the Start and End datetime object;
    durations = {}

    with open(log_file_path, 'r') as file:
        for line in file:
            if not line.strip():  # Skip empty lines
                continue
            time_str, job_name, event_type, pid = map(str.strip, line.split(","))
            timestamp = parse_time(time_str)
            pid = int(pid) # Convert the above string PID into an int PID;

            if event_type in ("START", "END"):
                job_events[pid][event_type] = timestamp # Check the existing `START` and `END` of PID; There exist jobs that can have only a START or only an END, we need to skip those;

    for pid, times in job_events.items():
        if "START" in times and "END" in times:
            duration = (times["END"] - times["START"]).total_seconds()
            durations[pid] = duration # calculated job duration in the durations dictionary (between Start-End)

            if duration > ERROR_THRESHOLD:
                logging.error(f"Job {pid} ran for {duration:.0f} seconds. [ERROR]")
            elif duration > WARNING_THRESHOLD:
                logging.warning(f"Job {pid} ran for {duration:.0f} seconds. [WARNING]")
            else:
                logging.info(f"Job {pid} ran for {duration:.0f} seconds.")
        else:
            logging.warning(f"Job {pid} is missing START or END timestamp [WARNING].")

    return durations

# Run the function
monitor_logs(log_file_path)
