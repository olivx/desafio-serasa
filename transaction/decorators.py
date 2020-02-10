from collections import defaultdict
from .settings import DATABASE, PATH_DATA_FILE
import json

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
            DATABASE.append(data['transaction'])
        return func()
    return wrapper
