import tkinter as tk
from tkinter import messagebox

#List to store conversion
history = [ ]

# Function to convert temperature
def convert_temperature():
    try:
        temperature = float(temperature_entry.get())

        if choice.get() == "C":
            result = (temperature * 9 / 5) + 32
            result_label.config(text=f"Result: {result:.2f} °F")
            history.append(f"{temperature} °C = {result:.2f} °F")
        else:
            result = (temperature - 32) * 5 / 9
            result_label.config(text=f"Result: {result:.2f} °C")
            history.append(f"{temperature} °F = {result:.2f} °C")

    except ValueError:
        messagebox.showerror(
            "Invalid Input", 
            "Please enter a valid temperature."
        )
# Function to save conversion history
def save_history():
    if history:
        with open("temperature_history.txt", "w") as file:
            for item in history:
                file.write(item + "\n")
        messagebox.showinfo("Saved", "Conversion history saved successfully.")
    else:
        messagebox.showinfo("Saved", "No conversion history to save.")




# Function to show conversion history
def show_history():
    if history:
        messagebox.showinfo("Conversion History", "\n".join(history))
    else:
        messagebox.showinfo("Conversion History", "No conversions yet.")

#Create main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("450x550")

# Heading
heading = tk.Label(window, text="Temperature Converter", font=("Arial", 20, "bold"))
heading.pack(pady=25)

# Temperature input
label = tk.Label(window, text="Enter Temperature:")
label.pack(pady=5)

temperature_entry = tk.Entry(window, width=20)
temperature_entry.pack(pady=5)

# Conversion choice
choice = tk.StringVar(value="C")

celsius_radio = tk.Radiobutton(
    window,
    text="Celsius to Fahrenheit",
    variable=choice,
    value="C"
)
celsius_radio.pack(pady=5)

fahrenheit_radio = tk.Radiobutton(
    window,
    text="Fahrenheit to Celsius",
    variable=choice,
    value="F"
)
fahrenheit_radio.pack(pady=5)

# Convert button
convert_button = tk.Button(
    window,
    text="Convert",
    command=convert_temperature
)
convert_button.pack(pady=20)

#History button
history_button = tk.Button(
    window,
    text="View History",
    command=show_history
)
history_button.pack(pady=10)

# Save history button
save_button = tk.Button(
    window,
    text="Save History",
    command=save_history
)
save_button.pack(pady=10)

# Result
result_label = tk.Label(window, text="Result:", font=("Arial", 12))
result_label.pack(pady=10)

# Start the application
window.mainloop()
