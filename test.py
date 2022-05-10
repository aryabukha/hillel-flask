from sqlalchemy import String, Integer
from sqlalchemy.schema import Column


class Book(Base):
    name = Column(String(50))
    age = Column(Integer)


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age


b1 = Book(name="LOTR", age=15)
b1.save()

sql = """
CREATE TABLE books
(name AS STRING(50),
age AS INTEGER)

INSERT INTO books VALUES ("LOTR", 15)
"""

