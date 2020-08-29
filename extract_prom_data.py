#
import pandas as pd
import json

map_list = ['s999', 's1622']

def extract():
#    messy_df = pd.read_json('test_prom_data.json')
#    messy_df = pd.read_json('test_prom_records.json',lines=True)
    messy_df = pd.read_json('test_prom_records.json',chunksize=10,lines=True)
#    messy_df.to_json('prom_data.json',orient='records',lines=True)
#    messy_df.to_json('test_prom_records.json',orient='records',lines=True)
    write_all(messy_df)

def write_all(messy_df):
    open('prom_data.json','w').close()
    with open('prom_data.json','a+') as target:
        for chunk in messy_df:
            messy_page = chunk.to_dict()
            extract_prom(messy_page, target)

def extract_prom(messy_page, target):
    messy_content = messy_page["RECORDS"]
    for chunk_index, tile in messy_content.items():
        if tile['MapID'] in map_list:
            json.dump(tile, target, indent=1)

if __name__ == "__main__":
    extract()
