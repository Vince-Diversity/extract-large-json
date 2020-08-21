# Verifies large json files
# by iterating over all of it.
import ijson

def verify(file, file_name):
    print('Verifying that ' +file_name + ' is readable...')
    parser = ijson.parse(file)
    for prefix, event, value in parser: pass
    print('Verification complete!')
    return None

if __name__ == "__main__":
    file_name = "good_map_tiles.json"
    with open(file_name, 'r') as file:
        verify(file, file_name)
