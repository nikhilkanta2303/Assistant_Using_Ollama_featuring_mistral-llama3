import tkinter as tk
from main import phoenixask, interrupt

# Create the main window
root = tk.Tk()
root.title("Pheonix")  # Set the title of the window

# Create a button
button = tk.Button(root, text="Ask Me", command=phoenixask)

# Set button size (optional)
button.config(width=23, height=3)  # Adjust width and height as needed
# Position the button (optional)
button.pack(padx=60, pady=60)  # Add padding around the button
# Start the main event loop to display the window
root.mainloop()
