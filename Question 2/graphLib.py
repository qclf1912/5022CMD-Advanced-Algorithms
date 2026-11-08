"""Helper functions for course data and prerequisite graph operations."""

from course import Course


# Return the initial sample courses used to populate the graph.
def sample_courses():
    return [
        Course("CS101", "Introduction to Programming", 4, "core", "Fundamentals of programming using Python."),
        Course("CS201", "Data Structures", 4, "core", "Lists, stacks, queues, trees, hash tables and graphs."),
        Course("CS301", "Algorithms", 4, "core", "Algorithm design, analysis and complexity."),
        Course("CS302", "Database Systems", 3, "elective", "Relational model, SQL and normalisation."),
        Course("CS401", "Software Engineering", 3, "core", "Software lifecycle, design and teamwork."),
        Course("CS305", "Artificial Intelligence", 3, "elective", "Search, reasoning and machine learning basics."),
    ]


# Define the initial directed edges representing prerequisite relationships.
def get_sample_edges():
    return [
        ("CS101", "CS201"),
        ("CS201", "CS301"),
        ("CS101", "CS301"),
        ("CS201", "CS302"),
        ("CS302", "CS401"),
        ("CS301", "CS401"),
        ("CS301", "CS305"),
    ]


# Find a course using its code and return the corresponding Course object.
def ask_course(by_code, prompt="Enter Course Code: "):
    code = input(prompt).strip().upper()
    course = by_code.get(code)
    if course is None:
        print("Course not found.")
    return course


# Validate and add a new course to the graph and course dictionary.
def add_course(graph, by_code):
    code = input("New course code: ").strip().upper()
    if not code or code in by_code:
        print("Course code is empty or already exists.")
        return
    name = input("Course name: ").strip()
    level = input("Level (core/elective): ").strip().lower()
    if level not in ("core", "elective") or not name:
        print("Invalid name or level.")
        return
    try:
        credit_hours = int(input("Credit hours: "))
    except ValueError:
        print("Credit hours must be a whole number.")
        return
    desc = input("Description: ").strip()
    course = Course(code, name, credit_hours, level, desc)
    graph.add_vertex(course)
    by_code[code] = course
    print(f"Course {code} added successfully.")


# Add a prerequisite relationship after checking that it does not create a cycle.
def add_prerequisite(graph, by_code):
    target = ask_course(by_code, "Course X (that needs the prerequisite): ")
    if not target:
        return
    prereq = ask_course(by_code, "Course Y (to become the prerequisite): ")
    if not target or not prereq:
        return
    if target is prereq:
        print("A course cannot be its own prerequisite.")
    elif graph.has_path(target, prereq):
        # Reject the edge if the target can already reach the proposed prerequisite.
        print("Rejected: this would create a circular prerequisite.")
    elif graph.add_edge(prereq, target):
        print(f"{prereq.code} is now a prerequisite of {target.code}.")
    else:
        print("That prerequisite already exists.")


# Remove an existing prerequisite relationship from the directed graph.
def remove_prerequisite(graph, by_code):
    target = ask_course(by_code, "Course X (to remove prerequisite from): ")
    if not target:
        return
    prereq = ask_course(by_code, "Prerequisite Y (to remove): ")
    if not target or not prereq:
        return
    if graph.remove_edge(prereq, target):
        print(f"{prereq.code} is no longer a prerequisite of {target.code}.")
    else:
        print("That prerequisite relationship does not exist.")
