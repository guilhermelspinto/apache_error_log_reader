import sys
import re
import csv

if len(sys.argv) < 2:
    print("How to use: python3 elreader.py /path/to/error_log [number_of_lines] [output_csv_file]")
    sys.exit(1)

file_path = sys.argv[1]

# numero de linhas
num_lines = None
if len(sys.argv) >= 3:
    try:
        num_lines = int(sys.argv[2])
    except ValueError:
        print("Invalid number of lines. Using default value (reading entire file).")

# nome do arquivo csv, vai ser exportado se tiver esse parametro
output_csv_file = None
if len(sys.argv) >= 4:
    output_csv_file = sys.argv[3] + ".csv"

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


if output_csv_file:
    with open(output_csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Error', 'Count'])
        for error, count in error_counts.items():
            writer.writerow([error, count])

    print(f"Errors exported to {output_csv_file}")

