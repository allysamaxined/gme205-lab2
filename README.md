# Programming Exercise 2
## Simple Spatial Objects in Python

#### Introduction to the Programming Exercise
This laboratory aims to introduce object-oriented thinking for spatial problems by designing simple spatial objects in Python. At the end of this exercise, users should be able to:

1. Model spatial entities as objects with their own states and behaviors, instead of treating them only as geometries.
2. Understand and distinguish data from meaning.
3. Implement Python classes and methods for spatial reasoning.
4. Generate reproducible outputs that reflect abstraction, representation, responsibility, and scale.

#### Materials and Requirements

Before proceeding with this exercise, users must have the following:

1. Python 3.x for scripting and spatial data processing.
2. Visual Studio Code as the primary development environment for Python scripting and Git integration.
3. Git for version control and managing the project workflow.

#### Python Libraries Used

1. Pandas
2. Matplotlib

#### Project Structure

This project follows the required directory structure:

```text
gme205-lab2/
├── data/
│   └── points.csv
├── output/
│   ├── lab2_preview.png
│   └── lab2_report.json
├── src/
│   ├── demo.py
│   ├── run_lab2.py
│   └── spatial.py
├── tests/
│   └── test_spatial.py
├── .gitignore
├── README.md
└── requirements.txt
```

- `demo.py` contains the demonstration of the classes.
- `run_lab2.py` loads the dataset and generates the required outputs.
- `spatial.py` contains the `Point` and `PointSet` classes and methods.
- `test_spatial.py` contains the tests used to check the classes and methods.

#### Environment Setup

1. From the project root, create the virtual environment:

```powershell
python -m venv .venv
```

2. Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install the required dependencies:

```powershell
python -m pip install pandas matplotlib
```

4. Verify their installation:

```powershell
python -m pip list
```

5. Generate the dependency list:

```powershell
python -m pip freeze > requirements.txt
```

All commands must be executed from the project root directory.

#### Running the Program

To demonstrate how `Point` and `PointSet` work, run:

```powershell
python src/demo.py
```

To process the CSV data and generate the required outputs, run:

```powershell
python src/run_lab2.py
```

The data is stored as `points.csv` inside the `data` folder.

#### Project Outputs

Executing `python src/run_lab2.py` generates the following outputs:

1. Scatter plot named `lab2_preview.png`  
   This shows the plotted coordinates of the points, grouped according to their tags.

2. JSON report named `lab2_report.json`  
   This contains the total point count, bounding box, and counts per tag.

### Reflections

### 1. Object vs. Geometry

**How did modeling points as objects change the way you thought about the data compared to treating them as rows in a table?**

Modeling points as objects made me look at them as individual entities. Each point became an entity with its own state and behavior. By implementing the points myself, instead of only seeing them in an attribute table, I was able to recognize them as equally important and crucial parts of the spatial data.

By programming these points, I developed a better understanding of what a point should and should not contain. As the exercises progressed from PE1, I've noticed a shift in the way I think about data in general. I previously looked at points as features containing all the information needed to access and use them immediately.

Changing the way I handled the data helped me see the points differently. Instead of being only features on a map or rows in a table, they became individual and meaningful parts of the spatial model.

### 2. Responsibility

**Which behaviors belonged in Point, which belonged in PointSet, and which belonged in the runner script? Give one concrete example.**

`Point` acts as a standalone entity with its own state, behavior, and purpose. A `Point` has an ID, coordinates consisting of longitude and latitude, a name, and a tag. It is responsible for representing one unique spatial object.

A `Point` is also responsible for validating its coordinates, calculating its distance from another point, converting its coordinates to a tuple, and determining whether it is a point of interest.

`PointSet` represents and manages a collection of `Point` objects. It performs operations that concern the collection as a whole, such as counting the points, calculating their bounding box, and filtering them according to their tags.

The runner script acts as the environment that makes the complete process happen. It:

1. Locates and loads the data.
2. Requests information such as the count and bounding box.
3. Controls how the outputs are produced.
4. Specifies where the outputs are saved and how they are named.

For example, calculating the distance between two points using `distance_to()` belongs to `Point` because it describes the behavior of one point in relation to another. Calculating the bounding box belongs to `PointSet` because it describes the extent of the entire collection. Creating the visualization belongs to the runner script because the script controls how the output is produced and saved.

### 3. Modeling Insight

**How did separating geometry, meaning, and behavior make the spatial logic easier or harder to understand?**

Separating information such as geometry, meaning, and behavior ensures that each part of the code has a specific responsibility. In my experience working with GIS software, this separation was not always apparent because I was accustomed to working with spatial features whose geometries and attributes were already presented together.

Separating geometry, meaning, and behavior helped me understand what a point should and should not do. It also helped me determine which part of the program should perform a particular operation. This made the spatial logic easier to understand because the entire process became simpler and more focused.

When working primarily through GIS software, much of this separation can be hidden from the user. Geometry and attributes are already presented together as features, while the behaviors that operate on them are often accessed through tools. Implementing the objects myself in Python made those responsibilities more explicit.