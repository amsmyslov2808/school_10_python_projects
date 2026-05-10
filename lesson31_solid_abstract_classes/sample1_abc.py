from abc import ABC, abstractmethod


# Абстрактный класс / интерфейс
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


# Конкретная реализация 1
class BankCardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата картой на сумму {amount} рублей")

    def refund(self, amount):
        print(f"Возврат на карту: {amount} рублей")


# Конкретная реализация 2
class CashPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата наличными на сумму {amount} рублей")

    def refund(self, amount):
        print(f"Возврат наличными: {amount} рублей")


# Конкретная реализация 3
class CryptoPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата криптовалютой на сумму {amount} рублей")

    def refund(self, amount):
        print(f"Возврат криптовалютой: {amount} рублей")


def process_payment(payment_system, amount):
    payment_system.pay(amount)


def process_refund(payment_system, amount):
    payment_system.refund(amount)


card = BankCardPayment()
cash = CashPayment()
crypto = CryptoPayment()

payments = [card, cash, crypto]

for payment in payments:
    process_payment(payment, 1000)

print()

for payment in payments:
    process_refund(payment, 500)
