from collections import namedtuple
# from .violations import low_score, compromised_income, minimum_installments


__fields = 'id consumer_id, score, income, requested_value, installments, time'
Consumer = namedtuple('Consumer', __fields)




