import json

from collections import defaultdict
def check_violations(*args, **kwargs):
    violatios = kwargs.get('violatios')
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            consumer = args[0]
            data = defaultdict(list)
            for violation in violatios:
                if violation(consumer):
                    data['violatios'].append(violation.__name__.replace('_', '-'))

            return func(transaction={'transaction': 50 , **data}, *args, **kwargs)
        return wrapper
    return _wrapper


def load_data(path='data/data.json'):
  with open(path) as json_file:
    return json.load(json_file)



DATABASE = list()



