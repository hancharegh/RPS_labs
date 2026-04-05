import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

from auth import login, register
from shaker_sort import shaker_sort
from array_service import save_array, get_arrays


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab 3 App")
        self.user_id = None
        self.array = []

        self.login_screen()

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

    def main_screen(self):
        self.clear()

        tk.Button(self.root, text="Ввести массив", command=self.manual_input).pack()
        tk.Button(self.root, text="Сгенерировать массив", command=self.generate).pack()
        tk.Button(self.root, text="Сортировать", command=self.sort).pack()
        tk.Button(self.root, text="Сохранить", command=self.save).pack()
        tk.Button(self.root, text="Показать сохранённые", command=self.show_saved).pack()

        self.output = tk.Text(self.root, height=10)
        self.output.pack()

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
        data = self.simple_input("Введите числа через пробел:")
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
        self.sorted_array = shaker_sort(self.array)
        self.output.insert(tk.END, f"\n{self.sorted_array}")

    def save(self):
        save_array(self.user_id, self.array, self.sorted_array)
        messagebox.showinfo("OK", "Сохранено")

    def show_saved(self):
        data = get_arrays(self.user_id)
        for d in data:
            self.output.insert(tk.END, f"\n{d}")

    def simple_input(self, text):
        return tk.simpledialog.askstring("Ввод", text)

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()
