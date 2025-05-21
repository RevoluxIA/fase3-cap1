def load_data_from_json(file_path):
    import json
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['readings']

def format_data_for_db(readings):
    formatted_data = []
    for reading in readings:
        formatted_data.append({
            'humidity': reading['humidity'],
            'temperature': reading['temperature'],
            'pH': reading['pH'],
            'ldr_value': reading['ldr_value'],
            'pump_status': reading['pump_status'],
            'nutrient_added': reading.get('nutrient_added', None)
        })
    return formatted_data