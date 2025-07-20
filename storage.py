import json
import globals

def load_save_json():
    with open('./data.json', 'r') as file:
        data = json.load(file)
    globals.total_del = data['emails_deleted']
    globals.total_size = data['bytes_deleted']

def save_progress():
    with open('./data.json', 'w') as file:
        json.dump({
            'emails_deleted': globals.total_del,
            'bytes_deleted': globals.total_size
        }, file)
        file.flush()