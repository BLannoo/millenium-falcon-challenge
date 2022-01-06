from pathlib import Path
from typing import List

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Routes(Base):
    __tablename__ = "routes"
    rowid = Column(Integer, primary_key=True)
    origin = Column(String)
    destination = Column(String)
    travel_time = Column(Integer)


class RoutesRepository:
    def __init__(self, db_path: Path):
        engine = create_engine(f"sqlite:///{db_path}")
        self.__sessionmaker = sessionmaker()
        self.__sessionmaker.configure(bind=engine)

    def get_routes_from(self, origin: str) -> List[Routes]:
        with self.__sessionmaker() as session:
            return session.query(Routes).filter(Routes.origin == origin).all()
