# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Import libraries and methods

from tkinter import *
import tkinter as tk
from tkinter import ttk
import time


# The class ToDoList
class ToDoList(Tk):
    # All classes have a function called __init__(), which is always executed when the class is being initiated.
    # Use the __init__() function to assign values to object properties, or other operations
    # that are necessary to do when the object is being created:
    def __init__(self):
        # The super() function makes it so that the ToDoList class inherits
        # the methods and properties from the Tk class of tkinter
        super().__init__()

# The function on_scroll() controls the visible parts of the listboxes.
# Information/data/variables generated from using the scrollbar associated with the listbox is passed into the
# on_scroll function. The on_scroll function in turn passes on these variables to the yview method of the listboxes.
# The purpose of this function is to update both the listboxes with the information from the single scrollbar
# because they are separate.
# Without this function, it would be difficult to update both listboxes at the same time when using/interacting with
# the single scrollbar.


def on_scroll(*args):

    # print(f"Scrollbar moved, args: {args}")
    listbox.yview(*args)
    listbox1.yview(*args)

# Defining a function that will get the task and insert it in the listbox through the <return> (Enter) keypress.
# It also gets the index of a task to be removed.


def insert_e(arg):
    # print({*args})
    task = task_var.get()
    remove = remove_var.get()

    # This section updates the time displayed
    current_time = time.strftime("%A %H:%M local time")
    label3 = Label(frame1, text=current_time, font=26)
    label3.grid(row=2, column=0, pady=1, padx=1)

    # Check if a task is to be inserted
    if task:
        # print(task)

        # print(listbox.size())
        listbox.insert("end", task)
        index = listbox.size()
        listbox1.insert(listbox.size(), index)
        # print(listbox.size())
        listbox['yscrollcommand'] = scrollbar.set
        # listbox1['yscrollcommand'] = scrollbar.set
        # This line clears up the entry field for submitting a task
        task_var.set("")

    # Check if a task is to be deleted from the to-do list
    if remove:
        # print(remove)
        # Variable 'slot' is created to store the value in 'remove',
        # cast as an int instead of a string, then subtract 1.
        # This makes it more convenient for the user to enter indexes/entries from
        # 1 and up to delete, instead of starting at 0.
        slot = int(remove) - 1
        listbox.delete(slot)
        # Rearrange the leftover indexes of the tasks left in the list. Use a counter and delete all index entries,
        # and afterwards repopulate each index in a while loop with the correct corresponding numbering
        counter = 1
        listbox1.delete(0, END)
        while counter <= listbox.size():
            # listbox1.delete(counter)
            text = str(counter)
            listbox1.insert(counter, text)
            counter += 1
        # This line clears up the entry field for removing a task
        remove_var.set("")

    # This line clears up the string variable entered
    # task_var.set("")
    # remove_var.set("")


# Defining a function that will get the task and insert it in the listbox through the submit button.
# It also gets the index of a task to be removed.
def insert():
    task = task_var.get()
    remove = remove_var.get()

    # This section updates the time displayed
    current_time = time.strftime("%A %H:%M local time")
    label3 = Label(frame1, text=current_time, font=26)
    label3.grid(row=2, column=0, pady=1, padx=1)

    # Check if a task is to be inserted
    if task:
        # print(task)
        listbox.grid(row=0, column=1)
        listbox1.grid(row=0, column=0)
        # print(listbox.size())
        listbox.insert(listbox.size() + 1, task)
        index = listbox.size()
        listbox1.insert(listbox.size(), index)
        # print(listbox.size())
        # This line clears up the entry field for submitting a task
        task_var.set("")

    # Check if a task is to be deleted from the to-do list
    if remove:
        # print(remove)
        # Variable 'slot' is created to store the value in 'remove',
        # cast as an int instead of a string, then subtract 1.
        # This makes it more convenient for the user to enter indexes from
        # 1 and up, instead of starting at 0.
        slot = int(remove) - 1
        listbox.delete(slot)
        # Rearrange the leftover indexes of the tasks left in the list. Use a counter and delete all index entries,
        # and afterwards repopulate each index in a while loop with the correct corresponding numbering
        counter = 1
        listbox1.delete(0, END)
        while counter <= listbox.size():
            text = str(counter)
            listbox1.insert(counter, text)
            counter += 1
        # This line clears up the entry field for removing a task
        remove_var.set("")

    # This line clears up the string variable entered
    # task_var.set("")
    # remove_var.set("")

# Defines a function for enabling the user to use the keyboard button Delete to remove entries highlighted as a
# result of a cursor selection in the listbox.


def del_task(event):

    # The actual content/variables/information passed to this function is not used in practice. Instead, the
    # function just use the methods of the listbox to carry out deletion of the entry in question.
    print(event)
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
        listbox1.delete(selected_index)

        # Repopulate the listbox1 widget to correctly correspond with the number of entries in the listbox widget
        counter = 1
        listbox1.delete(0, END)
        while counter <= listbox.size():
            text = str(counter)
            listbox1.insert(counter, text)
            counter += 1

# The main part of the program!


if __name__ == '__main__':

    # Make a clock
    # clock = time.localtime()
    # time_var = tk.StringVar()
    current = time.strftime("%A %H:%M local time")

    print(current)

    # Variable 'app' is created as an object of the ToDoList() class
    app = ToDoList()

    # the geometry function determines the size of the window containing the ToDoList object
    app.geometry("600x500")

    # Name the title of the window of the object
    app.title('To-Do List')

    # Declare string variables for storing the task and the index of the task to be deleted
    task_var = tk.StringVar()
    remove_var = tk.StringVar()

    # Declare an integer variable for keeping track of the total number of tasks in the list
    # tot_num_tasks = 0
    # print(type(tot_num_tasks))
    # print(tot_num_tasks)

    # Enables resizing of the object app in combination with the Sizegrip widget when you drag the window corner
    app.resizable(True, True)

    # Configures the columns and rows of the app object with the weight making each column or row wider or narrower
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    # Make a grouping container in the form of a frame in top and bottom where the 'sticky' option manipulates
    # the anchoring of the frames relative to app object window
    frame1 = ttk.Frame(app)
    frame1.grid(row=0, column=0, sticky=tk.N)
    frame2 = ttk.Frame(app)
    frame2.grid(row=1, column=0)

    # Make a descriptive label for the entry textbox and the deletion textbox, and place them in frame1 and its grid
    label1 = Label(frame1, text="Enter a task", font=26)
    label1.grid(row=0, column=0, pady=1, padx=1)
    label2 = Label(frame1, text="Remove task number:", font=26)
    label2.grid(row=1, column=0, pady=1, padx=1)
    # Makes a label to store the most recent time stamp. It is also updated when a task is deleted or entered
    label3_init = Label(frame1, text=current, font=26)
    label3_init.grid(row=2, column=0, pady=1, padx=1)

    # Make the entry textbox, the deletion textbox, and a button to both submit and delete a task depending on
    # the current content of the textboxes
    text1 = Entry(frame1, textvariable=task_var, width=40, font="helvetica")
    text2 = Entry(frame1, textvariable=remove_var, width=40, font="helvetica")
    btn1 = Button(frame1, text='Submit', command=insert)

    # Place the textboxes and submit button in frame1
    text1.grid(row=0, column=1, pady=1)
    text2.grid(row=1, column=1, pady=1)
    btn1.grid(row=2, column=1)
    # btn2.grid(row=2, column=2)

    # Bind events to textbox 1 and two. In this case the function insert_e() will be called and process any
    # entered text when the Return key is pressed
    text1.bind("<Return>", insert_e)
    text2.bind("<Return>", insert_e)

    # Use a listbox widget for listing the to-do's
    listbox = Listbox(frame2, height=20,
                      width=50,
                      # yscrollcommand=Scrollbar.set,
                      # bg="black",
                      activestyle='dotbox',
                      font="helvetica",
                      fg="black")

    # Place the listbox in frame2
    listbox.grid(row=0, column=1)


    # Create a scrollbar widget, place it in frame2 and associate it to the listbox containing the tasks
    scrollbar = ttk.Scrollbar(
        frame2,
        orient='vertical',
        # command=listbox.yview
    )
    scrollbar.grid(row=0, column=2, sticky=tk.NS)
    # listbox['yscrollcommand'] = scrollbar.set
    # listbox.configure(yscrollcommand=scrollbar.set)

    # Use another listbox to display the index of entries in the main to do list
    listbox1 = Listbox(frame2, height=20,
                       width=2,
                       # bg="black",
                       activestyle='dotbox',
                       font="helvetica",
                       fg="black")

    listbox1.grid(row=0, column=0)

    # Call a function for when an entry in the listbox is selected.
    listbox.bind('<Delete>', del_task)

    # Configures the scrollbar to be updated according to increase in entries of both listboxes (listbox and listbox1)
    scrollbar.config(command=on_scroll)

    # insert elements by their
    # index and names.

    listbox1.insert(0, "0")
    listbox1.insert(1, "1")
    listbox1.insert(2, "2")
    listbox1.insert(3, "3")
    listbox1.insert(4, "4")
    listbox1.insert(5, "5")
    listbox1.insert(6, "6")
    listbox1.insert(8, "8")
    listbox1.insert(9, "9")
    listbox1.insert(10, "10")
    listbox1.insert(11, "11")
    listbox1.insert(12, "12")
    listbox1.insert(13, "13")
    listbox1.insert(14, "14")
    listbox1.insert(15, "15")
    listbox1.insert(16, "16")
    listbox1.insert(17, "17")
    listbox1.insert(18, "18")
    listbox1.insert(19, "19")
    listbox1.insert(20, "20")
    listbox1.insert(21, "21")

    listbox.insert(0, "0")
    listbox.insert(2, "2")
    listbox.insert(3, "3")
    listbox.insert(4, "4")
    listbox.insert(1, "1")
    listbox.insert(5, "5")
    listbox.insert(6, "6")
    listbox.insert(8, "8")
    listbox.insert(9, "9")
    listbox.insert(10, "10")
    listbox.insert(11, "11")
    listbox.insert(12, "12")
    listbox.insert(13, "13")
    listbox.insert(14, "14")
    listbox.insert(15, "15")
    listbox.insert(16, "16")
    listbox.insert(17, "17")
    listbox.insert(18, "18")
    listbox.insert(19, "19")
    listbox.insert(20, "20")
    listbox.insert(21, "21")


    # Inserting a sizegrip for dynamic adjustment of the application window fewa
    sizegrip = ttk.Sizegrip(app)
    sizegrip.grid(row=2, sticky=tk.E)

    # print(task_var)
    # 'mainLoop' must be called to display the window containing the ToDoList object
    app.mainloop()
