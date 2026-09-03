from spatial import Point, PointSet # Added PointSet here.

# p = Point ("A", 121.0, 14.6)
# print (p.id, p.lon, p.lat)
# print (p.to_tuple())

# q = Point ("X", 999, 14)
# print (q.id, q.lon, q.lat)

# Sample/Test to Calculate the Distance using distance_to

# p1 = Point ("Calzada, Taguig", 121.0, 14.5)
# p2 = Point ("Melchor Hall, UP Diliman", 121.0, 14.6)

# distance = p1.distance_to(p2)

# print ("Distance: ", distance, "meters")

# I'm going to test the PointSet class here, so I commented out or used # for the previous code above.

p1 = Point ("Calzada, Taguig", 121.0, 14.5, "Home", "Residential")
p2 = Point ("Boracay Island", 121.9, 11.9, "Tourist Destination", "Recreational")
p3 = Point ("Siquijor Island", 123.5, 9.2, "Tourist Destination", "Recreational")

group = PointSet ([p1, p2, p3])

print ("Count: ", group.count())
print ("Bounding Box: ", group.bbox())

recreational_group = group.filter_by_tag ("Recreational")
print ("Count of Recreational Points/Areas: ", recreational_group.count()   )
