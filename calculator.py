import tkinter as tk
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 10

def click(event):
    global expression
    text = event.widget["text"]

    if text == "=":
        try:
            eval_expr = expression.replace("×", "*").replace("÷", "/").replace("%", " % ")
            # Safely evaluate using Decimal
            result = str(eval(eval_expr, {"__builtins__": None}, {"Decimal": Decimal}))
            calc_history.append(expression + " = " + result)
            equation.set(result)
            expression = result
        except Exception:
            equation.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        equation.set("")
    elif text == "X":
        expression = expression[:-1]
        equation.set(expression)
    elif text == "H":
        show_history()
    else:
        expression += text
        equation.set(expression)

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("300x400")
    history_window.configure(bg="white")

    if not calc_history:
        tk.Label(history_window, text="No history available.", font="Arial 14", bg="white").pack(pady=10)
    else:
        for record in calc_history:
            tk.Label(history_window, text=record, font="Arial 12", bg="white", anchor='w').pack(fill='x', padx=10)

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x550")
root.configure(bg="black")

expression = ""
calc_history = []

equation = tk.StringVar()

entry = tk.Entry(root, textvar=equation, font="Arial 30", bd=10, insertwidth=2, width=14,
                 bg="black", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=10)

# Buttons layout
buttons = [
    ["C", "X", "H", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0 ", ".", "%", "="]
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        # Special case for 0 to span two columns
        if btn_text == "0":
            button = tk.Button(
                root,
                text=btn_text,
                font="Arial 20",
                padx=30,
                pady=25,
                bg="#333",
                fg="white"
            )
            button.grid(row=i + 1, column=j, columnspan=2, sticky="nsew")
            button.bind("<Button-1>", click)
            continue

        button = tk.Button(
            root,
            text=btn_text,
            font="Arial 20",
            padx=20,
            pady=25,
            bg="#ff9500" if btn_text in "+-×÷=%=" else "#333",
            fg="white" if btn_text not in ("C", "X", "H") else "black"
        )
        button.grid(row=i + 1, column=j, sticky="nsew")
        button.bind("<Button-1>", click)

root.mainloop()
