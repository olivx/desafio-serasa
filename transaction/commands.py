import sys
from  argparse import ArgumentParser
from .settings import DATABASE_PATH
from .utils import show_validate_data, request_transaction
from .consumer import Consumer
import shelve

class Commands(object):

    def __init__(self):
        parser = ArgumentParser(
            description='Wellcome to  Coding Challenge!!',
            usage='''transactions <command> [<args>]:
            show: show all transaction 
            request: request a new transaction pass values key=value score, income, requested_value, installments 
        ''')
        parser.add_argument('command', help='List all transactions on database')
        # parse_args defaults to [1:] for args
        # get all  line or validation will fail
        args = parser.parse_args(sys.argv[1:2])

        # check command call  
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        # invoke method with same name
        getattr(self, args.command)()

    def show(self):
        parser = ArgumentParser(description='show all transactions requested')
        parser.add_argument('--reset', action='store_true')
        args = parser.parse_args(sys.argv[2:])
        show_validate_data()

    def request(self): 
        parser = ArgumentParser(description="create new request pass values like score=1000")
        parser.add_argument('--fields', action='store')
        args = parser.parse_args(sys.argv[2:])

        data = {}
        for field in args.fields.split(','): 
            key, value = field.split('=')
            data[key] = value
        request_transaction(**data)
        show_validate_data()    

    def reset(self): 
        parser = ArgumentParser(description="create new request pass values like score=1000")
        args = parser.parse_args(sys.argv[2:])
        answer = input('you would like to reset data ? Y/N').lower()
        if answer == 'y':
            dabatase = shelve.open(DATABASE_PATH)
            if 'data' in dabatase: 
                del dabatase['data']
                print(f'reseted transaction applications')
                return 
            print('any data was found in transaction application')

            
  

