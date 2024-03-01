import sys
import re
import csv
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Error log reader")
    parser.add_argument("-f", "--file", required=True, help="Path to error log file")
    parser.add_argument("-l", "--limit", type=int, default=None, help="Limit the number of lines to read")
    parser.add_argument("-e", "--export", metavar="FILENAME_EXPORTED", help="Export errors to a CSV file with the specified name")
    return parser.parse_args()

def main():
    args = parse_args()

    file_path = args.file
    num_lines = args.limit
    export_csv_file = args.export

    error_counts = {}

    with open(file_path, 'r') as f:
        if num_lines is None:
            lines = f.readlines()
        else:
            lines = f.readlines()[-num_lines:]

        for line in lines:
            match = re.search(r'PHP (Warning|Fatal error): (.+)', line)
            if match:
                error_type = match.group(1)
                error_message = match.group(2).strip()

                error = f"PHP {error_type}: {error_message}"

                if error in error_counts:
                    error_counts[error] += 1
                else:
                    error_counts[error] = 1

    for error, count in error_counts.items():
        print("-----------------------------------------------------------")
        print(f"Error: {error} - Count: {count}")

    if export_csv_file:
        output_csv_file = export_csv_file + ".csv"
        with open(output_csv_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Error', 'Count'])
            for error, count in error_counts.items():
                writer.writerow([error, count])

        print(f"Errors exported to {output_csv_file}")

if __name__ == "__main__":
    main()
