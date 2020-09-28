
def extract_better():
    with open('good_map_tiles.json', 'r') as oo:
#    with open('sample.json', 'r') as oo:
        with open('better_map_tiles.json', 'w') as scr:
            extract(oo, scr)

def extract(from_file, to_file):
    print('Writing...')
    for line in from_file:
        if line == '    {\n':
            to_file.write('{')
        else:
            if line == '    },\n':
                to_file.write('}\n')
            else:
                if line != '  ]\n' and line != '}':   # skips the last brackets
                    to_file.write(line.replace(" ", "").replace('\n',''))

if __name__ == "__main__":
    extract_better()
