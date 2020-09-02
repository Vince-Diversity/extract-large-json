import pandas as pd
import json

#map_list = ['s999', 's1622']
def read_map_list():
    map_list = []
    with open('prom_maps.txt', 'r') as oo:
        for line in oo:
            map_list.append(line.replace("\n", ""))
        print(map_list)
        return map_list

def extract():
    # about 1000 lines per kB
#    messy_df = pd.read_json('test_prom_records.json',chunksize=5,lines=True)
#    messy_df = pd.read_json('good_map_records.json',chunksize=1000*1000*10,lines=True)
#    messy_df = pd.read_json('s1501_error.json',chunksize=10,lines=True)
#    messy_df = pd.read_json('s1501_fixed.json',chunksize=10,lines=True)
#    messy_df = pd.read_json('s1501_fixed_2.json',chunksize=10,lines=True)
    messy_df = pd.read_json('good_map_tiles.json',chunksize=10,lines=True,
        encoding='ISO-8859-1')
    write_all(messy_df)

def write_all(messy_df):
    open('prom_data.json','w').close()
    with open('prom_data.json','a+') as target:
        map_list = read_map_list()
        for chunk in messy_df:
            print("Looking in chunk", chunk)
            messy_page = chunk.to_dict()
            extract_prom(messy_page, target, map_list)

def extract_prom(messy_page, target, map_list):
    messy_content = messy_page["RECORDS"]
    for chunk_index, tile in messy_content.items():
        if tile['MapID'] in map_list:
            json.dump(tile, target, indent=1)

if __name__ == "__main__":
    extract()
