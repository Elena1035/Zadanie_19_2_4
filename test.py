import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_success(self):  #умножение
        assert self.calc.multiply(self, 2, 2)

    def test_division_calculate_success(self):  #деление
        assert self.calc.division(self, 6, 2)

    def test_subtraction_calculate_success(self):  #вычитание
        assert self.calc.subtraction(self, 5, 2)

    def test_adding_calculate_success(self):     #сложение
        assert self.calc.adding(self, 4, 2)

    def teardown(self):
        print("Выполнено")

