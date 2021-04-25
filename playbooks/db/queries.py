from sqlalchemy import create_engine, and_

DB_FILE_NAME = 'test.db'

# create_engine - создание подключения к базе.
e = create_engine(f'sqlite:///{DB_FILE_NAME}')
e.execute("""
create table if not exists student (
id integer primary key autoincrement,
first_name varchar,
last_name varchar
)
""")

# .execute - выполнение запроса к базе
# добавление записей
e.execute("""
insert into student (first_name, last_name)
values ('Alex', 'Johnson')
""")

# получение данных
result = e.execute("""select * from student""")
for user in result:
    print(user)

# транзакция - осуществление одного или нескольких изменений базы данных
# в рамках транзакции либо выполяются все действия, либо все не выполняются (в случае если была ошибка хотя бы в одном)
conn = e.connect()
trans = conn.begin()
conn.execute(
    """
    insert into student (first_name, last_name)
    values (:first_name, :last_name)
    """, first_name='Pasha', last_name='Ivanov'
)
# .commit - применение транзакции
# .rollback - отмена транзакции
trans.commit()
conn.close()

# ORM - Object related model
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(f'sqlite:///{DB_FILE_NAME}', echo=True)

# декларативное описание модели (применяется почти всегда)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname


Base.metadata.create_all(engine)

# Session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

session.add(Person('Alex', 'Johnson'))
session.add_all([Person('Petk', 'Vasiliev'), Person('Ann', 'Ivanova')])
session.commit()

# cоздание запроса Query
person = session.query(Person).filter_by(first_name='Alex').first()
person = session.query(Person).filter(Person.first_name == 'Alex').first()
person = session.query(Person).filter(and_(
    Person.first_name == 'Alex',
    Person.last_name == 'Johnson',
)).all()
