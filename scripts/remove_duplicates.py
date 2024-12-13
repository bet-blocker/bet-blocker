import os
import logging


def remove_duplicates(file_name):
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    file_path = os.path.join(parent_dir, file_name)

    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    unique_lines = list(dict.fromkeys(lines))

    with open(file_path, 'w') as file:
        file.write("\n".join(unique_lines))

    logging.info(f"Duplicidades removidas. Arquivo atualizado: {file_path}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    remove_duplicates('blocklist.txt')
