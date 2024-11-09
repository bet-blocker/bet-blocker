import os
import sys
import logging

def check_duplicates_bets(file_name):
    # Obtenha o caminho da pasta anterior ao diretório do script
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    file_path = os.path.join(parent_dir, file_name)

    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    
    seen = {}
    duplicates = []
    for line_number, line in enumerate(lines, start=1):
        if line in seen:
            logging.info(f"Duplicated BET found on line {line_number}: '{line}'")
            duplicates.append(line_number)
        seen[line] = line_number

    if duplicates:
        logging.info(f"Duplicate lines: {duplicates}")
        sys.exit(1)  # Use a standard error code for failure
    else:
        logging.info("No duplicates found.")
        sys.exit(0)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    check_duplicates_bets('blocklist.txt')
