from spatial import PointSet
import matplotlib.pyplot as plt
import json # For the JSON file output

# Load the .CSV file containing the points and create a PointSet object.
group = PointSet.from_csv ("data/points.csv")

# Get the count and bounding box of the points in the PointSet.
count = group.count()
bbox = group.bbox()

print ("Count: ", count)
print ("Bounding Box: ", bbox)

# Getting the coordinates from the fifteen (15) points I have in the PointSet.
longitudes = [point.lon for point in group.points]
latitudes = [point.lat for point in group.points]

# Using Matplotlib to plot the points on a scatter plot
plt.scatter (longitudes, latitudes)

# Adding labels and title
plt.xlabel ("Longitude")
plt.ylabel ("Latitude")
plt.title ("Visualization of Known Water Bodies in the Philippines")

# Saving the plot
plt.savefig ("output/lab2_preview.png")

# Closing
plt.close()

# Generating the summary report
report = {
    "total_point_count": count,
    "bounding_box" : bbox
}

# Saving the report as a JSON file
with open ("output/lab2_report.json", "w") as f:
    json.dump (report, f, indent = 4)