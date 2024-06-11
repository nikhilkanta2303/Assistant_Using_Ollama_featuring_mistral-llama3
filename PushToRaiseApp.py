import tkinter as tk
from main import phoenixask, interrupt  # Assuming these functions exist

# Minimalistic Color Palette
BACKGROUND_COLOR = "#f2f2f2"  # Light Gray
TEXT_COLOR = "#333333"  # Dark Gray
BUTTON_COLOR = "#4CAF50"  # Green (accent)

# Create the main window
root = tk.Tk()
root.title("Pheonix AI")  # Set the title of the window
root.configure(bg=BACKGROUND_COLOR)  # Set background color

# Create a frame for centering elements
frame = tk.Frame(root, bg=BACKGROUND_COLOR)
frame.pack(expand=True)

# Title Label
title_label = tk.Label(frame, 
                       text="Phoenix AI", 
                       font=("Helvetica", 24),
                       fg=TEXT_COLOR,
                       bg=BACKGROUND_COLOR)
title_label.pack(pady=20)  # Add padding

# Create a button
button = tk.Button(frame, text="Raise", command=phoenixask,
                   fg=TEXT_COLOR, bg=BUTTON_COLOR,
                   font=("Helvetica", 14), relief="flat", highlightthickness=0)
# Adjust size (optional)
button.config(width=20, height=2)
button.pack(pady=30,padx=30)  # Add padding around the button

# Start the main event loop to display the window
root.mainloop()
