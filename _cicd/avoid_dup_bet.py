import os
import sys
import logging


def check_duplicates(file_name):
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    file_path = os.path.join(parent_dir, file_name)

    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    seen = set()
    duplicates = [f"Linha {i + 1}: '{line}'" for i, line in enumerate(lines) if line in seen or seen.add(line)]

    if duplicates:
        logging.error("Commit rejeitado! URLs duplicadas encontradas:\n" + "\n".join(duplicates))
        logging.error("Resolva as duplicidades executando: python scripts/remove_duplicates.py")
        sys.exit(1)

    logging.info("Nenhuma duplicidade encontrada.")
    sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    check_duplicates('blocklist.txt')