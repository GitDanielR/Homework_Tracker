import csv
from HomeworkTracker import HomeworkTracker
from HomeworkTracker import Assignment

csv_file = "homework_data.csv"

# Reads and writes CSV files to store the HomeworkTracker and retrieve it.
class FileGeneration:
    
    # Writes the CSV file to store the homework assignments.
    # Input: hwtracker - HomeworkTracker object with assignments.
    # Input: csv_file - output file name.
    # Output: None.
    def write_file(hwtracker, csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header to the CSV file.
            head = ["Name", "Course", "Due Date", "Description"]
            writer.writerow(head)
            # Write each assignment in the HomeworkTracker to the CSV.
            for item in hwtracker.getAssignmentList():
                n = item.get_name()
                c = item.get_course()
                d = item.get_due_date()
                de = item.get_description()
                items = [n, c, d, de]
                writer.writerow(items)
        print(f"CSV file {csv_file} updated.")
        
    # Reads the CSV file to store the homework assignments in a HomeworkTracker object.
    # Input: csv_file - input file name.
    # Output: hwtracker - HomeworkTracker object with assignments.
    def read_file(csv_file) -> HomeworkTracker:
        hwt = HomeworkTracker()
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            # Skip header
            next(reader)
            # Read rows and add assignment objects to the HomeworkTracker.
            for row in reader:
                assign = Assignment(row[0], row[1], row[2], row[3])
                hwt.addAssignment(assign)
        return hwt