from geopy.geocoders import Nominatim
import random
import math
import webbrowser

loc = Nominatim(user_agent="GetLoc")

getLoc = loc.geocode(input("enter starting address: "))

print("current address: " + getLoc.address)

print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)

maxDist = float(input("What is the max distance you would like to travel? (km): "))

# converting km to degrees
maxDist = maxDist / 111.139

# generating the distance traveled on the 'x' axis
travelLatitude = float(random.uniform(-maxDist, maxDist))

# calculating the max possible travel length on the 'y' axis
longitudeMax = float(math.sqrt((maxDist * maxDist) - (abs(travelLatitude) * abs(travelLatitude))))

# Generating new longitude value
travelLongitude = float(random.uniform(-longitudeMax, longitudeMax))

newLatitude = float(travelLatitude + getLoc.latitude)
newLongitude = float(travelLongitude + getLoc.longitude)

print("new Latitude = ", newLatitude)
print("new Longitude = ", newLongitude)

geoLoc = Nominatim(user_agent="GetLoc")
locTuple = (newLatitude, newLongitude)

newLocName = geoLoc.reverse(locTuple)
print("Your new location is: " + newLocName.address)

browser = input("open location in web browser? (y/n): ")

if browser == 'y':

    webbrowser.open("https://www.google.com/maps/search/?api=1&query=" + str(newLatitude)
                    + ',' + str(newLongitude), new=2)
