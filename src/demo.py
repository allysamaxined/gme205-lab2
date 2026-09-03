from spatial import Point

# p = Point ("A", 121.0, 14.6)
# print (p.id, p.lon, p.lat)
# print (p.to_tuple())

# q = Point ("X", 999, 14)
# print (q.id, q.lon, q.lat)

# Sample/Test to Calculate the Distance using distance_to

p1 = Point ("Calzada, Taguig", 121.0, 14.5)
p2 = Point ("Melchor Hall, UP Diliman", 121.0, 14.6)

distance = p1.distance_to(p2)

print ("Distance: ", distance, "meters")