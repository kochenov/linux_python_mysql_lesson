class Animal:
    """
    Базовый класс для всех домашних животных.
    """
    def __init__(self, species, name, age):
        """
        Инициализация животного.

        Args:
            species (str): Вид животного (например, "Собака", "Кошка").
            name (str): Кличка животного.
            age (int): Возраст животного (в годах).
        """
        self.species = species
        self.name = name
        self.age = age
        self.commands = set()  # Множество для хранения выученных команд

    def add_command(self, command):
        """
        Добавляет новую команду животному.

        Args:
            command (str): Новая команда, которую должно выучить животное.
        """
        self.commands.add(command)

    def get_commands(self):
        """
        Возвращает список выученных животным команд (отсортированный).

        Returns:
            list: Список выученных команд.
        """
        return sorted(self.commands)

    def __repr__(self):
        """
        Определяет строковое представление объекта Animal.

        Returns:
            str: Строка вида "Вид Кличка (Возраст)".
        """
        return f"{self.species} {self.name} ({self.age})"
    



class Dog(Animal):
    """
    Класс, описывающий собаку.

    Наследует от класса Animal.
    """
    def __init__(self, name, age):
        """
        Инициализация собаки.

        Args:
            name (str): Кличка собаки.
            age (int): Возраст собаки (в годах).
        """
        super().__init__("Собака", name, age)  # Инициализация базового класса Animal

        # Добавление стандартных команд для собаки
        self.commands.add("Сидеть")
        self.commands.add("Лежать")

class Cat(Animal):
    """
    Класс, описывающий кошку.

    Наследует от класса Animal.
    """
    def __init__(self, name, age):
        """
        Инициализация кошки.

        Args:
            name (str): Кличка кошки.
            age (int): Возраст кошки (в годах).
        """
        super().__init__("Кошка", name, age)  # Инициализация базового класса Animal

        # Добавление стандартной команды для кошки
        self.commands.add("Дай лапу")


class Registry:
    """
    Класс для управления реестром домашних животных.
    """
    def __init__(self):
        """
        Инициализация реестра.
        """
        self.animals = []  # Список животных в реестре

    def add_animal(self, animal):
        """
        Добавляет животное в реестр.

        Args:
            animal (Animal): Объект класса Animal, представляющий животное.
        """
        self.animals.append(animal)

    def get_animals(self):
        """
        Возвращает список всех животных в реестре, отсортированный по виду.

        Returns:
            list: Список объектов класса Animal.
        """
        return sorted(self.animals, key=lambda a: a.species)

    def get_animal_by_name(self, name):
        """
        Ищет животное в реестре по имени.

        Args:
            name (str): Кличка животного.

        Returns:
            Animal: Объект класса Animal, если животное найдено, иначе None.
        """
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def teach_command(self, animal_name, command):
        """
        Обучает животное новой команде.

        Args:
            animal_name (str): Кличка животного.
            command (str): Новая команда.
        """
        animal = self.get_animal_by_name(animal_name)
        if animal:
            animal.add_command(command)  # Добавляем команду найденному животному



class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Ошибка при работе со счетчиком")
        else:
            print(f"Добавлено новое животное (счетчик: {self.count})")