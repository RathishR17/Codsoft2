#To do List Tkinter
import tkinter as tk
from tkinter import messagebox, simpledialog

def add_list():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Please enter a To-Do list")

def delete_list():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning( "Please select something to delete")

def edit_list():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        current_task = listbox_tasks.get(selected_task_index)

        edited_task = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=current_task)

        if edited_task:
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, edited_task)

    except IndexError:
        messagebox.showwarning("Please select a task to edit")

root = tk.Tk()
root.title("To-Do List by Rathish")
root.geometry('400x300')
root.resizable(0, 0)
root.config(bg="PaleVioletRed")

# Create a frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)

listbox_tasks = tk.Listbox(frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

# Set the scrollbar to the listbox
scrollbar.config(command=listbox_tasks.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

entry_task = tk.Entry(root)
entry_task.pack(pady=10)

button_add = tk.Button(root, text="Add List", command=add_list)
button_add.pack()

button_edit = tk.Button(root, text="Edit List", command=edit_list)
button_edit.pack()

button_delete = tk.Button(root, text="Delete List", command=delete_list)
button_delete.pack()

root.mainloop()