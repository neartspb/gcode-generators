import math
import random
import tkinter as tk
from tkinter import filedialog

def generate_triangle(center_x, center_y, size, angle_offset):
    points = []
    for i in range(3):
        angle = math.radians(120 * i + angle_offset)
        x = center_x + size * math.cos(angle)
        y = center_y + size * math.sin(angle)
        points.append((x, y))
    points.append(points[0])  # Замыкаем треугольник
    return points

def generate_square(center_x, center_y, size, angle_offset):
    points = []
    for i in range(4):
        angle = math.radians(90 * i + angle_offset)
        x = center_x + size * math.cos(angle)
        y = center_y + size * math.sin(angle)
        points.append((x, y))
    points.append(points[0])  # Замыкаем квадрат
    return points

def generate_circle(center_x, center_y, radius):
    points = []
    for i in range(360):
        angle = math.radians(i)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
    points.append(points[0])  # Замыкаем круг
    return points

def generate_ellipse(center_x, center_y, width, height, angle_offset):
    points = []
    for i in range(360):
        angle = math.radians(i)
        x = center_x + (width / 2) * math.cos(angle) * math.cos(math.radians(angle_offset)) - (height / 2) * math.sin(angle) * math.sin(math.radians(angle_offset))
        y = center_y + (width / 2) * math.cos(angle) * math.sin(math.radians(angle_offset)) + (height / 2) * math.sin(angle) * math.cos(math.radians(angle_offset))
        points.append((x, y))
    points.append(points[0])  # Замыкаем эллипс
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

def generate_triangles(input_file, output_file):
    coordinates = read_coordinates(input_file)
    triangles = []
    for x, y in coordinates:
        size = random.uniform(5, 15)
        angle_offset = random.uniform(0, 360)
        triangle = generate_triangle(x, y, size, angle_offset)
        triangles.append(triangle)
    write_shapes(output_file, triangles)

def generate_squares(input_file, output_file):
    coordinates = read_coordinates(input_file)
    squares = []
    for x, y in coordinates:
        size = random.uniform(5, 15)
        angle_offset = random.uniform(0, 360)
        square = generate_square(x, y, size, angle_offset)
        squares.append(square)
    write_shapes(output_file, squares)

def generate_circles(input_file, output_file):
    coordinates = read_coordinates(input_file)
    circles = []
    for x, y in coordinates:
        radius = random.uniform(5, 15)
        circle = generate_circle(x, y, radius)
        circles.append(circle)
    write_shapes(output_file, circles)

def generate_ellipses(input_file, output_file):
    coordinates = read_coordinates(input_file)
    ellipses = []
    for x, y in coordinates:
        width = random.uniform(5, 15)
        height = random.uniform(5, 105)
        angle_offset = random.uniform(0, 360)
        ellipse = generate_ellipse(x, y, width, height, angle_offset)
        ellipses.append(ellipse)
    write_shapes(output_file, ellipses)

def select_input_file():
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".ngc")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def run_triangle_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_triangles(input_file, output_file)

def run_square_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_squares(input_file, output_file)

def run_circle_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_circles(input_file, output_file)

def run_ellipse_script():
    input_file = input_entry.get()
    output_file = output_entry.get()
    generate_ellipses(input_file, output_file)

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

tk.Button(root, text="Generate Triangles", command=run_triangle_script).grid(row=2, column=0, columnspan=3, pady=10)
tk.Button(root, text="Generate Squares", command=run_square_script).grid(row=3, column=0, columnspan=3, pady=10)
tk.Button(root, text="Generate Circles", command=run_circle_script).grid(row=4, column=0, columnspan=3, pady=10)
tk.Button(root, text="Generate Ellipses", command=run_ellipse_script).grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
