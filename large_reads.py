# Reads large files between two lines [a,b]
# and copies them to a sample file.
from itertools import islice
import argparse
from math import inf

def large_read(a, b):
    with open("good_map_tiles.json", 'r') as oo:
        with open("sample_map_tiles.json", 'w') as scr:
            add_head(oo, scr)
            for line in islice(oo, a, b):
                scr.write(line)
        scr.close()
    oo.close()

# JSON head: the RECORD section
def add_head(oo, scr):
    for line in islice(oo, 0, 2):
        scr.write(line)

def make_parser():
    parser = argparse.ArgumentParser(
        description='The two arguments determine interval [a,b] \
        of lines')
    parser.add_argument('a', metavar='a',
        type=int, help = "Starts copying from this line.")
    parser.add_argument('b', metavar='b', type=int, help = "End \
        copying on his line.")
    args = parser.parse_args()
    return args.a, args.b

if __name__ == "__main__":
    a, b = make_parser()
    large_read(a, b)
