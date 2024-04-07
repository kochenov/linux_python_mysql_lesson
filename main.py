from classes import *

def main():
    """
    Функция, реализующая работу с реестром домашних животных.

    Создает объект реестра, обрабатывает выбор пользователя 
    и выполняет соответствующие действия.
    """
    registry = Registry()  # Создание объекта реестра

    while True:
        """
        Бесконечный цикл для работы с меню.

        Отображает меню, считывает выбор пользователя 
        и вызывает соответствующие функции.
        """
        print("-" * 30)
        print("Реестр домашних животных")
        print("-" * 30)
        print("1. Завести новое животное")
        print("2. Обучить животное команде")
        print("3. Показать список животных")
        print("4. Выход")
        print("-" * 30)

        choice = input("Введите номер пункта: ")

        if choice == "1":
            """
            Обработка пункта меню "Завести новое животное".

            Считывает информацию о животном (тип, имя, возраст), 
            создает объект животного и добавляет его в реестр.
            """
            try:
                animal_type = input("Введите тип животного (собака/кошка): ").lower()
                name = input("Введите имя животного: ")
                age = int(input("Введите возраст животного: "))

                if animal_type not in ("собака", "кошка"):
                    raise ValueError("Неверный тип животного")

                if not all([animal_type, name, age]):
                    raise ValueError("Не все поля заполнены")

                if animal_type == "собака":
                    animal = Dog(name, age)
                elif animal_type == "кошка":
                    animal = Cat(name, age)

                with Counter() as counter:
                    registry.add_animal(animal)
                    print(f"Животное {animal} зарегистрировано")

            except ValueError as e:
                print(f"Ошибка: {e}")

            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")

            finally:
                print("-" * 30)

        elif choice == "2":
            """
            Обработка пункта меню "Обучить животное команде".

            Считывает имя животного и новую команду, 
            обучает животное этой команде.
            """
            try:
                animal_name = input("Введите имя животного: ")
                command = input("Введите новую команду: ")
                registry.teach_command(animal_name, command)
                print(f"Животное {animal_name} обучено команде {command}")

            except KeyError as e:
                print(f"Животное с именем {animal_name} не найдено")

            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")

            finally:
                print("-" * 30)

        elif choice == "3":
            """
            Обработка пункта меню "Показать список животных".

            Выводит список всех животных в реестре 
            с их командами.
            """
            for animal in registry.get_animals():
                print(f"{animal}")
                for command in animal.get_commands():
                    print(f" - {command}")

        elif choice == "4":
            """
            Обработка пункта меню "Выход".

            Завершает работу программы.
            """
            break

        else:
            """
            Обработка ввода неверного номера пункта меню.

            Выводит сообщение о неверном номере пункта.
            """
            print("Неверный номер пункта")


if __name__ == "__main__":
    main()
