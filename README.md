
# Most Active Cookie Finder

This project provides a command-line tool to find the **most active cookie(s)** from a CSV cookie log for a specific date. It is designed to be **robust, maintainable, and production-ready**.

---

## 🗂️ Project Structure

```
project_root/
├── main.py                  # CLI entry point
├── src/
│   ├── __init__.py
│   └── cookie_analyzer.py   # Core logic for processing cookie logs
├── data/
│   ├── cookies_file_1.csv       # Example CSV log file
│   ├── cookies_file_2.csv
│   ├── ...                  # Additional CSV files
├── tests/
│   └── test_cookie_analyzer.py  # Pytest unit tests
├── run_all.sh               # Shell script to process multiple files/dates
├── app.log                  # Generated log file (after running main.py)
└── README.md
```

---

## ⚡ Features

* Finds the **most active cookie(s)** for a given date.
* Handles **ties** (prints all cookies with max occurrences).
* **Production-grade error handling**:

  * File not found
  * Permission denied
  * Invalid CSV lines
  * Invalid date format
* **Logging** to `app.log` for info, warnings, and errors.
* Supports **multiple CSV files** via a shell script.
* Clean, modular code for **unit testing** and maintainability.

---

## 🛠️ Requirements

* Python 3.10+
* No third-party libraries required for core functionality.
* Optional (for testing):

  ```bash
  pip install pytest pytest-cov
  ```

---

## 🏁 Usage

### Single File

```bash
python main.py -f ./data/cookie_log.csv -d 2018-12-09
```

Output (stdout):

```
AtY0laUfhglK3lC7
```

Logs are written to `app.log`:

```
2025-10-24 14:10:01 [INFO] Processed file ./data/cookie_log.csv for date 2018-12-09: 1 most active cookie(s) found
```

### Multiple Files with Shell Script

```bash
chmod +x run_all.sh
./run_all.sh
```

* Loops through all CSV files in `data/` folder.
* Uses a pre-defined list of dates corresponding to files.
* Prints stdout results for each file/date.
* Logs all processing info into `app.log`.

---

## 📄 CSV Format

The CSV must have a header row:

```
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
```

* **cookie**: string identifier of the cookie
* **timestamp**: ISO 8601 format (`YYYY-MM-DDTHH:MM:SS+00:00`)

---

## 🧪 Testing

The project uses **pytest** for unit tests.

Run all tests:

```bash
pytest -v
```

Check coverage:

```bash
pytest --cov=src tests/
```

---

## 📝 Logging

* All logs are written to `app.log` in the project root.
* Includes info, warning, and error messages.
* Example entries:

```
2025-10-24 14:10:01 [INFO] Processed file ./data/cookie_log.csv for date 2018-12-09: 1 most active cookie(s) found
2025-10-24 14:11:02 [ERROR] File not found: ./data/missing_file.csv
2025-10-24 14:12:05 [WARNING] Execution interrupted by user (Ctrl+C)
```

---

## Production-Ready Features

1. Robust **error handling** (file, CSV, date format, keyboard interrupts)
2. **Logging** for traceability
3. Clean **CLI interface** with argparse
4. **Modular design**: logic separated in `cookie_analyzer.py`
5. Fully **testable** with `pytest`

---


