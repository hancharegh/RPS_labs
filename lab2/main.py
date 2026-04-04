import random
from shaker_sort import shaker_sort


def input_from_keyboard() -> list[int]:
    return list(map(int, input("Введите элементы массива через пробел: ").split()))


def generate_random_array() -> list[int]:
    size = int(input("Введите размер массива: "))
    return [random.randint(-100, 100) for _ in range(size)]


def load_from_file(filename: str) -> list[int]:
    with open(filename, "r", encoding="utf-8") as file:
        return list(map(int, file.read().split()))


def save_to_file(filename: str, original: list[int], sorted_arr: list[int]) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Исходный массив:\n{original}\n")
        file.write(f"Отсортированный массив:\n{sorted_arr}\n")


def main():
    print("Выберите способ ввода массива:")
    print("1 — ввод с клавиатуры")
    print("2 — генерация случайных чисел")
    print("3 — загрузка из файла")

    choice = input("Ваш выбор: ")

    if choice == "1":
        array = input_from_keyboard()
    elif choice == "2":
        array = generate_random_array()
    elif choice == "3":
        filename = input("Введите имя файла: ")
        array = load_from_file(filename)
    else:
        print("Некорректный выбор")
        return

    original_array = array.copy()
    sorted_array = shaker_sort(array)

    print("Исходный массив:", original_array)
    print("Отсортированный массив:", sorted_array)

    save = input("Сохранить результат в файл? (y/n): ")
    if save.lower() == "y":
        filename = input("Введите имя файла: ")
        save_to_file(filename, original_array, sorted_array)


if __name__ == "__main__":
    main()
