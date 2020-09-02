import json

def read_map_list():
    map_list = []
    with open('prom_maps.txt', 'r') as oo:
        for line in oo:
            map_list.append(line.replace("\n", ""))
        print(map_list)
        return map_list

def extract():
    with open('good_map_dicts.json','r') as messy_file:
        write_all(messy_file)

def write_all(messy_file):
    open('prom_data.json','w').close()
    with open('prom_data.json','a+') as target:
        map_list = read_map_list()
        extract_prom(messy_file, target, map_list)

def extract_prom(messy_file, target, map_list):
    for line in messy_file:
        tile = json.loads(line)
        if tile['MapID'] in map_list:
            json.dump(tile, target)
            target.write('\n')

if __name__ == "__main__":
    extract()
