import tkinter as tk
from tkinter import filedialog, messagebox
import re

def round_coordinates(line, precision):
    # Функция для округления координат до указанного количества знаков после запятой
    def round_match(match):
        return f"{float(match.group()):.{precision}f}"
    
    return re.sub(r"\d+\.\d+", round_match, line)

def process_file(input_path, output_path, precision):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    with open(output_path, 'w') as file:
        for line in lines:
            rounded_line = round_coordinates(line, precision)
            file.write(rounded_line)

def choose_file():
    input_path = filedialog.askopenfilename(filetypes=[("G-code and NGC files", "*.gcode;*.ngc")])
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".ngc", filetypes=[("G-code and NGC files", "*.gcode;*.ngc")])
        if output_path:
            precision = int(precision_entry.get())
            process_file(input_path, output_path, precision)
            messagebox.showinfo("Успех", "Файл успешно обработан и сохранен!")

# Создание графического интерфейса
root = tk.Tk()
root.title("G-code and NGC Rounding Tool")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

precision_label = tk.Label(frame, text="Количество знаков после запятой:")
precision_label.pack()

precision_entry = tk.Entry(frame)
precision_entry.pack()

button = tk.Button(frame, text="Выбрать и обработать файл", command=choose_file)
button.pack()

root.mainloop()
