import json
import tkinter as tk
from tkinter import ttk, messagebox


def load_teachers():
    """Load teacher data from the JSON file."""
    with open("teachers.json", "r", encoding="utf-8") as f:
        return json.load(f)


def on_select(*_):
    """Update the UI when a teacher is selected."""
    name = teacher_var.get()
    teacher = next(t for t in teachers if t["name"] == name)
    grade_var.set(teacher["grade"])
    parallel_var.set(teacher["parallel"])
    students_var.set(str(teacher["students"]))

    # Clear previous menu entries
    for widget in menu_frame.winfo_children():
        widget.destroy()
    entry_vars.clear()

    # Create entry widgets for each menu item
    for menu_name, qty in teacher["menus"].items():
        row = ttk.Frame(menu_frame)
        row.pack(fill="x", pady=2)
        ttk.Label(row, text=menu_name).pack(side="left")
        var = tk.IntVar(value=qty)
        entry_vars[menu_name] = var
        ttk.Entry(row, textvariable=var, width=5).pack(side="right")


def confirm():
    """Show a confirmation message."""
    messagebox.showinfo("Confirmación", "Datos confirmados")


def main():
    global teachers, teacher_var, grade_var, parallel_var, students_var, menu_frame, entry_vars

    teachers = load_teachers()

    root = tk.Tk()
    root.title("Listado de Docentes")

    teacher_var = tk.StringVar()
    grade_var = tk.StringVar()
    parallel_var = tk.StringVar()
    students_var = tk.StringVar()
    entry_vars = {}

    ttk.Label(root, text="Seleccione un docente:").pack(anchor="w")
    teacher_names = [t["name"] for t in teachers]
    option_menu = ttk.OptionMenu(root, teacher_var, teacher_names[0], *teacher_names, command=on_select)
    option_menu.pack(fill="x")

    info = ttk.Frame(root)
    info.pack(fill="x", pady=5)

    ttk.Label(info, text="Nombre:").grid(row=0, column=0, sticky="w")
    ttk.Label(info, textvariable=teacher_var).grid(row=0, column=1, sticky="w")

    ttk.Label(info, text="Grado:").grid(row=1, column=0, sticky="w")
    ttk.Label(info, textvariable=grade_var).grid(row=1, column=1, sticky="w")

    ttk.Label(info, text="Paralelo:").grid(row=2, column=0, sticky="w")
    ttk.Label(info, textvariable=parallel_var).grid(row=2, column=1, sticky="w")

    ttk.Label(info, text="Número de estudiantes:").grid(row=3, column=0, sticky="w")
    ttk.Label(info, textvariable=students_var).grid(row=3, column=1, sticky="w")

    menu_frame = ttk.LabelFrame(root, text="Menús entregados")
    menu_frame.pack(fill="x", pady=5)

    ttk.Button(root, text="OK", command=confirm).pack(pady=5)

    # Initialize with first teacher selected
    teacher_var.set(teacher_names[0])
    on_select()

    root.mainloop()


if __name__ == "__main__":
    main()
