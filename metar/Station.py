#!/usr/bin/python
#
#    Python module to provide Station information from the ICAO identifiers
#
#    Copyright 2004    Tom Pollard
# 

from .Datatypes import Position


class Station:
    """An object representing a weather Station."""
    
    def __init__(self, id, city=None, state=None, country=None, latitude=None, longitude=None):
        self.id = id
        self.city = city
        self.state = state
        self.country = country
        self.position = Position(latitude, longitude)
        if self.state:
            self.name = "%s, %s" % (self.city, self.state)
        else:
            self.name = self.city
        
station_file_name = "nsd_cccc.txt"
station_file_url = "http://www.noaa.gov/nsd_cccc.txt"

stations = {}

fh = open(station_file_name, 'r')
for line in fh:
    f = line.strip().split(";")
    stations[f[0]] = Station(f[0], f[3], f[4], f[5], f[7], f[8])
fh.close()

if __name__ == "__main__":
    for id in ['KEWR', 'KIAD', 'KIWI', 'EKRK']:
        print(id, stations[id].name, stations[id].country)
