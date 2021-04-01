import typing
import decimal


ACCOUNTS_DB_PATH = 'accounts.txt'


class Account:
    def __init__(self, name: str, age: int, balance: decimal.Decimal):
        self.name = name
        self.age = age
        self.balance = balance


def serialize(account: Account) -> str:
    return f'{account.name} {account.age} {account.balance}'


def deserialize(row: str) -> Account:
    name, age_str, balance_str = row.split(' ')

    return Account(name=name, age=int(age_str), balance=decimal.Decimal(balance_str))


Accounts = typing.NewType('Accounts', typing.List[Account])


def load_accounts(from_file: typing.IO) -> typing.Union[Accounts, typing.NoReturn]:
    """
    Returns list of accounts parsed from database.
    Function may throw error while parsing data.
    """
    accounts = []

    for line in from_file:
        account = deserialize(line)
        accounts.append(account)

    return accounts


if __name__ == '__main__':
    with open(ACCOUNTS_DB_PATH, 'r') as f:
        accounts = load_accounts(f)

    print('Active accounts:')
    for account in accounts:
        print(f'User: {account.name} {account.age} years old, Current balance: {account.balance}')
