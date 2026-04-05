import tkinter as tk
from tkinter import messagebox, simpledialog
import random

from auth import login, register
from shaker_sort import shaker_sort
from array_service import save_array, get_arrays


class App:
    def __init__(self, root):  # <-- исправлено с init на __init__
        self.root = root
        self.root.title("Lab 3 App")
        self.user_id = None
        self.array = []
        self.sorted_array = []

        self.login_screen()

    # ------------------ ЭКРАН ЛОГИНА ------------------
    def login_screen(self):
        self.clear()

        tk.Label(self.root, text="Логин").pack()
        self.login_entry = tk.Entry(self.root)
        self.login_entry.pack()

        tk.Label(self.root, text="Пароль").pack()
        self.pass_entry = tk.Entry(self.root, show="*")
        self.pass_entry.pack()

        tk.Button(self.root, text="Войти", command=self.do_login).pack()
        tk.Button(self.root, text="Регистрация", command=self.do_register).pack()

    # ------------------ ГЛАВНЫЙ ЭКРАН ------------------
    def main_screen(self):
        self.clear()

        tk.Button(self.root, text="Ввести массив", command=self.manual_input).pack()
        tk.Button(self.root, text="Сгенерировать массив", command=self.generate).pack()
        tk.Button(self.root, text="Сортировать", command=self.sort).pack()
        tk.Button(self.root, text="Сохранить", command=self.save).pack()
        tk.Button(self.root, text="Показать сохранённые", command=self.show_saved).pack()
        tk.Button(self.root, text="Справка", command=self.show_help).pack()
        tk.Button(self.root, text="Выйти", command=self.logout).pack()  # кнопка выхода

        self.output = tk.Text(self.root, height=10)
        self.output.pack()

    # ------------------ МЕТОДЫ КНОПОК ------------------
    def do_login(self):
        user = login(self.login_entry.get(), self.pass_entry.get())
        if user:
            self.user_id = user
            self.main_screen()
        else:
            messagebox.showerror("Ошибка", "Неверный логин/пароль")

    def do_register(self):
        if register(self.login_entry.get(), self.pass_entry.get()):
            messagebox.showinfo("Успех", "Регистрация успешна")
        else:
            messagebox.showerror("Ошибка", "Пользователь уже есть")

    def manual_input(self):
        data = simpledialog.askstring("Ввод", "Введите числа через пробел:")
        if not data:
            return
        try:
            self.array = list(map(int, data.split()))
            self.output.insert(tk.END, f"\n{self.array}")
        except:
            messagebox.showerror("Ошибка", "Некорректный ввод")

    def generate(self):
        self.array = [random.randint(-100, 100) for _ in range(10)]
        self.output.insert(tk.END, f"\n{self.array}")

    def sort(self):
        if not self.array:
            messagebox.showwarning("Предупреждение", "Массив пуст")
            return
        self.sorted_array = shaker_sort(self.array)
        self.output.insert(tk.END, f"\n{self.sorted_array}")

    def save(self):
        if not self.array or not self.sorted_array:
            messagebox.showwarning("Предупреждение", "Нет данных для сохранения")
            return
        save_array(self.user_id, self.array, self.sorted_array)
        messagebox.showinfo("OK", "Сохранено")

    def show_saved(self):
        data = get_arrays(self.user_id)
        if not data:
            messagebox.showinfo("Сохранённые массивы", "Нет сохранённых массивов")
            return
        for d in data:
            self.output.insert(tk.END, f"\n{d}")

    def show_help(self):
        help_text = (
            "Инструкция по использованию приложения:\n\n"
            "1. Введите логин и пароль для входа или регистрации.\n"
            "2. На главном экране вы можете:\n"
            "   - Ввести массив вручную через пробел.\n"
            "   - Сгенерировать случайный массив (10 элементов от -100 до 100).\n"
            "   - Отсортировать массив с помощью сортировки перемешиванием.\n""   - Сохранить массив и отсортированный результат.\n"
            "   - Просмотреть ранее сохранённые массивы.\n"
            "3. Для ввода чисел используйте только целые числа, разделённые пробелом.\n"
            "4. Кнопка 'Выйти' возвращает на экран логина.\n"
            "5. Справка доступна на этом экране по кнопке 'Справка'."
        )
        messagebox.showinfo("Справка", help_text)

    def logout(self):
        """Возврат на экран логина"""
        self.user_id = None
        self.array = []
        self.sorted_array = []
        self.login_screen()

    # ------------------ ВСПОМОГАТЕЛЬНЫЕ ------------------
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()
