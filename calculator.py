import tkinter as tk

# ================================
# ЗМІННІ ТА ТИПИ ДАНИХ
# ================================
# Колір теми (рядки)
BG_COLOR = "#1a1a2e"
BTN_COLOR = "#16213e"
BTN_HOVER = "#0f3460"
ACCENT_COLOR = "#e94560"
TEXT_COLOR = "#ffffff"
DISPLAY_BG = "#0f0f1a"

# Шрифти (кортежі)
FONT_DISPLAY = ("Courier New", 32, "bold")
FONT_BTN = ("Courier New", 18, "bold")
FONT_SMALL = ("Courier New", 12)

# Словник з операціями
OPERATIONS = {
    "+": "додавання",
    "-": "віднімання",
    "*": "множення",
    "/": "ділення",
}

# ================================
# КЛАС КАЛЬКУЛЯТОРА
# ================================
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        # Змінні стану
        self.current_input = ""
        self.expression = ""
        self.last_result = 0
        self.history = []  # Список для зберігання історії

        self.build_ui()

    # ================================
    # ПОБУДОВА ІНТЕРФЕЙСУ
    # ================================
    def build_ui(self):
        # Заголовок
        title_label = tk.Label(
            self.root,
            text="◈ CALC",
            font=("Courier New", 14, "bold"),
            bg=BG_COLOR,
            fg=ACCENT_COLOR,
        )
        title_label.grid(row=0, column=0, columnspan=4, pady=(15, 0))

        # Поле виразу (що вводимо)
        self.expr_label = tk.Label(
            self.root,
            text="",
            font=FONT_SMALL,
            bg=DISPLAY_BG,
            fg="#888888",
            anchor="e",
            width=20,
        )
        self.expr_label.grid(
            row=1, column=0, columnspan=4,
            padx=15, pady=(10, 0), ipady=5, sticky="ew"
        )

        # Головний дисплей
        self.display = tk.Label(
            self.root,
            text="0",
            font=FONT_DISPLAY,
            bg=DISPLAY_BG,
            fg=TEXT_COLOR,
            anchor="e",
            width=12,
            height=2,
        )
        self.display.grid(
            row=2, column=0, columnspan=4,
            padx=15, pady=(0, 15), ipady=10, sticky="ew"
        )

        # ================================
        # СПИСОК КНОПОК (список кортежів)
        # ================================
        buttons = [
            ("C", 3, 0, ACCENT_COLOR),
            ("⌫", 3, 1, BTN_HOVER),
            ("%", 3, 2, BTN_HOVER),
            ("/", 3, 3, ACCENT_COLOR),

            ("7", 4, 0, BTN_COLOR),
            ("8", 4, 1, BTN_COLOR),
            ("9", 4, 2, BTN_COLOR),
            ("*", 4, 3, ACCENT_COLOR),

            ("4", 5, 0, BTN_COLOR),
            ("5", 5, 1, BTN_COLOR),
            ("6", 5, 2, BTN_COLOR),
            ("-", 5, 3, ACCENT_COLOR),

            ("1", 6, 0, BTN_COLOR),
            ("2", 6, 1, BTN_COLOR),
            ("3", 6, 2, BTN_COLOR),
            ("+", 6, 3, ACCENT_COLOR),

            ("±", 7, 0, BTN_COLOR),
            ("0", 7, 1, BTN_COLOR),
            (".", 7, 2, BTN_COLOR),
            ("=", 7, 3, ACCENT_COLOR),
        ]

        # ================================
        # ЦИКЛ — створюємо кнопки
        # ================================
        for text, row, col, color in buttons:
            btn = tk.Button(
                self.root,
                text=text,
                font=FONT_BTN,
                bg=color,
                fg=TEXT_COLOR,
                activebackground=ACCENT_COLOR,
                activeforeground=TEXT_COLOR,
                relief="flat",
                borderwidth=0,
                width=4,
                height=2,
                cursor="hand2",
                command=lambda t=text: self.on_click(t),
            )
            btn.grid(row=row, column=col, padx=6, pady=6)

            # Ефект при наведенні мишки
            btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg=BTN_HOVER if c == BTN_COLOR else c))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))

        # Підпис внизу
        tk.Label(
            self.root,
            text="зроблено на Python + tkinter",
            font=("Courier New", 9),
            bg=BG_COLOR,
            fg="#444444",
        ).grid(row=8, column=0, columnspan=4, pady=(0, 10))

    # ================================
    # ОБРОБКА НАТИСКАНЬ
    # ================================
    def on_click(self, text):
        # Розгалуження — перевіряємо що натиснули
        if text == "C":
            self.clear()

        elif text == "⌫":
            self.backspace()

        elif text == "=":
            self.calculate()

        elif text == "±":
            self.toggle_sign()

        elif text == "%":
            self.percent()

        else:
            self.add_to_input(text)

    # ================================
    # ФУНКЦІЇ КАЛЬКУЛЯТОРА
    # ================================
    def add_to_input(self, char):
        # Робота з рядками
        if char == "." and "." in self.current_input:
            return  # Не дозволяємо два крапки

        self.current_input = self.current_input + char
        self.expression = self.expression + char
        self.update_display(self.current_input)
        self.expr_label.config(text=self.expression)

    def clear(self):
        self.current_input = ""
        self.expression = ""
        self.update_display("0")
        self.expr_label.config(text="")

    def backspace(self):
        # Зрізаємо останній символ (робота з рядками)
        if len(self.current_input) > 0:
            self.current_input = self.current_input[:-1]
            self.expression = self.expression[:-1]

            if self.current_input == "":
                self.update_display("0")
            else:
                self.update_display(self.current_input)

            self.expr_label.config(text=self.expression)

    def toggle_sign(self):
        if self.current_input and self.current_input != "0":
            if self.current_input[0] == "-":
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display(self.current_input)

    def percent(self):
        if self.current_input:
            value = float(self.current_input)
            value = value / 100
            self.current_input = str(value)
            self.update_display(self.current_input)

    def calculate(self):
        if not self.expression:
            return

        try:
            # Обчислюємо вираз
            result = eval(self.expression)

            # Зберігаємо в список (список)
            history_entry = self.expression + " = " + str(result)
            self.history.append(history_entry)

            # Форматуємо результат
            if isinstance(result, float) and result.is_integer():
                result_str = str(int(result))
            else:
                result_str = str(round(result, 8))

            self.expr_label.config(text=self.expression + " =")
            self.update_display(result_str)
            self.current_input = result_str
            self.expression = result_str

        except ZeroDivisionError:
            self.update_display("Ділення на 0!")
            self.current_input = ""
            self.expression = ""

        except Exception:
            self.update_display("Помилка")
            self.current_input = ""
            self.expression = ""

    def update_display(self, value):
        # Обрізаємо якщо дуже довге число (робота з рядками)
        if len(str(value)) > 12:
            value = str(value)[:12]
        self.display.config(text=value)


# ================================
# ЗАПУСК ПРОГРАМИ
# ================================
if __name__ == "__main__":
    root = tk.Tk()

    # Розміщуємо вікно по центру екрану
    window_width = 400
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    app = Calculator(root)
    root.mainloop()
