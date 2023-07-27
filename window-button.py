import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
window = tk.Tk()
window.title("Python Window with Button")

# Create a button widget
button = tk.Button(window, text="Click Me!", command=button_click)
button.pack(pady=20)

# Start the main event loop
window.mainloop()
