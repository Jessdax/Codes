def get_total_income(transactions):
    return sum(t['amount'] for t in transactions if t['type'] == 'income')

def get_total_expenses(transactions):
    return sum(t['amount'] for t in transactions if t['type'] == 'expense')
    
def get_balance(transactions):
    return get_total_income(transactions) - get_total_expenses(transactions)
