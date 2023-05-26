import tkinter as tk

def execute_command():
    command = input_entry.get()
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, '$ ' + command + '\n')
    # Add your command execution logic here
    # You can run the command using subprocess or any other method
    output_text.insert(tk.END, 'Command executed: ' + command + '\n')
    output_text.config(state=tk.DISABLED)
    input_entry.delete(0, tk.END)

# Create the main application window
window = tk.Tk()
window.title("inCollege - Job Prospecting for Students")

# Create the input entry field
input_entry = tk.Entry(window)
input_entry.pack(pady=10)

# Create the output text area
output_text = tk.Text(window, height=50, width=150)
output_text.config(state=tk.DISABLED)
output_text.pack()

# Create the execute button
execute_button = tk.Button(window, text="Execute", command=execute_command)
execute_button.pack(pady=10)

# Start the GUI event
window.mainloop()
