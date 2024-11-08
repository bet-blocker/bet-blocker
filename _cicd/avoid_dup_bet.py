import sys
import logging

def check_duplicates_bets(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    
    seen = {}
    for line_number, line in enumerate(lines, start=1):
        if line in seen:
            logging.info(f"Duplicated BET found on line {line_number}: '{line}'")
            sys.exit(line_number)
        seen[line] = line_number

    logging.info("No duplicates found.")
    sys.exit(0)

if __name__ == "__main__":
    check_duplicates_bets('../blocklist.txt')

