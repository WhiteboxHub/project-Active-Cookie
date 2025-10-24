#!/usr/bin/env python3
import argparse
import sys
import logging
from src.cookie_analyzer import read_log_file, get_most_active_cookies

# Configure logging
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
    parser.add_argument(
        "-f", "--file",
        required=True,
        help="Path to cookie log CSV file."
    )
    parser.add_argument(
        "-d", "--date",
        required=True,
        help="Date in YYYY-MM-DD format (UTC)."
    )
    args = parser.parse_args()

    # Validate date format early
    try:
        import datetime
        datetime.datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        logging.error("Invalid date format. Use YYYY-MM-DD.")
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

    # Get most active cookies
    try:
        most_active = get_most_active_cookies(cookies, args.date)
    except Exception as e:
        logging.error(f"Error processing cookies: {e}")
        sys.exit(1)

    # Print results
    if not most_active:
        logging.info(f"No cookies found for date: {args.date}")
    else:
        for cookie in most_active:
            print(cookie)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Execution interrupted by user.")
        sys.exit(130)  # Standard code for Ctrl+C termination
