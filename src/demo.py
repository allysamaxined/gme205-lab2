from spatial import Point, PointSet 

# Testing out the PointSet class with a CSV file.

group = PointSet.from_csv ("data/points.csv")
print ("Count: ", group.count())
print ("Bounding Box: ", group.bbox())
river_group = group.filter_by_tag ("River")
print ("Known Rivers in the Philippines: ", river_group.count())