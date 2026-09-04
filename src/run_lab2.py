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

# Group the required scatter plot by water-body tag for clearer visualization.
tags = ["River", "Lake", "Beach", "Falls", "Reef", "Bay", "Gulf"]

# Assigning colors to each tag for better visualization and getting their coordinates.
for tag in tags:
    tagged_points = group.filter_by_tag (tag)

    longitudes = [point.lon for point in tagged_points.points]
    latitudes = [point.lat for point in tagged_points.points]

    plt.scatter (longitudes, latitudes, label = tag)

# Adding labels and title
plt.xlabel ("Longitude")
plt.ylabel ("Latitude")
plt.title ("Visualization of Known Water Bodies in the Philippines")

# Adding a legend. This can be customized based on user preference and on the amount of data involved.
plt.legend (
    title="Water Body Type",
    fontsize = 8,
    title_fontsize = 9,
    markerscale = 0.7
)

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