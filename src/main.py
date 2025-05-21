from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from models import Reading
from db import setup_database
from crud import create_reading

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['readings']

def main():
    # Initialize database connection
    engine = create_engine('sqlite:///readings.db')
    setup_database(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Load data from JSON file
    readings = load_data_from_json('data/data.json')

    # Simulate storing data in the database
    for reading in readings:
        create_reading(session, reading)

    session.commit()
    session.close()

if __name__ == '__main__':
    main()