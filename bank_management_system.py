
print('Welcome to the Ramasedi Central Bank')
Bank_account_balance = 1000
trials = 0

while trials <= 3:
    pin = int(input(' Enter your banking pin '))
    if pin == 1234:
        print('you have entered your pin correctly')
        print('press 1 for balance ')
        print('press 2 to withdraw cash')
        print('press 4 to exit')
        withdrawal_amount = int(input('Enter withdrawal amount '))


    else:
        print('pin is incorrect, please take your card and try again... ')
        break

    service = int(input('how can we help '))

    if service == 1:
        print(f'you have P{Bank_account_balance}.00 in your bank account.')

    elif service == 2:
        print(withdrawal_amount)
    break


while withdrawal_amount > Bank_account_balance:
    print('sorry, you do not have that amount of money in your bank account...')
    break

    if withdrawal_amount <= 0:
        print('please enter a valid amount')

Bank_account_balance -= withdrawal_amount
print(Bank_account_balance)


