import argparse
import re
import sys
import textwrap
import unicodedata

# Clear accents, numbers and any punctuation
def normalize_text(text: str):
    decomposed = unicodedata.normalize('NFD', text)
    cleaned = re.sub(r'[^A-Za-z\s]', '', decomposed)
    return " ".join(cleaned.split())

# Wrap lines to a specified width without breaking words
def normalize_width(text: str, width: int = 120):
    return textwrap.fill(
        text,
        width,
        break_long_words=False
    )

def parse_args():
    parser = argparse.ArgumentParser(
        description='Normalize text and wrap lines.'
    )
    parser.add_argument('input_file', nargs='?')
    parser.add_argument('-o', '--output')
    parser.add_argument('-w', '--width', type=int, default=120)
    
    return parser.parse_args()

# IO
def read_input(path: str | None) -> str:
    if path:
        with open(path, encoding='utf-8') as f:
            return f.read()
    return sys.stdin.read()
def write_output(text: str, path: str | None):
    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
    else:
        print(text)

def main():
    args = parse_args()

    content = read_input(args.input_file)

    result = normalize_text(content)
    result = normalize_width(result, args.width)

    write_output(result, args.output)

if __name__ == '__main__':
    main()
