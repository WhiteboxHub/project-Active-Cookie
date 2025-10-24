import csv
import random
import string
from datetime import datetime, timedelta

# Function to generate a random cookie (16 alphanumeric characters)
def random_cookie():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Function to generate a random timestamp within the last 2 years
def random_timestamp():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 10, 24)
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    random_date = start_date + timedelta(seconds=random_seconds)
    return random_date.isoformat() + "+00:00"

# Generate 10 CSV files with 20 rows each
file_paths = []
for file_num in range(1, 11):
    file_name = f'./data/cookies_file_{file_num}.csv'
    file_paths.append(file_name)
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['cookie', 'timestamp'])
        for _ in range(20):
            writer.writerow([random_cookie(), random_timestamp()])

