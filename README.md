# Programming Exercise 2
## Simple Spatial Objects in Python

#### Introduction to the Programming Exercise
This Programming Exercise aims to introduce object-oriented thinking for spatial problems by designing simple objects in Python. At the end of this exercise, users must be able to:
    1. Model spatial entities as objects with their own states and behaviors, not just stuck on being geometries.
    2. Understand and distinguish what "data" is from "meaning."
    3. Implement Python classes and methods for spatial reasoning.
    4. Generate or produce outputs that can be reproduced, reflecting abstraction, representation, responsibility, and scale.

#### Materials/Requirements
Before proceeding to this exercise, users must have the following requirements:
    1. Python 3.x for scripting, spatial data processing, and database interaction.
    2. Visual Studio Code (VS Code) as the primary development environment for Python scripting and Git integration.
    3. Git for version control and managing analytical workflows.

Python Libraries Used
    1. Pandas
    2. Matplotlib
    3. OS
    4. Sys

#### Project Structure
This project specifically follows this required directory structure:
    
    gme205_lab2/
        data
            points.csv
        output
            lab2_preview.png
            lab2_report.json
        src
            demo.py             # This has the executed demosntration of the classes.
            run_lab2.py         # This will load the dataset and return the required outputs.
            spatial.py          # This has the Point and PointSet classes and methods.
        tests
            test_spatial.py     # This can include the test codes used/ran during the process.
        .gitignore
        README.md
        requirements.txt

#### Environment Setup
    1. After creating the root directory, create the virtual environment.
        python -m venv .venv
    2. Activate the venv on the Windows.
        .venv\Scripts\activate
    3. Install required dependencies.
       pip install pandas matplotlib    .
       pip list                 # Run a test to verify their installation
       pip freeze > requirements.text     # Generate a text file containing these dependencies.

! Commands must be executed from the root directory.

#### Running the Program
To demonstrate how the 'Point' and 'PointSet' works, run:
    python src/demo.py

To process the .CSV data and generate outputs, run:
    python src/run_lab2.py

! The data is saved as points.csv inside the data folder.

#### Project Output
By executing 'python src/run_lab2.py', the following outputs will be generated:
    1. Scatter Plot named lab2_preview.png
        This shows the plotted coordinates of the points.
    2. JSON Report named lab2_report.json  
        This contains the total count of points and bounding box of the data.

### Reflections

### 1. Object vs. Geometry: How did modeling points as objects change the way you thought about the data compared to treating them as rows in a table?

Modeling points as objects made me look at them as single entities of their own, that each point became an individual entity with its own state and behavior. By doing it myself, sort of manually, compared to just seeing them on an Attribute Table, I'm able to see these points as equally important and crucial parts of my spatial data, not just as instances that can be found on an Attribute Table.

By programming these points, I was able to develop a better distinction on what a point should and should not have. As the exercises progress (coming from PE1), Ive' noticed a shift in the way I think about data in general. I used to look at these points as something that has all of the information needed so that they can be accessed right away, and everything is in them. However, I noticed that when you shift the way you think and the way you handle the data, you see them differently. Instead of just a feature on a map, they become an integral part of it.


### 2. Responsibility: Which behaviors belonged in Point, which belonged in PointSet, and which belonged in the runner script? Give one concrete example.

With Point, you see it act as a standalone entity that has its own state, behavior, and basically, a purpose it has to stick to. I gave Point its state and attributes. The Point itself has id, coordinates (longitude and latitude), name, and tag. It is responsible for representing its own, unique object. As you can see on the test_spatial.py file, a Point also has the responsibility to validate its own coordinates, calculate its distance from one point to another, convert itself to a tuple, and determine if it's a point of interest.

With PointSet, it becomes entirely different. From having a single entity that has its own role, PointSet represents and manages a collection of Point objects and performs operations that concern the collection as a whole. It appears as though PointSet is the representation of what a set of points are.

With the runner script, this behaves like an environment that makes things happen. In the runner script, I was able to learn and command to:
        1. Find where the data is located and reference it;
        2. Provide me with the information I requested, such as count and bounding box;
        3. Control how the outputs are returned or produced; and
        4. Specify where I want to save my outputs and how to name them.

For example, calculating the distance between two points (using distance_to) can be done by Point, since this deals with the behavior of one point in relation to another. On the other hand, calculating the bounding box is done by PointSet. This is not only because it contains the collection of points, but also because it has the responsibility of providing information about the extent of these points as a whole. Lastly, to visualize them, I need the runner script, as it contains the commands that specify how the outputs will be produced and saved.

### 3. Modeling Insight: How did separating geometry, meaning, and behavior make the spatial logic easier (or harder) to understand?

In programming, it is a typical or usual practice to separate information like geometry, meaning, and behavior as this ensures that the code is specified as to what it needs to execute and return. In my experience working with GIS software, however, this separation was not always apparent to me. I was more accustomed to working with spatial features where their geometry and attributes were already presented together.

Separating geometry, meaning, and behavior helped me understand what a point must and must not do. It helps with understanding what should be done for what part of it. It makes the spatial logic easier in a way that it makes the entire process simpler and more focused. 

When working primarily through GIS software, much of this separation can be hidden from the user. Geometry and attributes are already presented together as features, while the behaviors that operate on them are often accessed through tools. Implementing the objects myself in Python made those responsibilities more explicit.