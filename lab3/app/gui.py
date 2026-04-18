import tkinter as tk
from tkinter import messagebox, simpledialog
import random

from array_service import save_array, get_arrays
from shaker_sort import shaker_sort


class App:
    def __init__(self, root, user_id, logout_callback):
        self.root = root
        self.user_id = user_id
        self.logout_callback = logout_callback

        self.root.title("Сортировка массивов")
        self.root.geometry("600x500")

        self.array = []

        # статус
        self.status = tk.Label(root, text="Готов к работе", bd=1, relief=tk.SUNKEN, anchor="w")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        # верхняя панель
        top_frame = tk.Frame(root)
        top_frame.pack(fill="x")

        tk.Button(top_frame, text="Справка", command=self.show_help).pack(side="left", padx=10, pady=5)
        tk.Button(top_frame, text="Выйти", command=self.logout, bg="red", fg="white").pack(side="right", padx=10, pady=5)

        # ввод
        input_frame = tk.LabelFrame(root, text="Ввод массива", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(input_frame, text="Ввести вручную", command=self.manual_input).pack(side="left", padx=5)
        tk.Button(input_frame, text="Сгенерировать", command=self.generate_array).pack(side="left", padx=5)

        # действия
        action_frame = tk.LabelFrame(root, text="Действия", padx=10, pady=10)
        action_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(action_frame, text="Сортировать", command=self.sort_array).pack(side="left", padx=5)
        tk.Button(action_frame, text="Сохранить", command=self.save).pack(side="left", padx=5)
        tk.Button(action_frame, text="Показать сохранённые", command=self.show_saved).pack(side="left", padx=5)

        # вывод
        output_frame = tk.LabelFrame(root, text="Результат", padx=10, pady=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.output = tk.Text(output_frame, height=15)
        self.output.pack(fill="both", expand=True)

    # ------------------------

    def logout(self):
        self.root.destroy()
        self.logout_callback()

    def show_help(self):
        help_text = (
            "📌 Справка по программе\n\n"
            "Данная программа предназначена для работы с массивами чисел.\n\n"
            "Возможности:\n"
            "• Ввод массива вручную\n"
            "• Генерация случайного массива\n"
            "• Сортировка (шейкерная сортировка)\n"
            "• Сохранение массивов в базу данных\n"
            "• Просмотр сохранённых массивов\n\n"
            "Как пользоваться:\n"
            "1. Введите массив или сгенерируйте его\n"
            "2. Нажмите 'Сортировать'\n"
            "3. При необходимости сохраните результат\n"
            "4. Можно посмотреть сохранённые массивы\n\n"
            "Авторизация:\n"
            "Каждый пользователь видит только свои данные\n"
        )

        messagebox.showinfo("Справка", help_text)

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
        save_array(self.user_id, self.array, sorted_arr)

        self.set_status("Массив сохранён")

    def show_saved(self):
        data = get_arrays(self.user_id)

        self.output.insert(tk.END, "\n\nСохранённые массивы:\n")

        for original, sorted_arr in data:
            self.output.insert(tk.END, f"\n{original} -> {sorted_arr}")

        self.set_status("Загружены сохранённые массивы")
