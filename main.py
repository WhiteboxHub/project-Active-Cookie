#!/usr/bin/env python3
import argparse
import sys
import logging
from src.cookie_analyzer import read_log_file, get_most_active_cookies
from datetime import datetime

# Configure logging to file
logging.basicConfig(
    filename="app.log",        # log file
    filemode="a",              # append to existing log
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    parser = argparse.ArgumentParser(
        description="Find most active cookie(s) for a given date."
    )
    parser.add_argument("-f", "--file", required=True, help="Path to cookie log CSV file.")
    parser.add_argument("-d", "--date", required=True, help="Date in YYYY-MM-DD format (UTC).")
    args = parser.parse_args()

    # Validate date format
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        logging.error(f"Invalid date format: {args.date}. Use YYYY-MM-DD.")
        sys.exit(1)

    # Read file with error handling
    try:
        cookies = read_log_file(args.file)
    except FileNotFoundError:
        logging.error(f"File not found: {args.file}")
        sys.exit(1)
    except PermissionError:
        logging.error(f"Permission denied when accessing file: {args.file}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error reading file {args.file}: {e}")
        sys.exit(1)

    # Process cookies
    try:
        most_active = get_most_active_cookies(cookies, args.date)
    except Exception as e:
        logging.error(f"Error processing cookies: {e}")
        sys.exit(1)

    # Output results
    if not most_active:
        logging.info(f"No cookies found for date: {args.date}")
    else:
        for cookie in most_active:
            print(cookie)  # keep stdout clean for results
        logging.info(f"Processed file {args.file} for date {args.date}: {len(most_active)} most active cookie(s) found")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Execution interrupted by user (Ctrl+C).")
        sys.exit(130)
