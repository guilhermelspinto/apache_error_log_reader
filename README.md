# Apache Error Log Reader

The Apache Error Log Reader is a Python tool that allows users to analyze Apache server error logs, identifying and tallying different types of recorded errors.

## Features

- **Error Log Reading**: Analyzes Apache server error log files to identify "PHP Warning" and "PHP Fatal error" errors.
- **Error Grouping and Counting**: Groups similar errors and counts how many times each error occurred.
- **Export to CSV**: Optionally, results can be exported to a CSV file for additional analysis.

## How to Use

### Prerequisites

- Python 3 installed on the system.

### Installation

1. Clone the repository to your local system:

    ```bash
    git clone https://github.com/guilhermelspinto/apache-error-log-reader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd apache-error-log-reader
    ```

### Usage

Run the `elreader.py` script passing the path to the Apache error log file as the first argument:

```bash
python3 elreader.py /path/to/error_log
```

Optionally, you can specify the number of lines to be read from the file and the output CSV file name:

```bash
python3 elreader.py /path/to/error_log 100 output.csv
```

### Results

The results will be displayed in the terminal, showing the grouped errors and their corresponding counts. If an output CSV file name is specified, the results will also be exported to that file.

## Contribution

Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

