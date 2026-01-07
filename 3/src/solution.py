from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
from sqlalchemy.orm import Session

def add_books(engine):
    # Создаем сессию
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    
    try:
        # Создаем первую книгу
        book1 = Book(
            title='To Kill a Mockingbird',
            author='Harper Lee',
            published_year=1960
        )
        
        # Создаем вторую книгу
        book2 = Book(
            title='1984',
            author='George Orwell',
            published_year=1949
        )
        
        # Добавляем книги в сессию
        session.add(book1)
        session.add(book2)
        
        # Коммитим изменения в базу данных
        session.commit()
        
    except Exception as e:
        # В случае ошибки откатываем изменения
        session.rollback()
        raise e
        
    finally:
        # Всегда закрываем сессию
        session.close()
# END
