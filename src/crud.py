from sqlalchemy import create_engine, Column, Integer, Float, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Reading(Base):
    __tablename__ = 'readings'
    
    id = Column(Integer, Sequence('reading_id_seq'), primary_key=True)
    humidity = Column(Float)
    temperature = Column(Float)
    pH = Column(Float)
    ldr_value = Column(Integer)
    pump_status = Column(String)

def create_reading(session, humidity, temperature, pH, ldr_value, pump_status):
    new_reading = Reading(humidity=humidity, temperature=temperature, pH=pH, ldr_value=ldr_value, pump_status=pump_status)
    session.add(new_reading)
    session.commit()

def get_reading(session, reading_id):
    return session.query(Reading).filter(Reading.id == reading_id).first()

def update_reading(session, reading_id, **kwargs):
    reading = session.query(Reading).filter(Reading.id == reading_id).first()
    for key, value in kwargs.items():
        setattr(reading, key, value)
    session.commit()

def delete_reading(session, reading_id):
    reading = session.query(Reading).filter(Reading.id == reading_id).first()
    session.delete(reading)
    session.commit()