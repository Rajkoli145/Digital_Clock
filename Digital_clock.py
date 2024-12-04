import tkinter as tk
from time import strftime

# Initialize the time format
is_24_hour = False

# Function to update the time
def update_time():
    if is_24_hour:
        current_time = strftime('%H:%M:%S %p')  # 24-hour format
    else:
        current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    label.config(text=current_time)  # Update label text with current time
    label.after(1000, update_time)  # Refresh every 1 second

# Function to toggle between 12-hour and 24-hour formats
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour  # Switch the format
    button.config(text="Switch to 24-hour" if not is_24_hour else "Switch to 12-hour")  # Update button text

# Initialize the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x300")  # Set window size
root.configure(bg='white')  # Set background color

# Create and configure the clock label
label = tk.Label(root, font=('Helvetica', 48, 'bold'), bg='black', fg='cyan')
label.pack(expand=True)  # Center the label in the window

# Create the toggle button
button = tk.Button(
    root, 
    text="Switch to 24-hour", 
    font=('Helvetica', 14), 
    command=toggle_format, 
    bg='Black', 
    fg='Black'
)
button.pack(pady=20)  # Add some padding around the button

# Start the clock
update_time()

# Run the application
root.mainloop()