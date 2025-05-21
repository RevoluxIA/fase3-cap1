from sqlalchemy import create_engine, Column, Integer, Float, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///data.db"  # Using SQLite for simplicity

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Reading(Base):
    __tablename__ = 'readings'
    
    id = Column(Integer, Sequence('reading_id_seq'), primary_key=True)
    humidity = Column(Float)
    temperature = Column(Float)
    pH = Column(Float)
    ldr_value = Column(Integer)
    pump_status = Column(String)

def init_db():
    Base.metadata.create_all(engine)

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()