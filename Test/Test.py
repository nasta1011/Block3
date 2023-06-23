import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_success(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 2) == 7

    def test_pow_success(self):
        assert self.calc.pow(self, 7, 2) == 49

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')