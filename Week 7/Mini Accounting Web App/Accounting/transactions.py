def add_transaction(transactions, date, type, amount, description, delete):
    transactions.append({
    "date": date,
    "type": type,
    "amount": amount,
    "description": description,
    "delete": delete

    })
def show_transactions(transactions):
    return transactions
