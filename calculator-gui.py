import tkinter as tk

# Function to append numbers and operators to the input field
def add_to_input(value):
    current = entry_input.get()
    entry_input.delete(0, tk.END)
    entry_input.insert(tk.END, current + value)

# Function to clear the input field
def clear_input():
    entry_input.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        expression = entry_input.get()
        result = eval(expression)
        entry_input.delete(0, tk.END)
        entry_input.insert(tk.END, str(result))
    except Exception as e:
        entry_input.delete(0, tk.END)
        entry_input.insert(tk.END, "Error")

# Create the GUI window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="#F0F0F0")
# window.geometry("600x400")  # Set the width and height as desired



# Styling
button_bg = "#E0E0E0"
button_active_bg = "#D0D0D0"
button_fg = "#000000"
button_font = ("Arial", 25, "bold")

# Create the input field
entry_input = tk.Entry(window, width=30, justify=tk.RIGHT, font=("Arial", 25), bd=2)
entry_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
button_1 = tk.Button(window, text="1", command=lambda: add_to_input("1"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_1.grid(row=1, column=0, padx=5, pady=5)
# Add the rest of the number buttons...
button_2 = tk.Button(window, text="2", command=lambda: add_to_input("2"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_2.grid(row=1, column=1, padx=5, pady=5)
button_3 = tk.Button(window, text="3", command=lambda: add_to_input("3"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_3.grid(row=1, column=2, padx=5, pady=5)
button_4 = tk.Button(window, text="4", command=lambda: add_to_input("4"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5 = tk.Button(window, text="5", command=lambda: add_to_input("5"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6 = tk.Button(window, text="6", command=lambda: add_to_input("6"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_7 = tk.Button(window, text="7", command=lambda: add_to_input("7"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_7.grid(row=3, column=0, padx=5, pady=5)
button_8 = tk.Button(window, text="8", command=lambda: add_to_input("8"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_8.grid(row=3, column=1, padx=5, pady=5)
button_9 = tk.Button(window, text="9", command=lambda: add_to_input("9"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_9.grid(row=3, column=2, padx=5, pady=5)
button_0 = tk.Button(window, text="0", command=lambda: add_to_input("0"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_0.grid(row=4, column=0, padx=5, pady=5)

# Create operator buttons
button_plus = tk.Button(window, text="+", command=lambda: add_to_input("+"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_plus.grid(row=1, column=3, padx=5, pady=5)
# Add the rest of the operator buttons...
button_minus = tk.Button(window, text="-", command=lambda: add_to_input("-"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_minus.grid(row=2, column=3, padx=5, pady=5)
button_multiply = tk.Button(window, text="*", command=lambda: add_to_input("*"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide = tk.Button(window, text="/", command=lambda: add_to_input("/"), bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_divide.grid(row=4, column=3, padx=5, pady=5)

# Create equal sign button
button_equal = tk.Button(window, text="=", command=calculate, bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_equal.grid(row=4, column=2, padx=5, pady=5)

# Create clear button
button_clear = tk.Button(window, text="Clear", command=clear_input, bg=button_bg, activebackground=button_active_bg, fg=button_fg, font=button_font)
button_clear.grid(row=4, column=1, padx=5, pady=5)

# Customize the layout and appearance as desired

# Start the main GUI loop
window.mainloop()
