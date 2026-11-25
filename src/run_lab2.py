from collections import Counter
import json
from pathlib import Path

import matplotlib.pyplot as plt

from spatial import PointSet


# Prepare the input and output paths.
data_path = Path("data/points.csv")
output_directory = Path("output")
output_directory.mkdir(exist_ok=True)

# Load the points.
group = PointSet.from_csv(data_path)

count = group.count()
bbox = group.bbox()

print("Count:", count)
print("Bounding Box:", bbox)

# Plot every point, grouped according to its tag.
tags = sorted(
    {
        point.tag
        for point in group.points
        if point.tag
    }
)

for tag in tags:
    tagged_points = group.filter_by_tag(tag)

    longitudes = [point.lon for point in tagged_points.points]
    latitudes = [point.lat for point in tagged_points.points]

    plt.scatter(longitudes, latitudes, label=tag)

# Label the plot.
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Spatial Objects in UP Diliman")
plt.legend(title="Point Tag")
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save and close the plot.
plt.savefig(
    output_directory / "lab2_preview.png",
    dpi=300,
)
plt.close()

# Count the points belonging to each tag.
tag_counts = Counter(
    point.tag or "untagged"
    for point in group.points
)

# Generate the JSON summary.
report = {
    "total_point_count": count,
    "bounding_box": list(bbox),
    "counts_per_tag": dict(sorted(tag_counts.items())),
}

with open(
    output_directory / "lab2_report.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(report, file, indent=4)

print("Created output/lab2_preview.png")
print("Created output/lab2_report.json")