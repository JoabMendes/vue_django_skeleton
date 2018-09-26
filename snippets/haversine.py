
from math import radians, cos, sin, asin, sqrt


def haversine(lat1, lon1, lat2, lon2):

    R = 6372.8 # 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(d_lat/2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon/2)**2
    c = 2 * asin(sqrt(a))

    return R * c




lon1 = -35.21107208163892
lat1 = -5.846766713329185
lon2 = -76.49472889999998
lat2 = 44.2374429


print(haversine(lat1, lon1, lat2, lon2))