# Assignment class. Defines an assignment.
class Assignment:
    def __init__(self, name, course, due_date, description=None):
        self.name = name
        self.course = course
        self.due_date = due_date
        self.description = description
    
    # Desiplay description of a single assignment
    # Input: None, call method on an object
    # Output: Description
    def displayAssignment(self):
        print(f"Title: {self.name}, Course: {self.course}, Due Date: {self.due_date}, Description: {self.description}")
    
    # Gets the name of an assignment.
    # Input: None.
    # Output: Name.
    def get_name(self):
        return self.name
    
    # Gets the course an assignment is in.
    # Input: None.
    # Output: Course.
    def get_course(self):
        return self.course
    
    # Gets the due date of an assignment.
    # Input: None.
    # Output: Due date.
    def get_due_date(self):
        return self.due_date
    
    # Gets the description of an assignment.
    # Input: None.
    # Output: Description.
    def get_description(self):
        return self.description
    
class HomeworkTracker:
    numItems = 0
    
    # Default state for HomeworkTracker class.
    # Input: None.
    # Output: Initialized, empty list of assignments.
    def __init__(self):
        self.assignments = []
    
    # Get assignment list.
    # Input: None.
    # Output: List of assignments.
    def getAssignmentList(self):
        return self.assignments
    
    # Adds an assignment to the HomeworkTracker.
    # Input: Assignment.
    # Output: Prints if the assignment was invalid.
    def addAssignment(self, assignment):
        if isinstance(assignment, Assignment):
            self.assignments.append(assignment)
            self.numItems += 1
        else:
            print("Invalid assignment operation.")
    
    # Removes an assignment from the HomeworkTracer.
    # Input: Assignment name.
    # Output: None.
    def removeAssignment(self, assignmentName):
        self.assignments = [obj for obj in self.assignments if obj.get_name() != assignmentName]

    # Gets the number of items in the HomeworkTracker
    # Input: None
    # Output: Number of items.
    def getNumItems(self):
        return self.numItems
       
    # Displays assignments.
    # Input: None.
    # Output: Prints the assignments.
    def displayAssignments(self):
           for a in self.assignments:
               a.displayAssignment()
               
    # Displays assignments ordered by class.
    # Input: None.
    # Output: Prints the assignments by class.
    def displayCourseAssignments(self):
           sortedAssignments = sorted(self.assignments, key=Assignment.get_course)
           for a in sortedAssignments:
               a.displayAssignment()
               
    # Creates List ordered by class.
    # Input: None.
    # Output: Prints the assignments by class.
    def by_class_order(self) -> list:
           return sorted(self.assignments, key=Assignment.get_course)
    
    # Creates List ordered by due date.
    # Input: None.
    # Output: Prints the assignments by class.
    def by_due_order(self) -> list:
           return sorted(self.assignments, key=Assignment.get_due_date)

    # Displays assignments ordered by due date.
    # Input: None.
    # Output: Prints the assignments by due date.
    def displayDueDateAssignments(self):
           sortedAssignments = sorted(self.assignments, key=Assignment.get_due_date)
           for a in sortedAssignments:
               a.displayAssignment