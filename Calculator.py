import tkinter as tk
def press(num):
    global expression
    expression = expression + str(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)
def equalpress():
    try:
        global expression
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = ""
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: " + str(e))
        expression = ""
def clear():
    global expression
    entry.delete(0, tk.END)
    expression = ""
window = tk.Tk()
window.title("Large Calculator")
window.color="lightblue"
expression = ""
entry = tk.Entry(window, font=("Arial", 20), width=30,bg="green")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
row = 1
col = 0
for button in buttons:
    btn = tk.Button(window, text=button, fg='black', bg='blue', font=("Arial", 16), height=2, width=8)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.config(command=lambda num=button: press(num))
    col += 1
    if col > 3:
        col = 0
        row += 1
clear_button = tk.Button(window, text='Clear', fg='black', bg='blue', font=("Arial", 16), height=2, width=8, command=clear)
clear_button.grid(row=row, column=col, padx=5, pady=5)
equal_button = tk.Button(window, text='=', fg='black', bg='blue', font=("Arial", 16), height=2, width=8, command=equalpress)
equal_button.grid(row=row+1, column=col, padx=5, pady=5)
window.mainloop()