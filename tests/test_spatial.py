# This file verifies if the Point and PointSet classes are working
# as intended.

import os
import sys
import unittest

# This tells Python to look inside the src folder for spatial.py.
sys.path.append (
    os.path.abspath (
        os.path.join (os.path.dirname (__file__), "..", "src")
    )
)

from spatial import Point, PointSet


class TestPoint (unittest.TestCase):

    def test_to_tuple (self):
        point = Point ("A", 121.0, 14.6)

        self.assertEqual (point.to_tuple(), (121.0, 14.6))

    def test_invalid_longitude (self):
        with self.assertRaises (ValueError):
            Point ("X", 999, 14.0)

    def test_invalid_latitude (self):
        with self.assertRaises (ValueError):
            Point ("X", 121.0, 100.0)

    def test_distance_to (self):
        point = Point ("A", 121.0, 14.6)

        distance = point.distance_to (point)

        self.assertAlmostEqual (distance, 0.0)

    def test_from_row (self):
        row = {
            "id": "P1",
            "lon": 121.0580,
            "lat": 14.6507,
            "name": "Quezon Hall",
            "tag": "poi"
        }

        point = Point.from_row (row)

        self.assertEqual (point.id, "P1")
        self.assertEqual (point.name, "Quezon Hall")
        self.assertTrue (point.is_poi())


class TestPointSet (unittest.TestCase):

    def setUp (self):
        self.p1 = Point (
            "P1", 121.0, 14.5, "Location 1", "poi"
        )
        self.p2 = Point (
            "P2", 122.0, 15.0, "Location 2", "building"
        )
        self.p3 = Point (
            "P3", 123.0, 16.0, "Location 3", "poi"
        )

        self.group = PointSet ([self.p1, self.p2, self.p3])

    def test_count (self):
        self.assertEqual (self.group.count(), 3)

    def test_bbox (self):
        expected_bbox = (121.0, 14.5, 123.0, 16.0)

        self.assertEqual (self.group.bbox(), expected_bbox)

    def test_filter_by_tag (self):
        poi_group = self.group.filter_by_tag ("poi")

        self.assertEqual (poi_group.count(), 2)
        self.assertEqual (self.group.count(), 3)

    def test_from_csv (self):
        data_path = os.path.abspath (
            os.path.join (
                os.path.dirname (__file__),
                "..",
                "data",
                "points.csv"
            )
        )

        csv_group = PointSet.from_csv (data_path)

        self.assertEqual (csv_group.count(), 10)
        self.assertEqual (
            csv_group.bbox(),
            (121.0538, 14.6478, 121.0672, 14.6573)
        )


if __name__ == "__main__":
    unittest.main()