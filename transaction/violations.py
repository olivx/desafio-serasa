
def low_score(consumer):
    """ When the score is lower than 200: low-score"""
    if int(consumer.score) < 200:
        return True
    return False 


def minimum_installments(consumer):
    """ When the istallments value is lower than 6 """
    if int(consumer.installments)  <  6 :
        return True
    return False 

def compromised_income(consumer):
    """ When the istallments value is lower than 6 """
    if int(consumer.installments) > 0 and (int(consumer.requested_value) / int(consumer.installments)) < (consumer.income * 0.3) :
        return True
    return False 

# def doubled_transactions(*args, **kwargs):
# """ When happens two transactions in the same 2 minutes: doubled-transactions """
#     pass  