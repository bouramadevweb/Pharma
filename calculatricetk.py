import tkinter as tk

def create_button(master, text, row, col, command):
    tk.Button(master, text=text, command=command).grid(row=row, column=col, sticky="nsew")

def on_button_click(result_var, button):
    current_text = result_var.get()

    if button.isdigit() or button == '.':
        # Ajouter le chiffre ou le point au résultat actuel
        result_var.set(current_text + button)
    elif button in ('+', '-', '*', '/'):
        # Ajouter l'opérateur au résultat actuel
        result_var.set(current_text + ' ' + button + ' ')
    elif button == '=':
        try:
            # Évaluer l'expression mathématique et mettre à jour le résultat
            result_var.set(str(eval(current_text)))
        except Exception as e:
            # Gérer les erreurs d'évaluation
            result_var.set("Erreur")
    elif button == 'C':
        # Effacer le résultat actuel
        result_var.set("")

def run_calculator_app():
    root = tk.Tk()
    root.title("Calculatrice")

    result_var = tk.StringVar()
    result_entry = tk.Entry(root, textvariable=result_var, justify="right", font=("Arial", 14))
    result_entry.grid(row=0, column=0, columnspan=3, sticky="nsew")

    buttons = [
        '7', '8', '9',
        '4', '5', '6',
        '1', '2', '3',
        '0', '.', '+', '-', '*', '/',
        '=', 'C'
    ]

    row_val = 1
    col_val = 0
    for button in buttons:
        create_button(root, button, row_val, col_val, lambda b=button: on_button_click(result_var, b))
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    for i in range(1, 5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    run_calculator_app()
