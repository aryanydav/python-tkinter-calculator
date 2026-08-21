import tkinter as tk

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")  # Get the text of the button clicked
    if text == "=":  # When "=" is pressed, evaluate the expression
        try:
            result = eval(str(screen.get()))  # Evaluate the expression in the screen
            screen.set(result)  # Display the result
        except Exception:
            screen.set("Error")  # If there's an error, show "Error"
    elif text == "C":  # If "C" is pressed, clear the screen
        screen.set("")
    else:  # For numbers and operators, append them to the current screen
        screen.set(screen.get() + text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")  # Set the window title
root.geometry("300x400")  # Set the window size

# Entry widget for the calculator screen
screen = tk.StringVar()  # A variable to hold the text shown on the screen
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=5, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10)  # Place the entry widget in the window

# Buttons for the calculator
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create and place buttons on the grid
for i in range(4):
    for j in range(4):
        button = tk.Button(button_frame, text=buttons[i*4 + j], font="Arial 15", height=2, width=5)
        button.grid(row=i, column=j, padx=5, pady=5)  # Grid layout for buttons
        button.bind("<Button-1>", click)  # Bind the click event to the button

# Run the main event loop
root.mainloop()
