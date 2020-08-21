# The useful data is crammed below a lot of junk.
# The flag for the topmost useful map is MapID: "s1".
# s is tagged to all staff-made maps.
# This script guesses the location of this flag,
# verifies the flag and copies all below to good_map_tiles.json.
import ijson
from itertools import islice
from os import SEEK_END
import argparse

# counts opening brackets at start of file
header_size = 3
# approximate location of s1, found in test runs
test_run_location_percent = 8567631.19
# byte array decoder that
# gets rid of unnecesary \n which the 'rb' somehow spawns
decode = lambda b: b.decode()[:-1]

def extract(guess):
    with open('map_tiles.json', 'rb') as big_file:
        print('Climbing this high up...', guess)
        guess_file = open('temp.json', 'r+')
        make_guess_file(-guess, big_file, guess_file)
        parser = ijson.parse(guess_file)
        flag_location = goto_first_flag(parser)
        if not flag_location:
            print('Not high enough!')
            open('temp.json', 'w').close()  # empty temp.json
            return
    # Flag is found
    print("We're 50 % there now.")
    good_file_name = 'good_map_tiles.json'
    with open(good_file_name, 'w') as good_file:
        extract_from_flag(flag_location, guess_file, good_file)
        print('Extracted there now!')
    guess_file.close()
    open('temp.json', 'w').close()  # empty temp.json

def write_header(from_file, to_file):
    for i in range(header_size):
        to_file.write(decode(from_file.readline()))

def make_guess_file(guess, big_file, guess_file):
    write_header(big_file, guess_file)
    big_file.seek(guess, SEEK_END)
    big_file.readline() # go to end of line
    for line in big_file:
        guess_file.write(decode(line))
    # recover the final bracket
    big_file.seek(-1, SEEK_END)
    guess_file.write(big_file.readline().decode())
    guess_file.seek(0)  # reset location

def goto_first_flag(parser):
    count = 0
    for prefix, event, value in parser:
        if event == 'end_map':  # event at opening bracket
            count = count + 2   # pretend each bracket is counted twice
        if prefix == "RECORDS.item.MapID":
            if value != None and len(value) > 1:
                value_flag = value
                if value_flag == "s1":
                    print('Found map flag! ID: ', value)
                    flag_location = int(count/2) # json.parse counts twice
                    flag_location -= 1  # include the flag MapID
                    flag_location -= 1  # include opening bracket
                    return flag_location
        count += 1
    return False

def extract_from_flag(flag, from_file, to_file):
    from_file.seek(0)
    practically_inf = int(test_run_location_percent*100)
    print('Writing to good_map_tiles.json...')
    for i in range(header_size):
        to_file.write(from_file.readline())
    for line in islice(from_file, flag, practically_inf):
        to_file.write(line)

def take_guesses():
    io_parser = argparse.ArgumentParser(
        description='How many millions of bits should we climb?'
        )
    io_parser.add_argument('g', metavar='guess', type=int)
    return io_parser.parse_args().g*999999

if __name__ == "__main__":
    extract(take_guesses())