class MySuperClass:
    """Тестовий клас, описує студента."""

    # Класові змінні
    var_lover_case = "Це проста класова змінна"
    var_upper_case = "ЦЕ КЛАСОВА ЗМІННА З ВЕЛИКИМИ ЛІТЕРАМИ"  # Нова класова змінна
    COLLEGE_NAME = "Це подібне до константи в класі, але можна змінити"
    _protected_var = 1  # Захищена змінна
    __private_var = 2  # Приватна змінна

    # Класові змінні для підрахунку студентів
    total_students = 0
    total_marks = 0

    # Моя нова класова змінна
    student_id = "Студент ID №1"

    def __init__(self, surname: str, name: str, mark: int = 0, group: str = None):
        """Ініціалізуємо об'єкт студента."""
        print("Викликаємо __init__")
        self.__surname = surname  # Приватний атрибут
        self.__name = name  # Приватний атрибут
        
        # Якщо mark == None, використовуємо значення 0
        self.mark = mark if mark is not None else 0  # Перевірка на None, якщо mark == None, присвоюється 0
        
        self.group = group  # Публічний атрибут
        self._age = None  # Захищений атрибут
        self._scholarship = 0  # Студентська стипендія

        # Перезаписуємо класову змінну через екземпляр
        self.var_lover_case = "Перазаписали класову змінну"
        self.var_upper_case = "Нова велика літера для var_upper_case"  # Перезапис класової змінної через екземпляр
        self.student_id = "Новий ідентифікатор студента"  # Перезапис моєї класової змінної

        # Оновлюємо статистику, тільки якщо mark не None
        MySuperClass.total_students += 1
        MySuperClass.total_marks += self.mark  # Тут буде додаватися значення mark, яке гарантовано не None

    def __del__(self):
        """Викликається при видаленні об'єкта. Зменшує кількість студентів."""
        print("Відрахували студента")
        MySuperClass.total_students -= 1
        if self.mark is not None:  # Перевірка, щоб уникнути помилки при відніманні None
            MySuperClass.total_marks -= self.mark  # Віднімаємо оцінку студента тільки, якщо вона є

    @property
    def college_raiting(self):
        """Рейтинг коледжу, розрахований на основі середнього балу студентів."""
        return MySuperClass.total_marks / MySuperClass.total_students if MySuperClass.total_students > 0 else 0

    @property
    def name(self):
        """Властивість для доступу до ім'я студента (тільки для читання)."""
        return self.__name
    
    @property
    def surname(self):
        """Властивість для доступу до прізвища студента (тільки для читання)."""
        return self.__surname

    @property
    def say_hello(self):
        """Тільки для демонстрації, повертає привітання."""
        return f"Привіт {1 + 2}"

    def __repr__(self):
        """Представлення об'єкта у вигляді рядка."""
        return f"MySuperClass(surname={self.surname}, name={self.name}, mark={self.mark})"
    
    def __len__(self):
        """Повертає довжину прізвища студента."""
        return len(self.surname)
    
    def function_in_class(self):
        """Публічний метод для демонстрації."""
        return "Ми викликали публічний метод"

    def _protected_method_in_class(self):
        """Захищений метод, який демонструє доступ до приватних методів."""
        self.__this_is_private()
        return "Доступ до захищеного методу"

    def __this_is_private(self):
        """Приватний метод, не доступний поза класом."""
        print("Це приватний метод!")

    def calculate_scholarship_after_session(self, rating: int):
        """Розраховує стипендію студента на основі оцінки після сесії."""
        if rating == 5:
            self._scholarship = "1800 грн"
            return "Присвоєно підвищену стипендію"
        elif rating == 4:
            self._scholarship = "1400 грн"
            return "Присвоєно звичайну стипендію"
        self._scholarship = 0
        return "Рейтинг занизький для стипендії"
    
    def panishment(self):
        """Приклад методу з гумористичним описом наслідків поганих оцінок."""
        return "Ми прийшли додому і мама нас насварила за погані оцінки"

# Функція в модулі для демонстрації
def function_in_module():
    """Це просто функція, яка може бути реалізована з іншою логікою."""
    pass
