import json

def read(path):
    with open(path, 'r') as f:
        return f.read()
    
def read_note_map(path):
    return json.loads(read(path))

NOTE_MAP = read_note_map('note_map.json')