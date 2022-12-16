import csv, re
from var_dump import var_dump

filename = input('Введите название файла: ')
param_filter = input('Введите параметр фильтрации: ')
sort_param = input('Введите параметр сортировки: ')
sort_reverse = input('Обратный порядок сортировки (Да / Нет): ')
interval = list(map(int, input('Введите диапазон вывода: ').split()))
table_columns = input('Введите требуемые столбцы: ')


class Salary:
    """Класс для представления зарплаты

    Attributes:
        vacancy : Параметры
    """
    def __init__(self, vacancy):
        """Инициализирует объект Salary, заполняет необходимые поля

        Args:
            vacancy : Параметры
        """
        self.salary_from = vacancy['salary_from']
        self.salary_to = vacancy['salary_to']
        self.salary_gross = vacancy['salary_gross']
        self.salary_currency = vacancy['salary_currency']


class Vacancy:
    """Класс для конвертирования данных в нормальный вид

    Attributes:
        vacancy : Параметры
    """
    def __init__(self, vacancy):
        """Инициализирует объект Vacancy, заполняет необходимые поля

        Args:
            vacancy : Параметры
        """
        self.name = vacancy['name']
        self.description = vacancy['description']
        self.key_skills = vacancy['key_skills']
        self.experience_id = vacancy['experience_id']
        self.premium = vacancy['premium']
        self.employer_name = vacancy['employer_name']
        self.salary = Salary(vacancy)
        self.area_name = vacancy['area_name']
        self.published_at = vacancy['published_at']


class DataSet:
    """Класс, содержащий все данные

    Attributes:
        file_name (Any): Название файла
        vacancies_objects (Any): Вакансии
    """
    def __init__(self, file_name, vacancies_objects):
        """Инициализирует объект DataSet

        Args:
            file_name (Any): Название файла
            vacancies_objects (Any): Вакансии
        """
        self.file_name = file_name
        self.vacancies_objects = vacancies_objects


def pell_HTML(line):
    """Возвращает исправленную строку, при отсутствии совпалений с исходной

    Returns:
        outcome (str): Строка, изменяющаяся при отсутствии совпадений с исходной
    """
    outcome = re.sub(r'<.*?>', '', line)
    outcome = re.sub(r'\s+', ' ', outcome)
    return outcome.strip()


def csv_reader():
    """Считывает файл

    Returns:
        csv_header (list): Лист заголовков
        csv_lines (list or str): Лист значений
    """
    csv_lines = []
    csv_header = []
    file_open = open(filename, encoding='utf-8-sig')
    with file_open:
        file_reader = csv.reader(file_open)
        for line in file_reader:
            if not csv_header:
                csv_header = line
            else:
                my_line = line.copy()
                if all(my_line):
                    csv_lines.append(line)
    if not csv_lines and not csv_header:
        print('Пустой файл')
        exit()
    return csv_header, csv_lines


def get_vacancies():
    """Возвращает массив со значениями

    Returns:
         vacancies_array (list): массив значений
    """
    vacancies_array = []
    for line in lines:
        fill_dict(line, vacancies_array)
    return vacancies_array


def fill_dict(line, vacancies_array):
    """Преобразование над массивом значений

    Args:
        vacancies_array (list): массив значений
    """
    short_dict = {}
    for k, el in zip(header, line):
        if k == 'description':
            el = pell_HTML(el)
        elif k == 'key_skills':
            el = el.split('\n')
        short_dict[k] = el
    vacancies_array.append(Vacancy(short_dict))


def transfer_data():
    """Запуск всех методов
    """
    global header, lines
    header, lines = csv_reader()
    vacancies = get_vacancies()
    data_set = DataSet(filename, vacancies)
    var_dump(data_set)


transfer_data()