import tkinter as tk
from tkinter import messagebox, simpledialog
import random

from array_service import save_array, get_arrays
from shaker_sort import shaker_sort


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Сортировка массивов")
        self.root.geometry("600x500")

        self.array = []

       
        self.status = tk.Label(root, text="Готов к работе", bd=1, relief=tk.SUNKEN, anchor="w")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

       
        input_frame = tk.LabelFrame(root, text="Ввод массива", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(input_frame, text="Ввести вручную", command=self.manual_input).pack(side="left", padx=5)
        tk.Button(input_frame, text="Сгенерировать", command=self.generate_array).pack(side="left", padx=5)

        
        action_frame = tk.LabelFrame(root, text="Действия", padx=10, pady=10)
        action_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(action_frame, text="Сортировать", command=self.sort_array).pack(side="left", padx=5)
        tk.Button(action_frame, text="Сохранить", command=self.save).pack(side="left", padx=5)
        tk.Button(action_frame, text="Показать сохранённые", command=self.show_saved).pack(side="left", padx=5)

        
        output_frame = tk.LabelFrame(root, text="Результат", padx=10, pady=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.output = tk.Text(output_frame, height=15)
        self.output.pack(fill="both", expand=True)

    # ------------------------

    def set_status(self, text):
        self.status.config(text=text)

    def manual_input(self):
        data = simpledialog.askstring("Ввод", "Введите числа через пробел:")

        if not data:
            return

        try:
            self.array = list(map(int, data.split()))
            self.output.insert(tk.END, f"\nИсходный: {self.array}")
            self.set_status("Массив введён вручную")
        except:
            messagebox.showerror("Ошибка", "Некорректный ввод")

    def generate_array(self):
        self.array = [random.randint(0, 100) for _ in range(10)]
        self.output.insert(tk.END, f"\nСгенерирован: {self.array}")
        self.set_status("Массив сгенерирован")

    def sort_array(self):
        if not self.array:
            messagebox.showwarning("Ошибка", "Сначала введите массив")
            return

        sorted_arr = shaker_sort(self.array)
        self.output.insert(tk.END, f"\nОтсортирован: {sorted_arr}")
        self.set_status("Массив отсортирован")

    def save(self):
        if not self.array:
            messagebox.showwarning("Ошибка", "Нет данных для сохранения")
            return

        sorted_arr = shaker_sort(self.array)
        save_array(1, self.array, sorted_arr)

        self.set_status("Массив сохранён")

    def show_saved(self):
        data = get_arrays(1)

        self.output.insert(tk.END, "\n\nСохранённые массивы:\n")

        for original, sorted_arr in data:
            self.output.insert(tk.END, f"\n{original} -> {sorted_arr}")

        self.set_status("Загружены сохранённые массивы")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
