import tkinter as tk

expression = ""
BG = "#1a1a2e"
BTN = "#1a2540"
RED = "#e94560"
WHITE = "#ffffff"
GRAY = "#555555"

def press(btn):
    global expression

    if btn == "C":
        expression = ""
        display.config(text="0")
        expr_label.config(text="")

    elif btn == "⌫":
        expression = expression[:-1] 
        display.config(text=expression or "0")
        expr_label.config(text=expression)

    elif btn == "=":
        try:
            result = eval(expression)
            history.append(expression + " = " + str(result))  
            expr_label.config(text=expression + " =")
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            display.config(text=str(result))
            expression = str(result)
        except ZeroDivisionError:
            display.config(text="Ділення на 0!")
            expression = ""
        except:
            display.config(text="Помилка")
            expression = ""

    else:
        expression = expression + btn  
        display.config(text=expression)
        expr_label.config(text=expression)

root = tk.Tk()
root.title("Калькулятор")
root.configure(bg=BG)
root.resizable(False, False)

history = []

expr_label = tk.Label(root, text="", font=("Arial", 11), bg=BG, fg=GRAY, anchor="e")
expr_label.pack(fill="x", padx=15, pady=(15, 0))

display = tk.Label(root, text="0", font=("Arial", 36, "bold"), bg=BG, fg=WHITE, anchor="e")
display.pack(fill="x", padx=15, pady=(0, 15))

buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="],
]

for row in buttons:
    frame = tk.Frame(root, bg=BG)
    frame.pack(fill="x", padx=15, pady=4)

    for btn in row:
        if btn in ["+", "-", "*", "/", "%", "⌫", "C"]:
            color = RED
        elif btn == "=":
            color = "#0f3460"
        else:
            color = BTN

        width = 8 if btn == "0" else 4

        tk.Button(
            frame,
            text=btn,
            font=("Arial", 16),
            bg=color,
            fg=WHITE,
            relief="flat",
            width=width,
            height=2,
            command=lambda b=btn: press(b)
        ).pack(side="left", padx=4)

root.mainloop()
