from datetime import datetime
from collections import namedtuple
from .violation import low_score, minimum_installments, compromised_income
from .utils import check_violations

# class Consumer:

#     def __init__(self, consumer_id, score, income, requested_value, installments, time=None, *args, **kwargs):
#         self.score = score
#         self.income = income 
#         self.installments =  installments
#         self.requested_value = requested_value
#         self.consumer_id  = self.__generate_id(consumer_id)
#         self.time = self.__format_datetime(time)

#     def __format_datetime(self, time=None):
#         if not time:
#             return f'{datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]}Z'
#         return time 

#     def __generate_id(self, _id=None):
#         if not _id:
#             return 1
#         return _id

#     def __str__(self): 
#         return f'{self.__dict__}'

#     @validate_decorator(violatios=[low_score, minimum_installments, compromised_income])
#     def validate(self, transaction=None):
#         return transaction


__fields = 'id consumer_id, score, income, requested_value, installments, time'
Consumer = namedtuple('Consumer', __fields)

@check_violations(violatios=[low_score, minimum_installments, compromised_income])
def transaction_validate(consumer, transaction=None):
    return transaction



