class MySuperClass:
    """Тестовий клас, описує студента."""

    # Класові змінні
    COLLEGE_NAME = "Національний університет"
    total_students = 0
    total_marks = 0

    def __init__(self, surname: str, name: str, mark: int = 0, group: str = None):
        """Ініціалізуємо об'єкт студента."""
        self.__surname = surname  # Приватний атрибут для прізвища
        self.__name = name  # Приватний атрибут для імені
        self.mark = mark  # Публічний атрибут для оцінки
        self.group = group  # Публічний атрибут для групи
        self._age = None  # Захищений атрибут для віку (поки не використовується)
        self._scholarship = None  # Спочатку стипендія не встановлена

        # Оновлюємо статистику
        MySuperClass.total_students += 1
        MySuperClass.total_marks += self.mark

    def __del__(self):
        """Викликається при видаленні об'єкта. Зменшує кількість студентів."""
        MySuperClass.total_students -= 1
        MySuperClass.total_marks -= self.mark

    @property
    def scholarship(self):
        """Властивість для отримання стипендії."""
        return self._scholarship or "Стипендія не призначена"

    def update_scholarship(self, rating: int, special_case: bool = False):
        """
        Оновлює стипендію студента на основі оцінки та додаткових умов.
        
        Параметри:
            rating (int): Рейтинг студента (1-5).
            special_case (bool): Якщо студент має особливий статус (наприклад, сирота, учасник змагань).
        """
        if special_case:
            self._scholarship = "2000 грн (Особливий статус)"
            return "Призначено підвищену стипендію через особливий статус"

        if rating == 5:
            self._scholarship = "1800 грн"
            return "Присвоєно підвищену стипендію"
        elif rating == 4:
            self._scholarship = "1400 грн"
            return "Присвоєно звичайну стипендію"
        else:
            self._scholarship = None
            return "Рейтинг занизький для стипендії"

    def show_student_info(self):
        """Показує інформацію про студента."""
        return (
            f"Студент: {self.__name} {self.__surname}\n"
            f"Оцінка: {self.mark}\n"
            f"Група: {self.group or 'Не вказана'}\n"
            f"Стипендія: {self.scholarship}"
        )

    @property
    def name(self):
        """Ім'я студента."""
        return self.__name

    @property
    def surname(self):
        """Прізвище студента."""
        return self.__surname

    # Альтернативний конструктор для створення об'єкта за ім'ям та прізвищем
    @classmethod
    def create_from_name_surname(cls, full_name):
        name, surname = full_name.split(" ")
        return cls(surname, name, 0)

    # Альтернативний конструктор для створення об'єкта за прізвищем та ім'ям
    @classmethod
    def create_from_surname_name(cls, surname_name):
        surname, name = surname_name.split(" ")
        return cls(surname, name, 0)
