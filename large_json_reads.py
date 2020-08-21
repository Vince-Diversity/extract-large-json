import ijson

def rw_maps():
    with open('map_tiles.json', 'rb') as big_file:
        big_file.seek(0, 0)
        parser = ijson.parse(big_file)
        with open('sample_tile_data.json', 'w') as small_file:
            find_first_flag(parser, small_file)
        small_file.close()
    big_file.close()

def find_first_flag(parser, to_file):
    # skip the MapID: ""
    beforeThat = True
    while beforeThat:
        prefix, _, _ = parser.__next__()
        print(prefix)
        if prefix == 'RECORDS.item.MapID':
            beforeThat = False
            return

    print('Finding maps...')
    count = 0
    for prefix, event, value in parser:

        if count%9999999 == 0:
            print('At count ', count, prefix, event, value)
        if prefix == "RECORDS.item.MapID":
            if value != None:
                value_flag = value[0]
                if value_flag == "s":
                    print('Found!', prefix, event, value, 'at count', count)
                    return
        count += 1

if __name__ == "__main__":
    rw_maps()
