import random

class MySuperClass:
    """Тестовий клас, описує студента."""
    var_lover_case = "Це проста класова змінна"
    COLLEGE_NAME = "Національний університет"
    total_students = 0
    total_marks = 0
    student_id = "Невизначений"

    def __init__(self, surname: str, name: str, group: str = None, hobby: str = None):
        """Ініціалізуємо об'єкт студента з випадковими оцінками і рейтингом коледжу."""
        print("Викликаємо __init__")
        self.__surname = surname
        self.__name = name
        self.mark = random.randint(1, 5)  # Випадкова оцінка від 1 до 5
        self.group = group
        self._age = None
        self._scholarship = None
        self.hobby = hobby
        self.college_raiting = random.randint(1, 5)

        # Оновлюємо статистику
        MySuperClass.total_students += 1
        MySuperClass.total_marks += self.mark
        print(f"Відрахували студента: {self.__name} {self.__surname}")

    def __del__(self):
        """Викликається при видаленні об'єкта. Зменшує кількість студентів."""
        MySuperClass.total_students -= 1
        MySuperClass.total_marks -= self.mark
        print("Перазаписали класову змінну: Це проста класова змінна")

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
    
    def calculate_scholarship_after_session(self, rating: int):
        """Метод для обчислення стипендії після сесії, в залежності від оцінки."""
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
            f"Хобі: {self.hobby if self.hobby else 'Немає хобі'}\n"
            f"Рейтинг коледжу: {self.college_raiting}"
        )

    @property
    def name(self):
        """Ім'я студента."""
        return self.__name

    @property
    def surname(self):
        """Прізвище студента."""
        return self.__surname

    @classmethod
    def create_from_name_surname(cls, full_name):
        name, surname = full_name.split(" ")
        return cls(surname, name, 0)

    @classmethod
    def create_from_surname_name(cls, surname_name):
        surname, name = surname_name.split(" ")
        return cls(surname, name, 0)

    def function_in_class(self):
        """Метод для демонстрації виклику через об'єкт."""
        print(f"{self.name} {self.surname} викликає метод через об'єкт.")

    def _protected_method_in_class(self):
        """Захищений метод для демонстрації."""
        print("Це захищений метод, доступний тільки в класі або його підкласах.")

    @staticmethod
    def hobbi(hobby=None):
        """Метод для виведення хобі студента."""
        if hobby:
            print(f"Моє хобі: {hobby}")
        else:
            print("Студент не вказав хобі.")

