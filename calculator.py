import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget["text"]

    if text == "=":
        try:
            result = str(eval(expression))
            calc_history.append(expression + " = " + result)
            equation.set(result)
            expression = result  # Allow further calculation
        except Exception as e:
            equation.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        equation.set("")
    elif text == "H":
        show_history()
    else:
        expression += text
        equation.set(expression)

def show_history():
    if not calc_history:
        messagebox.showinfo("History", "No past calculations to show.")
    else:
        history_text = "\n".join(calc_history[-10:])  # Show last 10
        messagebox.showinfo("Calculation History", history_text)

# Initialize GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.configure(bg="black")

expression = ""
calc_history = []

equation = tk.StringVar()

entry = tk.Entry(root, textvar=equation, font="Arial 30", bd=10, insertwidth=2, width=14,
                 bg="black", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout (with History button)
buttons = [
    ["C", "H", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

symbol_to_operator = {"÷": "/", "×": "*", "%": "%"}

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        display_text = btn_text
        if btn_text in symbol_to_operator:
            btn_text = symbol_to_operator[btn_text]

        button = tk.Button(root, text=display_text, font="Arial 20", padx=20, pady=20,
                           bg="#ff9500" if display_text in "+-*/=%÷×" else "#333",
                           fg="white" if display_text != "C" else "black")
        button.grid(row=i+1, column=j, sticky="nsew")
        button.bind("<Button-1>", click)

root.mainloop()
