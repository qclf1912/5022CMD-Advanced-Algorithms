"""Course class for storing and displaying course information."""

class Course:

    # Initialize a course with its code, name, credit hours, level, and description.
    def __init__(self, code, name, credit_hours, level, description):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.level = level  # "core" or "elective"
        self.description = description

    # Return all course information in a readable format.
    def full_details(self):
        return (
            f"Course Code   : {self.code}\n"
            f"Course Name   : {self.name}\n"
            f"Credit Hours  : {self.credit_hours}\n"
            f"Level         : {self.level.capitalize()}\n"
            f"Description   : {self.description}"
        )

    # Apply the visibility rule: core courses show full details,
    # while elective courses display only their names.
    def visible_profile(self):
        if self.level == "core":
            return self.full_details()
        return f"Course Name   : {self.name}\n(Details hidden: elective course)"
