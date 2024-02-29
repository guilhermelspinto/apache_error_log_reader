import sys
import re

if len(sys.argv) < 2:
    print("How to use: python3 elreader.py /path/to/error_log [number_of_lines]")
    sys.exit(1)

file_path = sys.argv[1]

# Definir o número padrão de linhas a serem lidas
num_lines = None
if len(sys.argv) >= 3:
    try:
        num_lines = int(sys.argv[2])
    except ValueError:
        print("Invalid number of lines. Using default value (reading entire file).")

error_counts = {}

with open(file_path, 'r') as f:
    # Ler todas as linhas se o número de linhas não for especificado
    if num_lines is None:
        lines = f.readlines()
    else:
        lines = f.readlines()[-num_lines:]
    for line in lines:
        # Usar expressão regular para extrair o tipo de erro e a mensagem
        match = re.search(r'PHP (Warning|Fatal error): (.+)', line)
        if match:
            error_type = match.group(1)
            error_message = match.group(2).strip()
            # Formatar o tipo de erro e a mensagem
            error = f"PHP {error_type}: {error_message}"
            # Verificar se o erro já foi encontrado antes
            if error in error_counts:
                error_counts[error] += 1
            else:
                error_counts[error] = 1

for error, count in error_counts.items():
    print("-----------------------------------------------------------")
    print(f"Error: {error} - Count: {count}")

