import os
import sys
import logging
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def check_duplicates(file_name):
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    file_path = os.path.join(parent_dir, file_name)

    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        logging.error(f"Arquivo {file_name} não encontrado. Verifique se ele existe no diretório esperado.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Erro inesperado ao processar o arquivo: {e}")
        sys.exit(1)

    seen = set()
    duplicates = [f"Linha {i + 1}: '{line}'" for i, line in enumerate(lines) if line in seen or seen.add(line)]

    if duplicates:
        logging.error(f"{len(duplicates)} duplicatas encontradas no arquivo!")
        logging.error("Detalhes:\n" + "\n".join(duplicates))
        sys.exit(1)

    logging.info("Nenhuma duplicidade encontrada.")
    sys.exit(0)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = 'blocklist.txt'

    check_duplicates(file_name)
