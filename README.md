# Error Log Reader

The Error Log Reader is a Python script designed to read and analyze Apache server error logs, specifically identifying and tallying "PHP Warning" and "PHP Fatal error" occurrences.

## Features

- **Argument Parsing**: Utilizes the `argparse` module to parse command-line arguments for flexible usage.
- **Error Identification**: Parses the error log file to identify PHP warnings and fatal errors.
- **Error Counting**: Groups similar errors and counts their occurrences.
- **Export to CSV**: Optionally exports the error data to a CSV file for further analysis.

## Usage

### Prerequisites

- Python 3 installed on the system.

### Installation

1. Clone the repository to your local system:

    ```bash
    git clone https://github.com/your-username/error-log-reader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd error-log-reader
    ```

### Usage

Run the script `elreader.py` with the required arguments:

```bash
python3 elreader.py -f /path/to/error_log
```

Optional arguments:
- `-l, --limit`: Limit the number of lines to read from the error log file.
- `-e, --export`: Export errors to a CSV file with the specified name.

Example with optional arguments:

```bash
python3 elreader.py -f /path/to/error_log -l 100 -e exported_errors
```

This command will read the last 100 lines from the error log file and export the errors to a CSV file named `exported_errors.csv`.

## Contribution

Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
