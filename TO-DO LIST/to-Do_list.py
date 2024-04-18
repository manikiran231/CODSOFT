import tkinter as tk
from tkinter import messagebox

class TodoListGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List of Manikiran")
        self.root.geometry("600x400")  # Set window size to medium size
        self.root.configure(bg="#7D85B1")  # Set background color to berry blue
        
        self.tasks = []

        heading_label = tk.Label(self.root, text="To-Do List of Manikiran", font=("Arial", 20, "bold"), bg="#7D85B1", fg="white")  # Set heading label
        heading_label.pack(pady=10)

        self.task_field = tk.Entry(self.root, width=50, font=("Arial", 14))  # Increase size of text fields
        self.task_field.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#7D85B1")  # Frame for buttons
        button_frame.pack()

        add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, bg="#90EE90", font=("Arial", 14))  # Light green color
        add_button.grid(row=0, column=0, padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="#90EE90", font=("Arial", 14))  # Light green color
        delete_button.grid(row=0, column=1, padx=5, pady=5)

        delete_all_button = tk.Button(self.root, text="Delete All Tasks", command=self.delete_all_tasks, bg="#90EE90", font=("Arial", 14))  # Light green color
        delete_all_button.pack(pady=5)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="#90EE90", font=("Arial", 14))  # Light green color
        exit_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10, font=("Arial", 12, "bold"))  # Increase size of listbox and set text to bold
        self.task_listbox.pack(pady=10)

        self.root.mainloop()

    def add_task(self):
        task_string = self.task_field.get()  
        if len(task_string) == 0:  
            messagebox.showinfo('Error', 'Field is Empty.')  
        else:    
            self.tasks.append(task_string)   
            self.task_listbox.insert(tk.END, task_string)   
            self.task_field.delete(0, 'end')  

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
        else:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')  

    def delete_all_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = []


def main():
    todo_list_gui = TodoListGUI()


if __name__ == "__main__":
    main()
