import decimal

import mock
import pytest
import requests

from playbooks.serialization.account import Account


def test_account_created():
    # Arrange
    import decimal
    from playbooks.serialization.account import Account

    # Act
    account = Account('Alex', 25, decimal.Decimal(100))

    # Assert
    assert account.name == 'Alex'
    assert account.age == 25
    assert account.balance == decimal.Decimal(100)


def test_account_initialization_invalid_amount():
    # Arrange
    from playbooks.serialization.account import Account

    # Act

    # Assert
    with pytest.raises(AssertionError):
        Account('Alex', 25, 100)


@pytest.mark.parametrize(
    ('name', 'age', 'balance'),
    (
            ('Alex', 25, decimal.Decimal(30)),
            ('John', 35, decimal.Decimal(3000)),
            ('John', 15, decimal.Decimal(115)),
    )
)
def test_account_created_successfully(name, age, balance):
    # Arrange
    from playbooks.serialization.account import Account

    # Act
    account = Account(name, age, balance)

    # Assert
    assert account.name == name
    assert account.age == age
    assert account.balance == balance


@pytest.mark.parametrize(
    ('name', 'age', 'balance'),
    (
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
)
def test_account_creation_fails(name, age, balance):
    # Arrange
    from playbooks.serialization.account import Account

    # Act

    # Assert
    with pytest.raises(AssertionError):
        Account(name, age, balance)


def test_account_serialize(parameterizable_account):
    # Arrange
    from playbooks.serialization.account import serialize

    test_account = parameterizable_account(name='Alex')
    expected_serialized_account = 'Alex 25 100'

    # Act
    result = serialize(test_account)

    # Assert
    assert result == expected_serialized_account


@pytest.mark.parametrize(
    'serialized_account, expected_account',
    [
        ('Alex 25 100', Account('Alex', 25, decimal.Decimal(100))),
        ('John 35 100.50', Account('John', 35, decimal.Decimal(100.50))),
    ]
)
def test_deserialize_account(serialized_account, expected_account):
    # Arrange
    from playbooks.serialization.account import deserialize

    # Act
    result = deserialize(serialized_account)

    # Arrange
    assert result.name == expected_account.name
    assert result.age == expected_account.age
    assert result.balance == expected_account.balance


def test_load_accounts(accounts_file_mock):
    # Arrange
    from playbooks.serialization.account import load_accounts

    expected_accounts = [
        Account('Alex', 25, decimal.Decimal(100)),
        Account('John', 35, decimal.Decimal(100.50)),
    ]

    # Act
    result = load_accounts(accounts_file_mock)

    # Assert
    assert all(
        result_account.name == expected_account.name and
        result_account.age == expected_account.age and
        result_account.balance == expected_account.balance
        for result_account, expected_account
        in zip(result, expected_accounts)
    )


def test_load_accounts_from_api(monkeypatch):
    # Arrange
    from playbooks.serialization.account import load_accounts_from_api

    expected_accounts = [
        Account('Alex', 25, decimal.Decimal(100)),
        Account('John', 35, decimal.Decimal(100.50)),
    ]

    accounts_from_api_mock = mock.Mock()
    accounts_from_api_mock.text = (
        'Alex 25 100\n'
        'John 35 100.50'
    )
    monkeypatch.setattr(requests, 'get', lambda url: accounts_from_api_mock)

    # Act
    result = load_accounts_from_api('https://some.service')

    # Assert
    assert all(
        result_account.name == expected_account.name and
        result_account.age == expected_account.age and
        result_account.balance == expected_account.balance
        for result_account, expected_account
        in zip(result, expected_accounts)
    )


