import unittest
import decimal
from playbooks.serialization.account import Account
from playbooks.serialization.tests.factories import AccountFactory


class AccountTestCase(unittest.TestCase):
    def test_account_created(self):
        # Arrange

        # Act
        account = Account('Alex', 25, decimal.Decimal(100))

        # Assert
        self.assertEqual(account.name, 'Alex')
        self.assertEqual(account.age, 25)
        self.assertEqual(account.balance, decimal.Decimal(100))

    def test_account_initialization_invalid_amount(self):
        # Arrange
        from playbooks.serialization.account import Account

        # Act

        # Assert
        self.assertRaises(AssertionError, Account, 'Alex', 25, 100)

    def test_account_created_successfully(self):
        # Arrange
        from playbooks.serialization.account import Account

        cases = (
            ('Alex', 25, decimal.Decimal(30)),
            ('John', 35, decimal.Decimal(3000)),
            ('John', 15, decimal.Decimal(115)),
        )

        # Act
        for name, age, balance in cases:
            account = Account(name, age, balance)

            # Assert
            assert account.name == name
            assert account.age == age
            assert account.balance == balance

    def test_account_creation_fails(self):
        # Arrange
        from playbooks.serialization.account import Account

        cases = (
            ('', 25, decimal.Decimal(30)),
            ('Alex', None, decimal.Decimal(30)),
            ('Alex', 0, decimal.Decimal(30)),
            ('Alex', -10, decimal.Decimal(30)),
            (None, 25, decimal.Decimal(30)),
            (None, 11.5, decimal.Decimal(30)),
            ('Alex', 11.5, decimal.Decimal(30)),
            ('John', 35, None),
            ('John', 15, 'some balance'),
        )

        # Act

        # Assert
        for name, age, balance in cases:
            self.assertRaises(AssertionError, Account, name, age, balance)

    def test_account_serialize(self):
        # Arrange
        from playbooks.serialization.account import serialize

        test_account = AccountFactory(name='Alex')
        expected_serialized_account = 'Alex 25 100'

        # Act
        result = serialize(test_account)

        # Assert
        self.assertEqual(expected_serialized_account, result)

    def test_deserialize_account(self):
        # Arrange
        from playbooks.serialization.account import deserialize

        cases = (
            ('Alex 25 100', Account('Alex', 25, decimal.Decimal(100))),
            ('John 35 100.50', Account('John', 35, decimal.Decimal(100.50))),
        )

        # Act
        for serialized_account, expected_account in cases:
            result = deserialize(serialized_account)

            # Arrange
            assert result.name == expected_account.name
            assert result.age == expected_account.age
            assert result.balance == expected_account.balance
