from HomeworkTracker import Assignment
from HomeworkTracker import HomeworkTracker
from InOutFileCreation import FileGeneration

default_csv = "homework_data.csv"

# Creates the functions that the driver class calls to make the driver more readable.
class FunctionCalls:
    # Opens the default homework file on startup.
    # Input: None
    # Output: None
    def on_startup(default_csv) -> HomeworkTracker:
        hwtracker = HomeworkTracker()
        hwtracker = FunctionCalls.open_file(default_csv)
        return hwtracker
    
    # Opens csv_file.
    # Input: File name.
    # Output: None.
    def open_file(csv_file) -> HomeworkTracker:
        hwtracker = HomeworkTracker()
        try:
            hwtracker = FileGeneration.read_file(csv_file)
            return hwtracker
        except FileNotFoundError as e:
            print(f"File {csv_file} not found.")
    
    # Gets desired user operation.
    # Input: Character representing the desired operation.
    # Output: Operation character.
    def prompt_for_option():
        print("\nWhat would you like to do?")
        print("Enter the character in parenthesis.")
        print("(A)dd Assignment, (D)isplay Assignments, (O)pen File, (R)emove Assignment, (S)ave CSV File, (Q)uit")
        operation = input().lower()
        return operation
    
    # Adds an assignment to the HomeworkTracker.
    # Input: Assignment details.
    # Output: Prints if the assignment was invalid.
    def add_assignment(self) -> HomeworkTracker:
        print("Enter assignment name: ")
        name = input()
        print("Enter course name: ")
        course = input()
        print("Enter due date (MM/DD): ")
        due_date = input()
        print("Enter description (optional): ")
        desc = input()
        new_assignment = Assignment(name, course, due_date, desc)
        self.addAssignment(new_assignment)
        return self
    
    # Removes an assignment from the HomeworkTracer.
    # Input: Assignment name.
    # Output: None.
    def remove_assignment(self) -> HomeworkTracker:
        print("Enter assignment name: ")
        assignment_name = input()
        self.removeAssignment(assignment_name)
        return self    
    
    # Writes the CSV file to store the homework assignments.
    # Input: hwtracker - HomeworkTracker object with assignments.
    # Input: csv_file - output file name.
    # Output: None.
    def write_file(hwtracker, csv_file):
        FileGeneration.write_file(hwtracker, csv_file)
        
    # Displays assignments.
    # Input: Organization format.
    # Output: Prints the assignments.
    def display_assignments(hwtracker):
        print("How should the items be formatted? (U)norganized, by (C)lass, by (D)ue date.")
        operation = input().lower()
        if operation == "u":
            hwtracker.displayAssignments()
        elif operation == "c":
            hwtracker.displayCourseAssignments()
        elif operation == "d":
            hwtracker.displayDueDateAssignments()
        else:
            print("Invalid format.")
            
    def switch_frame(diff_frames, frame):
        for f in diff_frames:
            if f != frame:
                f.pack_forget()
            else:
                f.pack(fill="both", expand=True)