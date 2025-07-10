import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x550")
root.resizable(False, False)

# Store tasks as a list of dicts: {'text': 'Task', 'done': False}
tasks = []

# Function to update the listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        display_text = f"✔️ {task['text']}" if task['done'] else task['text']
        listbox.insert(tk.END, display_text)

# Add a task
def add_task():
    task_text = entry.get().strip()
    if task_text:
        tasks.append({'text': task_text, 'done': False})
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        del tasks[selected]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        tasks.clear()
        update_listbox()

# Mark selected task as done
def mark_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]['done'] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# UI Elements
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill=tk.X)

add_btn = tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), height=15, selectbackground="lightblue")
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

done_btn = tk.Button(root, text="Mark as Done", font=("Arial", 12), command=mark_done)
done_btn.pack(pady=5)

del_btn = tk.Button(root, text="Delete Selected", font=("Arial", 12), command=delete_task)
del_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All", font=("Arial", 12), command=clear_tasks)
clear_btn.pack(pady=5)

# Start app
root.mainloop()
