class MySuperClass:
    """Тестовий клас, описує студента.

    Attributes:
        surname (str): Прізвище студента.
        name (str): Ім'я студента.
        mark (int): Оцінка студента.
        group (str, optional): Група студента.
        _age (int, optional): Вік студента (захищений атрибут).
    """

    def __init__(self, surname: str, name: str, mark: int, group: str = None):
        """Ініціалізуємо об'єкт студента.

        Args:
            surname (str): Прізвище студента.
            name (str): Ім'я студента.
            mark (int): Оцінка студента.
            group (str, optional): Група студента.
        """
        print("Викликаємо __init__")
        self.__surname = surname  # Приватний атрибут
        self.__name = name  # Приватний атрибут
        self.mark = mark  # Публічний атрибут
        self.group = group  # Публічний атрибут
        self._age = None  # Захищений атрибут

    @property
    def name(self):
        """Властивість для доступу до ім'я студента (тільки для читання)."""
        return self.__name

    @property
    def surname(self):
        """Властивість для доступу до прізвища студента (тільки для читання)."""
        return self.__surname

    def __repr__(self):
        return f"MySuperClass(surname={self.surname}, name={self.name}, mark={self.mark})"

    def __len__(self):
        """Повертає довжину прізвища студента."""
        return len(self.surname)

def function_in_module():
    """Приклад функції в модулі. Можна реалізувати тут іншу логіку."""
    pass
