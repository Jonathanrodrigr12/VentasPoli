import enum


class PaymentType(enum.Enum):
    cash = 1
    credit_card = 2
    debit_card = 3