import tkinter as tk
from FunctionCalls import FunctionCalls
from HomeworkTracker import HomeworkTracker
from HomeworkTracker import Assignment
from InOutFileCreation import FileGeneration

# Define the root for the Homework Tracker GUI.
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Homework Tracker")

# Set the application icon
icon_path = "book_icon.ico"
root.iconbitmap(default=icon_path)

# Define different fonts
header_font = ("Courier New", 24, "bold")
button_font = ("Courier New", 16)

# Background colors
pink = "#ffb3b3"

# Button sizes
button_width = 12
button_height = 1

# Default homework tracker setup
csv_file = "homework_data.csv"
hwtracker = FunctionCalls.on_startup(csv_file)

# Define the different frames.
# Main Frame. Gives options for different features of Homework Tracker.
main_frame = tk.Frame(root, bg=pink)
main_frame.pack(fill="both", expand=True)

welcome = tk.Label(main_frame, text="Welcome to Your Homework Tracker!", font=header_font, bg=pink)
welcome.pack(side=tk.TOP, pady=10)

# Give main frame buttons pointing to each subframe.
# Open File Button
file_open_button = tk.Button(main_frame, text="Open File", width=button_width, height=button_height, command=lambda: switch_frame(open_frame))
file_open_button.pack(side=tk.TOP, pady=10)

# Display Button
display_button = tk.Button(main_frame, text="Display", width=button_width, height=button_height, command=lambda: switch_frame(disp_frame))
display_button.pack(side=tk.TOP, pady=10)

# Add Button
add_button = tk.Button(main_frame, text="Add", width=button_width, height=button_height, command=lambda: switch_frame(frame_add))
add_button.pack(side=tk.TOP, pady=10)

# Remove Button
remove_button = tk.Button(main_frame, text="Remove", width=button_width, height=button_height, command=lambda: switch_frame(rm_frame))
remove_button.pack(side=tk.TOP, pady=10)

# Save Button
save_button = tk.Button(main_frame, text="Save", width=button_width, height=button_height, command=lambda: export_pop())
save_button.pack(side=tk.TOP, pady=10)

# Quit Button
quit_button = tk.Button(main_frame, text="Quit", width=button_width, height=button_height, command=lambda: switch_frame(quit_frame))
quit_button.pack(side=tk.TOP, pady=10)

# 1) Open File Frame
#       Need button that writes the file, and returns to main frame    
open_frame = tk.Frame(root, bg=pink)
open_text = tk.Label(open_frame, text="Enter CSV File Name: ", font=header_font, bg=pink)
open_text.pack(side=tk.TOP, pady=10)
entry = tk.Entry(open_frame, width=30)
entry.pack(side=tk.TOP, pady=10)

# Back button and home buttom
bb4 = tk.Button(open_frame, text="Back", width=button_width, height=button_height, command=lambda: switch_frame(main_frame))
bb4.pack(side=tk.BOTTOM, pady=10)
entry_accept = tk.Button(open_frame, text="Submit", command=lambda: open_file_input())
entry_accept.pack(side=tk.TOP, pady=10)

# 2) Display Assignment Frame
#   a) Unordered 
#       Need button that displays unordered results with button to return to main frame after.
#   b) Ordered by class 
#       Need button that displays results by class with button to return to main frame after.
#   c) Ordered by due date
#       Need button that displays results by due date with button to return to main frame after.
disp_frame = tk.Frame(root, bg=pink)
# Prompt for type of arrangement.
disp_prompt = tk.Label(disp_frame, text="How should the assignments be ordered?", font=header_font, bg=pink)
disp_prompt.pack(side=tk.TOP, pady=10)

# Three buttons for unorganized, by class, and by due date display.
unordered = tk.Button(disp_frame, text="Unordered", width=button_width, height=button_height, command=lambda: disp_unord())
unordered.pack(side=tk.TOP, pady=10)

by_class = tk.Button(disp_frame, text="By Class", width=button_width, height=button_height, command=lambda: disp_class())
by_class.pack(side=tk.TOP, pady=10)

by_due_date_frame = tk.Button(disp_frame, text="By Due Date", width=button_width, height=button_height, command=lambda: disp_due())
by_due_date_frame.pack(side=tk.TOP, pady=10)

# Back button
bb5 = tk.Button(disp_frame, text="Back", width=button_width, height=button_height, command=lambda: switch_frame(main_frame))
bb5.pack(side=tk.BOTTOM, pady=10)

# Unorganized Frame
unorganized_frame = tk.Frame(root, bg=pink)
unorg_label = tk.Label(unorganized_frame, text="Homework Assignments", font=header_font, bg=pink)
unorg_label.pack(side=tk.TOP, pady=10)
header_label = tk.Label(unorganized_frame, text="Name\tCourse\tDue Date\tDescription")
header_label.pack(side=tk.TOP, pady=10)
text_widgit = tk.Text(unorganized_frame, wrap=tk.NONE)
text_widgit.pack()

# Add back and home button
bb2 = tk.Button(unorganized_frame, text="Back", width=button_width, height=button_height, command=lambda: switch_frame(disp_frame))
bb2.pack(side=tk.BOTTOM, pady=10)
home_button = tk.Button(unorganized_frame, text="Home", width=button_width, height=button_height, command=lambda: switch_frame(main_frame))
home_button.pack(side=tk.BOTTOM, pady=10)

# By Class Frame
by_class_frame = tk.Frame(root, bg=pink)
class_label = tk.Label(by_class_frame, text="Homework Assignments", font=header_font, bg=pink)
class_label.pack(side=tk.TOP, pady=10)
head_label = tk.Label(by_class_frame, text="Name\tCourse\tDue Date\tDescription")
head_label.pack(side=tk.TOP, pady=10)
class_widgit = tk.Text(by_class_frame, wrap=tk.NONE)
class_widgit.pack()

# Add back and home button
back_button = tk.Button(by_class_frame, text="Back", width=button_width, height=button_height, command=lambda: switch_frame(disp_frame))
back_button.pack(side=tk.BOTTOM, pady=10)
home_button = tk.Button(by_class_frame, text="Home", width=button_width, height=button_height, command=lambda: switch_frame(main_frame))
home_button.pack(side=tk.BOTTOM, pady=10)

# By Due Date Frame
by_due_date_frame = tk.Frame(root, bg=pink)
due_label = tk.Label(by_due_date_frame, text="Homework Assignments", font=header_font, bg=pink)
due_label.pack(side=tk.TOP, pady=10)
head_label = tk.Label(by_due_date_frame, text="Name\tCourse\tDue Date\tDescription")
head_label.pack(side=tk.TOP, pady=10)
due_widgit = tk.Text(by_due_date_frame, wrap=tk.NONE)
due_widgit.pack()

# Back and home button
bb1 = tk.Button(by_due_date_frame, text="Back", width=button_width, height=button_height, command=lambda: switch_frame(disp_frame))
bb1.pack(side=tk.BOTTOM, pady=10)
hb1 = tk.Button(by_due_date_frame, text="Home", width=button_width, height=button_height, command=lambda: switch_frame(main_frame))
hb1.pack(side=tk.BOTTOM, pady=10)

# 3) Add Assignment Frame
#Need button that adds assignment and returns to main frame after.
frame_add = tk.Frame(root, bg=pink)
name_l = tk.Label(frame_add, text="Name:", font=button_font, bg=pink)
name_l.pack(side=tk.TOP, pady=10)
name_entered = tk.Entry(frame_add, width=30)
name_entered.pack(side=tk.TOP, pady=10)

course_l = tk.Label(frame_add, text="Course:", font=button_font, bg=pink)
course_l.pack(side=tk.TOP, pady=10)
course_entered = tk.Entry(frame_add, width=30)
course_entered.pack(side=tk.TOP, pady=10)

dd_l = tk.Label(frame_add, text="Due Date (MM/DD):", font=button_font, bg=pink)
dd_l.pack(side=tk.TOP, pady=10)
due_date_entered = tk.Entry(frame_add, width=30)
due_date_entered.pack(side=tk.TOP, pady=10)

desc_l = tk.Label(frame_add, text="Description", font=button_font, bg=pink)
desc_l.pack(side=tk.TOP, pady=10)
desc_entered = tk.Entry(frame_add, width=30)
desc_entered.pack(side=tk.TOP, pady=10)

# Back and submit button
bb3 = tk.Button(frame_add, text="Back", width=button_width, height=button_height, command=lambda: switch_frame(main_frame))
bb3.pack(side=tk.BOTTOM, pady=10)
submit_data = tk.Button(frame_add, text="Submit", width=button_width, height=button_height, command=lambda: adding())
submit_data.pack(side=tk.BOTTOM, pady=10)

# 4) Remove Assignment Frame
#       Need button that removes assignment and returns to main frame after.
rm_frame = tk.Frame(root, bg=pink)
rm_prompt = tk.Label(rm_frame, text="Enter the name of the assignment", font=header_font, bg=pink)
rm_prompt.pack(side=tk.TOP, pady=10)
text_enter = tk.Entry(rm_frame, width=30)
text_enter.pack(side=tk.TOP, pady=10)

# Back and submit button
bb4 = tk.Button(rm_frame, text="Back", width=button_width, height=button_height, command=lambda: switch_frame(main_frame))
bb4.pack(side=tk.BOTTOM, pady=10)
sub_but = tk.Button(rm_frame, text="Submit", width=button_width, height=button_height, command=lambda: removing())
sub_but.pack(side=tk.BOTTOM, pady=10)

# 5) Quit HomeworkTracker Frame
#       Need button that exits the HomeworkTracker.
quit_frame = tk.Frame(root, bg=pink)
quit_l = tk.Label(quit_frame, text="Do you wish to save before exiting?", font=header_font, bg=pink)
quit_l.pack(side=tk.TOP, pady=10)

save_but = tk.Button(quit_frame, text="Save and Quit", command=lambda: save_and_quit())
save_but.pack(side=tk.TOP, pady=10)
quit_but = tk.Button(quit_frame, text="Quit without Saving", command=lambda: close())
quit_but.pack(side=tk.TOP, pady=10)

# Displays unordered assignments.
def disp_unord():
    switch_frame(unorganized_frame)
    text_widgit.delete('1.0', tk.END)
    
    for item in hwtracker.assignments:
        line = "" + item.get_name() + "\t\t\t" + item.get_course() + "\t\t\t" + item.get_due_date() + "\t\t\t" + item.get_description()
        text_widgit.insert(tk.END, line + "\n")

# Displays assignments by class.
def disp_class():
    switch_frame(by_class_frame)
    class_widgit.delete('1.0', tk.END)
    
    by_class = hwtracker.by_class_order()
    for item in by_class:
        line = "" + item.get_name() + "\t\t\t" + item.get_course() + "\t\t\t" + item.get_due_date() + "\t\t\t" + item.get_description()
        class_widgit.insert(tk.END, line + "\n")
        
def disp_due():
    # Add items to the screen
    switch_frame(by_due_date_frame)
    due_widgit.delete('1.0', tk.END)
    
    by_due = hwtracker.by_due_order()
    for item in by_due:
        line = "" + item.get_name() + "\t\t\t" + item.get_course() + "\t\t\t" + item.get_due_date() + "\t\t\t" + item.get_description()
        due_widgit.insert(tk.END, line + "\n")

# Function to open file.
def open_file_input():
    csv_file = entry.get()
    entry.delete(0, tk.END)
    if (csv_file[-4:-1:1] != ".csv"):
        csv_file = csv_file + ".csv"
    popup = tk.Toplevel(root, bg=pink)
    popup.geometry("320x120")
    popup.title("Opening CSV...")
    try:
        hwtracker = FileGeneration.read_file(csv_file)
        test_text = f"File {csv_file} succesfully opened."
    except:
        test_text = f"File {csv_file} not found."
    pop_label = tk.Label(popup, text=test_text, bg=pink)
    pop_label.pack(padx=20, pady=20)
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(padx=20, pady=10)
    switch_frame(main_frame)
    
def adding():
    course = course_entered.get()
    due_date = due_date_entered.get()
    description = desc_entered.get()
    name = name_entered.get()
    clear_entry()
    new_assign = Assignment(name, course, due_date, description)
    hwtracker.addAssignment(new_assign)
    switch_frame(main_frame)
    
def removing():
    ass_n = text_enter.get()
    text_enter.delete(0, tk.END)
    hwtracker.removeAssignment(ass_n)
    switch_frame(main_frame)
    
def clear_entry():
    course_entered.delete(0, tk.END)
    due_date_entered.delete(0, tk.END)
    desc_entered.delete(0, tk.END)
    name_entered.delete(0, tk.END)
    
def export_pop():
    popup = tk.Toplevel(root, bg=pink)
    popup.geometry("160x120")
    popup.title("Exporting Data...")
    try:
        FileGeneration.write_file(hwtracker, csv_file)
        exp_test = "File succesfully written."
    except:
        exp_test = "Error writing the file. I am bad a coding, sorry."
    pop_label = tk.Label(popup, text=exp_test, bg=pink)
    pop_label.pack(padx=20, pady=20)
    
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(padx=20, pady=10)
    
def save_and_quit():
    popup = tk.Toplevel(root, bg=pink)
    popup.title("Exporting Data...")
    try:
        FileGeneration.write_file(hwtracker, csv_file)
        exp_test = "File succesfully written."
    except:
        exp_test = "Error writing the file. I am bad a coding, sorry."
    pop_label = tk.Label(popup, text=exp_test, bg=pink)
    pop_label.pack(padx=20, pady=20)
    
    close_button = tk.Button(popup, text="Quit", command=close)
    close_button.pack(padx=20, pady=10)

def close():
    root.destroy()

# Function to hide frames       
def switch_frame(frame):
    main_frame.pack_forget()
    open_frame.pack_forget()
    disp_frame.pack_forget()
    unorganized_frame.pack_forget()
    by_class_frame.pack_forget()
    by_due_date_frame.pack_forget()
    frame_add.pack_forget()
    rm_frame.pack_forget()
    quit_frame.pack_forget()
    frame.pack(fill="both", expand=True)
    
# Allow for user interaction.
root.mainloop()