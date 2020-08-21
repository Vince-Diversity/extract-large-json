How to extract all s-tagged map info:

Place the extract_good_data.py
in the same directory as the map_tiles.json.

This is how I'd run this for the first time:
> python3 -m pip install ijson
> python3 extract_good_data.py -h
> python3 extract_good_data.py 10
> python3 extract_good_data.py 5000
(May take 25 minutes to run.)

The script takes twice the minimum amount of time
necessary to extract all s-tagged map info
into a new file.