import math
import random
import tkinter as tk
from tkinter import filedialog

def generate_star(center_x, center_y, size, angle_offset):
    points = []
    for i in range(5):
        angle = math.radians(72 * i - 90 + angle_offset)
        x = center_x + size * math.cos(angle)
        y = center_y + size * math.sin(angle)
        x += random.uniform(-1, 1)
        y += random.uniform(-1, 1)
        points.append((x, y))
    
    star_points = [
        points[0], points[2], points[4], points[1], points[3], points[0]
    ]
    return star_points

def generate_spiral(center_x, center_y, turns, spacing):
    points = []
    for i in range(turns * 360):
        angle = math.radians(i)
        radius = spacing * i / 360
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    return points

def generate_rectangular_spiral(center_x, center_y, turns, spacing, width, height, angle_offset):
    points = []
    for i in range(turns):
        for j in range(4):
            angle = math.radians(90 * j + angle_offset)
            if j % 2 == 0:
                length = width + spacing * i
            else:
                length = height + spacing * i
            x = center_x + length * math.cos(angle)
            y = center_y + length * math.sin(angle)
            points.append((x, y))
    return points

def generate_random_rectangular_spiral(center_x, center_y, turns, spacing):
    points = []
    for i in range(turns):
        width = random.uniform(5, 15)
        height = random.uniform(5, 15)
        angle_offset = random.uniform(0, 360)
        for j in range(4):
            angle = math.radians(90 * j + angle_offset)
            if j % 2 == 0:
                length = width + spacing * i
            else:
                length = height + spacing * i
            x = center_x + length * math.cos(angle)
            y = center_y + length * math.sin(angle)
            points.append((x, y))
    return points

def read_coordinates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    coordinates = []
    for line in lines:
        if line.startswith('G0'):
            parts = line.split()
            x = float(parts[1][1:])
            y = float(parts[2][1:])
            coordinates.append((x, y))
    return coordinates

def write_shapes(file_path, shapes):
    with open(file_path, 'w') as file:
        for shape in shapes:
            file.write("G0 F5000 Z30\n")
            file.write(f"G0 F5000\nG1 X{shape[0][0]} Y{shape[0][1]}\n")
            file.write("G0 F5000 Z1\n")
            for point in shape:
                file.write(f"G1 X{point[0]} Y{point[1]}\n")
            file.write("\n")

def generate_stars(input_file, output_file):
    coordinates = read_coordinates(input_file)
    stars = []
    for x, y in coordinates:
        size = random.uniform(5, 15)
        angle_offset = random.uniform(0, 360)
        star = generate_star(x, y, size, angle_offset)
        stars.append(star)
    write_shapes(output_file, stars)

def generate_spirals(input_file, output_file):
    coordinates = read_coordinates(input_file)
    spirals = []
    for x, y in coordinates:
        turns = random.randint(3, 10)
        spacing = random.uniform(0.5, 2)
        spiral = generate_spiral(x, y, turns, spacing)
        spirals.append(spiral)
    write_shapes(output_file, spirals)

def generate_rectangular_spirals(input_file, output_file):
    coordinates = read_coordinates(input_file)
    spirals = []
    for x, y in coordinates:
        turns = random.randint(3, 10)
        spacing = random.uniform(0.5, 2)
        width = random.uniform(5, 15)
        height = random.uniform(5, 15)
        angle_offset = random.uniform(0, 360)
        spiral = generate_rectangular_spiral(x, y, turns, spacing, width, height, angle_offset)
        spirals.append(spiral)
    write_shapes(output_file, spirals)

def generate_random_rectangular_spirals(input_file, output_file):
    coordinates = read_coordinates(input_file)
    spirals = []
    for x, y in coordinates:
        turns = random.randint(3, 10)
        spacing = random.uniform(0.5, 2)
        spiral = generate_random_rectangular_spiral(x, y, turns, spacing)
        spirals.append(spiral)
    write_shapes(output_file, spirals)

def select_input_file():
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".ngc")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def run_star_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_stars(input_file, output_file)

def run_spiral_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_spirals(input_file, output_file)

def run_rectangular_spiral_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_rectangular_spirals(input_file, output_file)

def run_random_rectangular_spiral_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_random_rectangular_spirals(input_file, output_file)

# Создание графического интерфейса
root = tk.Tk()
root.title("Shape Generator")

tk.Label(root, text="Input File:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Generate Stars", command=run_star_script).grid(row=2, column=0, columnspan=3, pady=10)
tk.Button(root, text="Generate Spirals", command=run_spiral_script).grid(row=3, column=0, columnspan=3, pady=10)
tk.Button(root, text="Generate Rectangular Spirals", command=run_rectangular_spiral_script).grid(row=4, column=0, columnspan=3, pady=10)
tk.Button(root, text="Generate Random Rectangular Spirals", command=run_random_rectangular_spiral_script).grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
