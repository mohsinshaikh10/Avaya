import geocoder
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy import distance

geocoder = Nominatim(user_agent="dist_calculator")
src = input("Enter Source: ")
dest = input("Enter the Destination: ")

srcCoordinate = geocoder.geocode(src)
destCoordinate = geocoder.geocode(dest)

srcLat, srcLong = (srcCoordinate.latitude),(srcCoordinate.longitude)
destLat, destLong = (destCoordinate.latitude),(destCoordinate.longitude)

source = (srcLat,srcLong)
destination = (destLat,destLong)

print(distance.distance(source,destination))
