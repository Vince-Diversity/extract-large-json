A map_tiles.json can be exported from the database,
that's what Jake did.

How to extract all s-tagged map info from map_tiles.json:

Place the extract_good_data.py
in the same directory as the map_tiles.json.

This is how I'd run this for the first time:
> python3 -m pip install ijson
> python3 extract_good_data.py -h
> python3 extract_good_data.py 10
> python3 extract_good_data.py 4000
(May take 25 minutes to run. The script takes twice the time
necessary to extract all s-tagged map info
into a new file.)

Now the file should be small enough to be sent to me.

If you're curious, this is the rest of the process:
Specify all maps to extract by adding it in prom_maps.txt
> python3 extract_prom_data.py
(Takes about two minutes.)
The maps are now exported to prom_data.json.