# --- Класс Animal ---

class Animal:
    """
    Абстрактный класс для представления животных.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
    """

    def __init__(self, name, age):
        """
        Инициализирует новый объект Animal.

        Args:
            name (str): Имя животного.
            age (int): Возраст животного.
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        Возвращает строковое представление объекта Animal.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Животное: {self.name}, возраст: {self.age}"


# --- Класс Pet ---

class Pet(Animal):
    """
    Класс для представления домашних животных.

    Наследует от Animal.

    Атрибуты:
        breed (str): Порода домашнего животного.
    """

    def __init__(self, name, age, breed):
        """
        Инициализирует новый объект Pet.

        Args:
            name (str): Имя животного.
            age (int): Возраст животного.
            breed (str): Порода домашнего животного.
        """
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        """
        Возвращает строковое представление объекта Pet.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Домашнее животное: {self.name}, возраст: {self.age}, порода: {self.breed}"

    def make_sound(self):
        """
        Абстрактный метод, который должен быть переопределен в классах-наследниках.

        Возвращает звук, издаваемый животным.

        Returns:
            str: Звук, издаваемый животным.
        """
        raise NotImplementedError


# --- Класс Dog ---

class Dog(Pet):
    """
    Класс для представления собак.

    Наследует от Pet.
    """

    def __init__(self, name, age, breed):
        """
        Инициализирует новый объект Dog.

        Args:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, age, breed)

    def __str__(self):
        """
        Возвращает строковое представление объекта Dog.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Собака: {self.name}, возраст: {self.age}, порода: {self.breed}"

    def make_sound(self):
        """
        Возвращает звук, издаваемый собакой.

        Returns:
            str: Звук "Гав!".
        """
        return "Гав!"


# --- Класс Cat ---

class Cat(Pet):
    """
    Класс для представления кошек.

    Наследует от Pet.
    """

    def __init__(self, name, age, breed):
        """
        Инициализирует новый объект Cat.

        Args:
            name (str): Имя кошки.
            age (int): Возраст кошки.
            breed (str): Порода кошки.
        """
        super().__init__(name, age, breed)

    def __str__(self):
        """
        Возвращает строковое представление объекта Cat.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Кошка: {self.name}, возраст: {self.age}, порода: {self.breed}"

    def make_sound(self):
        """
        Возвращает звук, издаваемый кошкой.

        Returns:
            str: Звук "Мяу!".
        """
        return "Мяу!"


# --- Класс Hamster ---

class Hamster(Pet):
    """
    Класс для представления хомяков.

    Наследует от Pet.
    """

    def __init__(self, name, age, breed):
        """
        Инициализирует новый объект Hamster.

        Args:
            name (str): Имя хомяка.
            age (int): Возраст хомяка.
            breed (str): Порода хомяка.
        """
        super().__init__(name, age, breed)

    def __str__(self):
        """
        Возвращает строковое представление объекта Hamster.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Хомяк: {self.name}, возраст: {self.age}, порода: {self.breed}"

    def make_sound(self):
        """
        Возвращает звук, издаваемый хомяком.

        Returns:
            str: Звук "Писк!".
        """
        return "Писк!"


# --- Класс PackAnimal ---

class PackAnimal(Animal):
    """
    Абстрактный класс для представления вьючных животных.

    Наследует от Animal.

    Атрибуты:
        carrying_capacity (int): Грузоподъемность животного.
    """

    def __init__(self, name, age, carrying_capacity):
        """
        Инициализирует новый объект PackAnimal.

        Args:
            name (str): Имя животного.
            age (int): Возраст животного.
            carrying_capacity (int): Грузоподъемность животного.
        """
        super().__init__(name, age)
        self.carrying_capacity = carrying_capacity

    def __str__(self):
        """
        Возвращает строковое представление объекта PackAnimal.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Вьючное животное: {self.name}, возраст: {self.age}, грузоподъемность: {self.carrying_capacity}"


# --- Класс Horse ---

class Horse(PackAnimal):
    """
    Класс для представления лошадей.

    Наследует от PackAnimal.
    """

    def __init__(self, name, age, carrying_capacity):
        """
        Инициализирует новый объект Horse.

        Args:
            name (str): Имя лошади.
            age (int): Возраст лошади.
            carrying_capacity (int): Грузоподъемность лошади.
        """
        super().__init__(name, age, carrying_capacity)

    def __str__(self):
        """
        Возвращает строковое представление объекта Horse.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Лошадь: {self.name}, возраст: {self.age}, грузоподъемность: {self.carrying_capacity}"

    def gallop(self):
        """
        Возвращает строку, описывающую скачку лошади.

        Returns:
            str: "Скачет!".
        """
        return "Скачет!"


# --- Класс Camel ---

class Camel(PackAnimal):
    """
    Класс для представления верблюдов.

    Наследует от PackAnimal.

    Атрибуты:
        humps (int): Количество горбов у верблюда.
    """

    def __init__(self, name, age, carrying_capacity, humps):
        """
        Инициализирует новый объект Camel.

        Args:
            name (str): Имя верблюда.
            age (int): Возраст верблюда.
            carrying_capacity (int): Грузоподъемность верблюда.
            humps (int): Количество горбов у верблюда.
        """
        super().__init__(name, age, carrying_capacity)
        self.humps = humps

    def __str__(self):
        """
        Возвращает строковое представление объекта Camel.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Верблюд: {self.name}, возраст: {self.age}, грузоподъемность: {self.carrying_capacity}, количество горбов: {self.humps}"

# --- Класс Donkey ---

class Donkey(PackAnimal):
    """
    Класс для представления ослов.

    Наследует от PackAnimal.

    Атрибуты:
        stubbornness (int): Упрямство осла.
    """

    def __init__(self, name, age, carrying_capacity, stubbornness):
        """
        Инициализирует новый объект Donkey.

        Args:
            name (str): Имя осла.
            age (int): Возраст осла.
            carrying_capacity (int): Грузоподъемность осла.
            stubbornness (int): Упрямство осла.
        """
        super().__init__(name, age, carrying_capacity)
        self.stubbornness = stubbornness

    def __str__(self):
        """
        Возвращает строковое представление объекта Donkey.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Осёл: {self.name}, возраст: {self.age}, грузоподъемность: {self.carrying_capacity}, упрямство: {self.stubbornness}"

    def be_stubborn(self):
        """
        Возвращает строку, описывающую упрямство осла.

        Returns:
            str: "Упрямится!".
        """
        return "Упрямится!"