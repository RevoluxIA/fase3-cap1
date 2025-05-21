from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Reading(Base):
    __tablename__ = 'readings'
    
    id = Column(Integer, primary_key=True, index=True)
    humidity = Column(Float)
    temperature = Column(Float)
    pH = Column(Float)
    ldr_value = Column(Integer)
    pump_status = Column(String)
    nutrient_added = Column(String, nullable=True)

class BootInfo(Base):
    __tablename__ = 'boot_info'
    
    id = Column(Integer, primary_key=True, index=True)
    ets = Column(String)
    rst = Column(String)
    boot = Column(String)
    configsip = Column(Integer)
    SPIWP = Column(String)
    clk_drv = Column(String)
    q_drv = Column(String)
    d_drv = Column(String)
    cs0_drv = Column(String)
    hd_drv = Column(String)
    wp_drv = Column(String)
    mode = Column(String)
    clock_div = Column(Integer)
    load_1_address = Column(String)
    load_1_len = Column(Integer)
    load_2_address = Column(String)
    load_2_len = Column(Integer)
    ho = Column(Integer)
    tail = Column(Integer)
    room = Column(Integer)
    load_3_address = Column(String)
    load_3_len = Column(Integer)
    entry = Column(String)