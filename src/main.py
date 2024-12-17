from ComandHistory import *


# Пример использования
if __name__ == "__main__":
    history_len = 20
    history_leыn = input('Введите количество хранимых команд')

    history = CommandHistory(history_len)

    print("\nМеню:")
    print("1. Добавить команду")
    print("2. Изменить размер истории")
    print("3. Показать команды")
    print("4. Выйти")
    now_command = ''
    while True:
        choice = input("Выберите действие: ")
        if choice == "1":
            command = input("Введите команду: ")
            history.add_command(command)
            print(f"Команда '{command}' добавлена.")

        elif choice == "2":
            try:
                new_size = int(input("Введите новый размер истории: "))
                history.set_size(new_size)
                print(f"Размер истории изменен на {new_size}.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")

        elif choice == "3":
            commands = history.get_commands()
            print("История команд:")
            for i, cmd in enumerate(commands, start=1):
                print(f"{i}: {cmd}")

        elif choice == "4":
            command = history.next_command(now_command)
            now_command = command
            print(now_command)
            
            
        elif choice == "5":
            command = history.prev_command(now_command)
            now_command = command
            print(now_command)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")
