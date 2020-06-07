MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}

def get_last_blockchain_value():
    if(len(blockchain) < 1):
        return None
    return blockchain[-1]

def get_transaction_value():
    recipient = input('Enter the name of Recipeint of Transaction: ')
    amount =  float(input('Your Transaction Amount Please: '))
    return (recipient, amount)

def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

def add_transaction(recipient,sender=owner,amount = 1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    # print(hashed_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block,
    'index': len(blockchain),
    'transactions': open_transactions
    }
    blockchain.append(block)
    return True

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-'*20)

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def verify_chain():
    for (index,block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

def get_balance(participant):
    amount_sent = 0
    amount_recieved = 0
    sender = [[each['amount'] for each in block['transactions'] if each['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    sender.append(open_tx_sender)
    recipient = [[each['amount'] for each in block['transactions'] if each['recipient'] == participant] for block in blockchain]
    for each in sender:
        if len(each) > 0:
            amount_sent += each[0]
    for each in recipient:
        if len(each) > 0:
            amount_recieved += each[0]
    return amount_recieved - amount_sent



# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

take_input = True

while take_input:
    print('Please Choose: ')
    print('1: Add a New Transaction Value: ')
    print('2: Mine a New Block: ')
    print('3: Output the blockchain blocks: ')
    print('h: Manipulate the chain: ')
    print('Q: Quit the Program: ')
    user_choice = get_user_choice()
    if user_choice == '1':
        data = get_transaction_value()
        recipient, amount = data
        if add_transaction(recipient, amount=amount):
            print('Added Transaction!')
        else:
            print('Transaction Failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h' or user_choice == 'H':
        if len(blockchain) >= 1:
            blockchain[0] = {
            'previous_hash': '',
            'index': 0,
            'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
        }
    elif user_choice == 'q' or user_choice == 'Q':
        take_input = False
    else:
        print('Input was Invalid! Please Choose again!!!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain! ')
        break
    print(get_balance('Max'))
else:
    print('User left')

