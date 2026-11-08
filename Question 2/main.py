"""Main program for the University Course Prerequisite System."""

import graphLib
from directedGraph import DirectedGraph


# Display the available course management and prerequisite operations.
def display_menu():
    print("\n==== University Course Prerequisite System ====")
    print("1. View All Courses")
    print("2. View Course Details")
    print("3. View Prerequisites of a Course")
    print("4. View Courses Unlocked by a Course")
    print("5. Add a Course")
    print("6. View Course Profile (elective details hidden)")
    print("7. Add a Prerequisite")
    print("8. Remove a Prerequisite")
    print("9. Exit")


# Initialize the course graph and process the user's menu selections.
def main():
    graph = DirectedGraph()
    by_code = {}

    # Load sample courses into the graph and dictionary for quick lookup.
    for c in graphLib.sample_courses():
        graph.add_vertex(c)
        by_code[c.code] = c

    # Establish the initial prerequisite relationships between courses.
    for pre, post in graphLib.get_sample_edges():
        graph.add_edge(by_code[pre], by_code[post])

    # Continue displaying the menu until the user chooses to exit.
    choice = ""
    while choice != "9":
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        # Execute the operation that matches the selected menu option.
        match choice:
            case "1":
                print("\nAvailable Courses:")
                for i, c in enumerate(graph.vertices(), 1):
                    print(f"{i}. {c.code} - {c.name}")

            case "2":
                c = graphLib.ask_course(by_code)
                if c:
                    print("\n" + c.full_details())

            case "3":
                c = graphLib.ask_course(by_code)
                if c:
                    print(f"\nPrerequisites for {c.code} - {c.name}:")
                    items = graph.list_incoming_adjacent_vertex(c)
                    for p in items:
                        print(f"- {p.code} ({p.name})")
                    if not items:
                        print("- None")

            case "4":
                c = graphLib.ask_course(by_code)
                if c:
                    print(f"\nCourses unlocked by {c.code} - {c.name}:")
                    items = graph.list_outgoing_adjacent_vertex(c)
                    for u in items:
                        print(f"- {u.code} ({u.name})")
                    if not items:
                        print("- None")

            case "5":
                graphLib.add_course(graph, by_code)

            case "6":
                c = graphLib.ask_course(by_code)
                if c:
                    print("\n" + c.visible_profile())

            case "7":
                graphLib.add_prerequisite(graph, by_code)

            case "8":
                graphLib.remove_prerequisite(graph, by_code)

            case "9":
                print("\nExiting program. Goodbye! :D")

            case _:
                print("  Invalid choice. Please enter a number from 1 to 9.")


# Run the main function when this file is executed directly.
if __name__ == "__main__":
    main()
