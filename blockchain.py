genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'

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

def add_transaction(recipient,sender=owner,amount = 1.0):
    open_transactions.append({
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    })

def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''
    for each in last_block:
        value = last_block[each]
        hashed_block += str(value)

    block = {'previous_hash': hashed_block,
    'index': len(blockchain),
    'transactions': open_transactions
    }
    blockchain.append(block)

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-'*20)

def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
    return is_valid

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
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h' or user_choice == 'H':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q' or user_choice == 'Q':
        take_input = False
    else:
        print('Input was Invalid! Please Choose again!!!')
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print('Invalid Blockchain! ')
    #     break
else:
    print('User left')

