import os 
from .consumer import Consumer, transaction_validate
from .utils import load_data, DATABASE
import argparse

def request_transaction(*args, **kwargs): 
    base_values = {
        "id" : 5,
        "consumer_id": 10, 
        "score": 100, 
        "income": 4000, 
        "requested_value": 10000,
        "installments": 15, 
        "time": "2019-03-13T10:00:00.000Z"
        }

    base_values.update(kwargs)
    consumer = Consumer(**base_values)
    print("args", args, "kwargs", dict(consumer._asdict()))

def load_transactions_from_file():
    if len(DATABASE) == 0:
        for data in load_data(): 
            instance = Consumer(**data['transaction'])   
            DATABASE.append(transaction_validate(instance))
    
def show():
    for data in DATABASE:
        print(data)

def main():
    
    load_transactions_from_file()
    show()

    request_transaction('create', score=2000, installments=20)

   
if __name__ == "__main__":

    # main()