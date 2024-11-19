class MySuperClass:
    """Тестовий клас, описує студента."""

    # Класові змінні
    COLLEGE_NAME = "Національний університет"
    total_students = 0
    total_marks = 0
    student_id = "Невизначений"  # Додано атрибут класу student_id

    def __init__(self, surname: str, name: str, mark: int = 0, group: str = None, hobby: str = None):
        """Ініціалізуємо об'єкт студента."""
        self.__surname = surname  # Приватний атрибут для прізвища
        self.__name = name  # Приватний атрибут для імені
        self.mark = mark  # Публічний атрибут для оцінки
        self.group = group  # Публічний атрибут для групи
        self._age = None  # Захищений атрибут для віку (поки не використовується)
        self._scholarship = None  # Спочатку стипендія не встановлена
        self.hobby = hobby  # Хобі студента (може бути None)

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
        """Оновлює стипендію студента на основі оцінки та додаткових умов."""
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
            f"Стипендія: {self.scholarship}\n"
            f"Хобі: {self.hobby if self.hobby else 'Немає хобі'}"
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

    # Метод для демонстрації виклику через об'єкт
    def function_in_class(self):
        """Метод для демонстрації виклику через об'єкт."""
        print(f"{self.name} {self.surname} викликає метод через об'єкт.")

    # Статичний метод для хобі
    @staticmethod
    def hobbi(hobby=None):
        """Метод для виведення хобі студента."""
        if hobby:
            print(f"Моє хобі: {hobby}")
        else:
            print("Студент не вказав хобі.")
