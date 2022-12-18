from unittest import TestCase
from doctests import StaticSalary, currency_to_rub
from doctests import StaticCount

class StaticSalaryTests(TestCase):
    def test_salaries(self):
        self.assertEqual(StaticSalary().salaries, {2007: [], 2008: [], 2009: [], 2010: [], 2011: [], 2012: [], 2013: [], 2014: [], 2015: [], 2016: [], 2017: [], 2018: [], 2019: [], 2020: [], 2021: [], 2022: []})

    def test_vacancy_salaries(self):
        self.assertEqual(StaticSalary().vacancy_salaries, {2007: [], 2008: [], 2009: [], 2010: [], 2011: [], 2012: [], 2013: [], 2014: [], 2015: [], 2016: [], 2017: [], 2018: [], 2019: [], 2020: [], 2021: [], 2022: []})

    def test_check_len_dic(self):
        self.assertEqual(StaticSalary().check_len_dic({}, "Программист"), {2022: 0})

    def test_check_len_dic_long(self):
        self.assertEqual(StaticSalary().check_len_dic({"21": [10, 12, 15], "423": [26, 25, 49], "54": [35, 39, 34]}, "Программист"), {'21': 12, '423': 33, '54': 36})

    def test_vacancy_count(self):
        self.assertEqual(StaticCount().vacancy_count, {2007: 0, 2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0})

    def test_check_int_dic(self):
        self.assertEqual(StaticCount().check_int_dic({}, "Программист"), {2022: 0})

    def test_check_int_dic_long(self):
        self.assertEqual(StaticCount().check_int_dic(currency_to_rub, "Программист"), {'Манаты': 35.68, 'Белорусские рубли': 23.91, 'Евро': 59.9, 'Грузинский лари': 21.74, 'Киргизский сом': 0.76, 'Тенге': 0.13, 'Рубли': 1, 'Гривны': 1.64, 'Доллары': 60.66, 'Узбекский сум': 0.0055})

