import json

line_format =  '{"MapID": "", "X": "", "Y": "", "Ground": "", \
    "GroundAnim": "", "Mask": "", "MaskAnim": "", "Mask2": "", \
    "Mask2Anim": "", "Fringe": "", "FringeAnim": "", "Fringe2": "", \
    "Fringe2Anim": "", "Mask3": "", "Mask3Anim": "", "Fringe3": "", \
    "Fringe3Anim": "", "Type": "", "Data1": "", "Data2": "", \
    "Data3": "", "String1": "", "String2": "", "String3": "", \
    "Light": "", "GroundTileset": "", "GroundAnimTileset": "", \
    "MaskTileset": "", "MaskAnimTileset": "", "Mask2Tileset": "", \
    "Mask2AnimTileset": "", "FringeTileset": "", "FringeAnimTileset": \
    "", "Fringe2Tileset": "", "Fringe2AnimTileset": "", \
    "Mask3Tileset": "", "Mask3AnimTileset": "", \
    "Fringe3Tileset": "", "Fringe3AnimTileset": ""}'

def read_map_list():
    map_list = []
    with open('prom_maps.txt', 'r') as oo:
        for line in oo:
            map_list.append(line.replace("\n", ""))
        print(map_list)
        return map_list

def extract():
    map_list = read_map_list()
    prom_path = 'prom_data.json'
    with open('good_map_dicts.json','r') as messy_file:
        write_all(messy_file, map_list, prom_path)

# only when last line is part of map list does this work
def write_all(messy_file, map_list, target_path):
    open(target_path,'w').close()
    with open(target_path,'a+') as target:
        target.write('[\n')
        extract_prom(messy_file, target, map_list)
        target.write(line_format)   # so the last comma gives something
        target.write('\n]')

def extract_prom(messy_file, target, map_list):
    for line in messy_file:
        write_next(map_list, target, line)

def write_next(map_list, target, line):
    tile = json.loads(line)
    if tile['MapID'] in map_list:
        json.dump(tile, target)
        target.write(',\n')

if __name__ == "__main__":
    extract()
