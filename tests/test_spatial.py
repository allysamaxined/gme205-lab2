# Transferring all the tests from the demo.py file to this test_spatial.py file for better organization and separation of concerns.

import sys # Gives access to Python's runtime/environment and allows for the manipulation of the Python path and other system-level operations.
import os # Gives Python the tools so it can interact with the operating system.

sys.path.append (os.path.abspath (os.path.join (os.path.dirname (__file__), "..", "src"))) # This tells Python to look into other folders when searching for files.

from spatial import Point, PointSet

# Test on tuples
# To try these out, add/remove the comment symbol (#) at the beginning of each line before running the code.

# p = Point ("A", 121.0, 14.6)
# print (p.id, p.lon, p.lat)
# print (p.to_tuple())

# q = Point ("X", 999, 14)
# print (q.id, q.lon, q.lat)

# # Test to calculate the distance using distance_to

# p1 = Point ("Calzada, Taguig", 121.0, 14.5)
# p2 = Point ("Melchor Hall, UP Diliman", 121.0, 14.6)

# distance = p1.distance_to(p2)

# print ("Distance: ", distance, "meters")

# Testing out the PointSet class with a few points.

p1 = Point ("Calzada, Taguig", 121.0, 14.5, "Home", "Residential") 
p2 = Point ("Boracay Island", 121.9, 11.9, "Tourist Destination", "Recreational")
p3 = Point ("Siquijor Island", 123.5, 9.2, "Tourist Destination", "Recreational")

group = PointSet ([p1, p2, p3])

print ("Count: ", group.count())
print ("Bounding Box: ", group.bbox())

recreational_group = group.filter_by_tag ("Recreational")
print ("Count of Recreational Points/Areas: ", recreational_group.count())