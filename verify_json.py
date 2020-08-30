# Verifies large json files
# by iterating over all of it.
import pandas as pd

def verify(file, file_name):
    print('Verifying that ' +file_name + ' is readable...')
    df = pd.read_json('test_prom_records.json',lines=True)
    for line in df: pass
    print('Verification complete!')
    return None

if __name__ == "__main__":
    file_name = "good_map_tiles.json"
    with open(file_name, 'r') as file:
        verify(file, file_name)
