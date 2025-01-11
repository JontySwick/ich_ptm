# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади прямоугольника и calculate_perimeter() для вычисления периметра прямоугольника.
# Переопределить методы __str__, __repr__.
# Затем создайте экземпляр класса Rectangle и выведите информацию о нем, его площадь и периметр.

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.height

    def __str__(self):
        return f'{self.__class__.__name__}(width: {self.width}, height: {self.height})'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(width: {self.width}, height: {self.height}, '
                f'area: {self.calculate_area()}, perimeter: {self.calculate_perimeter()})'
                )


print(repr(Rectangle(12.3, 4.56)))


# 2. Создайте класс BankAccount для представления банковского счета.
# Класс должен иметь атрибуты account_number (номер счета) и balance (баланс),
# а также методы deposit() для внесения денег на счет и withdraw() для снятия денег со счета.
# Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег.
# Выведите оставшийся баланс.
# Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля.
# В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение "Недостаточно средств на счете".


class BankAccount:
    list_accounts = {}
    reserved_accounts = []

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposits(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

        return self.balance

    def withdraw(self, amount):
        new_amount = self.balance - amount
        if 0 <= new_amount < self.balance:
            self.balance = new_amount
            return self.balance
        else:
            return "Недостаточно средств на счете"


account = BankAccount('1234567890')
print(account.deposits(300))
print(account.withdraw(100))
print(account.withdraw(300))
