import re
from pathlib import Path

def load_folder():
    txtFolder = Path('./txt files to search')
    glob = list(txtFolder.glob('*.txt'))
    return glob

def search_input():
    search = input('Input Regex to search for: ')
    regex = re.compile(search)
    return regex

def search_folder(RE):
    for path in glob:
        file = open(path)
        fileContent = file.readlines()
        for line in fileContent:
            match = RE.search(line)
            if match != None:
                print(f'Regex found in \"{path}\":')
                print(line)

if __name__ == '__main__':
    glob = load_folder()
    regex = search_input()
    search_folder(regex)


