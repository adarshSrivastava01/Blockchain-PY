blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def get_user_input():
    return float(input('Your Transaction Amount Please: '))

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)

add_value(get_user_input())
add_value(get_user_input(),get_last_blockchain_value())
add_value(get_user_input(),get_last_blockchain_value())