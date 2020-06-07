blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def get_transaction_value():
    return float(input('Your Transaction Amount Please: '))

def get_user_choice():
    user_input = print('Your Choice: ')
    return user_input

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)

tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please Choose: ')
    print('1: Add a New Transaction Value: ')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()

    