import decimal

import factory
from playbooks.serialization.account import Account


class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    name = 'Alex'
    age = 25
    balance = decimal.Decimal(100)
