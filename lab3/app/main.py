import tkinter as tk
from tkinter import messagebox

from gui import App
from db import init_db
from auth import login, register


def open_main_app(user_id):
    root = tk.Tk()
    app = App(root, user_id, show_login)
    root.mainloop()


def show_login():
    login_window = tk.Tk()
    login_window.title("Авторизация")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Логин").pack()
    username = tk.Entry(login_window)
    username.pack()

    tk.Label(login_window, text="Пароль").pack()
    password = tk.Entry(login_window, show="*")
    password.pack()

    def try_login():
        user_id = login(username.get(), password.get())

        if user_id:
            login_window.destroy()
            open_main_app(user_id)
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

    def try_register():
        if register(username.get(), password.get()):
            messagebox.showinfo("Успех", "Пользователь создан")
        else:
            messagebox.showerror("Ошибка", "Пользователь уже существует")

    tk.Button(login_window, text="Войти", command=try_login).pack(pady=5)
    tk.Button(login_window, text="Регистрация", command=try_register).pack()

    login_window.mainloop()


if __name__ == "__main__":
    init_db()
    show_login()
