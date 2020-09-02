# Verifies large json files
# by iterating over all of it.
import ijson

def verify(file, file_name):
    print('Verifying that ' + file_name + ' is readable...')
    with open(file_name) as file:
        for prefix, event, value in ijson.parse(file): pass
    print('Verification complete!')
    return None

if __name__ == "__main__":
#    file_name = "good_map_records.json"
    file_name = "s1501_error.json"
    with open(file_name, 'r') as file:
        verify(file, file_name)
