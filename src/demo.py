from spatial import PointSet

group = PointSet.from_csv("data/points.csv")

print("Count:", group.count())
print("Bounding Box:", group.bbox())

poi_group = group.filter_by_tag("poi")
print("Number of POIs:", poi_group.count())