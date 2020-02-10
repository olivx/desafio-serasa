import json
import shelve
from .settings import PATH_DATA_FILE, DATABASE
from .decorators import validate_decorator, load_data_from_file
from collections import defaultdict
from .violations import low_score, minimum_installments , compromised_income
from .consumer import Consumer
from datetime import datetime


def request_transaction(**kwargs):
    base_values = {
        "id" : 5,
        "consumer_id": 10, 
        "score": 100, 
        "income": 4000, 
        "requested_value": 10000,
        "installments": 15, 
        "time": f'{datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z'
    }
    base_values.update(**kwargs)
    DATABASE.append(base_values)


@validate_decorator(violatios=[low_score, minimum_installments, compromised_income])
def validate(consumer, transaction=None):
    return transaction

@load_data_from_file
def show_validate_data(): 
    for index, transaction in enumerate(DATABASE, start=1):
        transaction.update({'id': index})
        print(validate(Consumer(**transaction)))







