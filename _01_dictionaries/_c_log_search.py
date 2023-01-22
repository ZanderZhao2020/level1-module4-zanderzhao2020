"""
Log Search using a Id-Name Dictionary
"""

# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.
#
#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.

#  Button 2: Search by ID
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
#
# Button 3: View List
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
#
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.
#
import tkinter as tk
from tkinter import simpledialog, messagebox

class LogSearch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.add = tk.Button(text="Add", command=self.onadd)
        self.add.place(relx=0.1, rely=0.1, relwidth=0.15, relheight=0.8)
        self.search = tk.Button(text="Search", command=self.onsearch)
        self.search.place(relx=0.3, rely=0.1, relwidth=0.15, relheight=0.8)
        self.view = tk.Button(text="View", command=self.onview)
        self.view.place(relx=0.5, rely=0.1, relwidth=0.15, relheight=0.8)
        self.remove = tk.Button(text="Remove", command=self.onremove)
        self.remove.place(relx=0.7, rely=0.1, relwidth=0.15, relheight=0.8)
        self.dict = {}
    def onadd(self):
        id = simpledialog.askstring("Prompt", "Enter an ID number")
        name = simpledialog.askstring("Prompt", "Enter a name")
        self.dict[id] = name
    def onsearch(self):
        id = simpledialog.askstring("Prompt", "Enter an ID number")
        if id in self.dict:
            messagebox.showinfo("Message", self.dict[id])
        else:
            messagebox.showerror("Error", "That ID does not exist")
    def onview(self):
        message = ""
        for id, name in self.dict.items():
            message += "ID: " + id + "  Name: " + name
        messagebox.showinfo("Message", message)
    def onremove(self):
        id = simpledialog.askstring("Prompt", "Enter an ID number")
        if id in self.dict:
            self.dict.pop(id)
        else:
            messagebox.showerror("Error", "That ID does not exist")
        pass
if __name__ == "__main__":
    app = LogSearch()
    app.title("LogSearch")
    app.geometry("750x50")
    app.mainloop()