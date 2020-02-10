from collections import defaultdict
from .settings import DATA_LIST, PATH_DATA_FILE, DATABASE_PATH, DATABASE_NAME
import json
import shelve

def validate_decorator(*args, **kwargs):
    violatios = kwargs.get('violatios')
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            consumer = args[0]
            data = defaultdict(list)
            for violation in violatios:
                if violation(consumer):
                    data['violatios'].append(violation.__name__.replace('_', '-'))
            return func(transaction={'transaction': consumer._asdict().get('id'),**data}, *args, **kwargs)
        return wrapper
    return _wrapper


def load_data_from_file(func):
    def wrapper(*args, **kwargs):
        with open(PATH_DATA_FILE) as file_json: 
            transactions = json.load(file_json)
        for index, data in  enumerate(transactions, start=1):
            DATA_LIST.append(data['transaction'])
        return func()
    return wrapper


def sync_data(func):
    def wrapper(*args, **kwargs):
        database =  shelve.open(DATABASE_PATH)
        if 'data' not in database:
            with open(PATH_DATA_FILE) as file_json: 
                transactions = json.load(file_json)
            for index, data in  enumerate(transactions, start=1):
                DATA_LIST.append(data['transaction'])
            database['data'] = DATA_LIST
            func() 
        else: 
            transactions = database['data']
            for index, data in  enumerate(transactions, start=1):
                DATA_LIST.append(data)
            func()
            if DATA_LIST != transactions:
                database['data'] = DATA_LIST 

        database.close()
    return wrapper
