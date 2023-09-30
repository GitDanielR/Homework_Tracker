from FunctionCalls import FunctionCalls
import datetime

from HomeworkTracker import HomeworkTracker

# Welcome information.
print("Welcome to your HomeworkTracker!")
print("Made by: Daniel Reyes")
print(f"Date: {datetime.date.today()}")

# Open default CSV and store in HomeworkTracker object. Need to have this csv_file already made with a header.
csv_file = "homework_data.csv"
hwtracker = FunctionCalls.on_startup(csv_file)

# Loop that allows for user interaction with the HomeworkTracker object.
while True:
    # Get desired operation.
    operation = FunctionCalls.prompt_for_option()
    # Open file operation.
    if operation == "o":
        print("Enter file name: ")
        csv_file = input()
        hwtracker = FunctionCalls.open_file(csv_file)
    # Display assignment operation.
    elif operation == "d":
        FunctionCalls.display_assignments(hwtracker)
    # Add assignment operation.
    elif operation == "a":
        hwtracker = FunctionCalls.add_assignment(hwtracker)
        changed_file = True
    # Remove assignment operation.
    elif operation == "r":
        hwtracker = FunctionCalls.remove_assignment(hwtracker)
        changed_file = True
    # Update CSV operation.
    elif operation == "s":
        FunctionCalls.write_file(hwtracker, csv_file)
        updated_file = True
    # Quit operation.
    elif operation == "q":
        # Check if file changed but changes not written.
        print("Do you wish to quit without saving? (yes/no)")
        ans = input().lower()
        # Exit without saving changes.
        if ans[0] == "y":
            print("CSV file unsaved...")
        # Save changes and exit.
        elif ans[0] == "n":
            FunctionCalls.write_file(hwtracker, csv_file)
        break
    # Invalid input entered.
    else:
        print("Invalid input.\n")
        
print("\nExiting HomeworkTracker!")