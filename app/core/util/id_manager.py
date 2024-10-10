import random
import json

from .singelton_meta import SingletonMeta


class UniqueID(metaclass=SingletonMeta):
    def __init__(self):
        if hasattr(self, '__initialized') and self.__initialized:
            return
        self.table = {
            'student': {},
            'teacher': {},
            'course': {}
        }
        self.__initialized = True     

    def generate_unique_id(self, num_digits: int, id_type: str):
        lower_bound = 10**(num_digits - 1)
        upper_bound = 10**num_digits - 1
        while True:
            random_id = random.randint(lower_bound, upper_bound)
            if random_id not in self.table[id_type]:  
                return random_id

    def insert(self, num_digits: int, id_type: str):
        random_id = self.generate_unique_id(num_digits, id_type)
        return random_id
    
    def save_to_dict(self, value: str, random_id: int, id_type: str):
        self.table[id_type][random_id] = value
    
    def delete(self, key: int, id_type: str):
        return self.table[id_type].pop(key, None)
    
    def get_table(self, id_type: str):
        return self.table[id_type]
    
    
    def find_by_id(self, id_type: str, id: int):
        return self.table.get(id_type, {}).get(id, None)


    def update_name(self, id_type: str, id: int, new_name: str):
        if self.find_by_id(id_type, id) is not None:
            self.table[id_type][id] = new_name
            return True
        return False

    
    def load_from_file(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.table = data.get('table', self.table)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading file: {e}")

    def save_to_file(self, file_path: str):
        try: 
            with open(file_path, 'w') as file:
                json.dump({
                    'table': self.table,
                }, file, indent=4)
        except IOError as e:
            print(f"Error writing JSON file: {e}")

unique_id_instance = UniqueID()

async def get_unique_id_instance():       
    return unique_id_instance