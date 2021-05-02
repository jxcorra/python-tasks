import decimal

import mock
import pytest


@pytest.fixture()
def account():
    from playbooks.serialization.account import Account

    return Account(
        name='Alex',
        age=25,
        balance=decimal.Decimal(100)
    )


@pytest.fixture()
def parameterizable_account():
    def wrappper(*args, **kwargs):
        name = kwargs.pop('name', 'Alex')
        age = kwargs.pop('age', 25)
        balance = kwargs.pop('balance', decimal.Decimal(100))

        from playbooks.serialization.account import Account

        return Account(name=name, age=age, balance=balance)

    return wrappper


@pytest.fixture()
def sample_accounts():
    return (
        'Alex 25 100',
        'John 35 100.50'
    )


@pytest.fixture()
def accounts_file_mock(sample_accounts):
    accounts_file_mock = mock.MagicMock()
    accounts_file_mock.__iter__.return_value = sample_accounts

    return accounts_file_mock
