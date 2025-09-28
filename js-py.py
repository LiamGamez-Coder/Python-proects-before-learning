bill_amount = int(input('What is your bill amount? '))
membership_status = input('Are you a member?')
discount = 0

if (bill_amount >= 1500):
    discount = 10 if membership_status == "Yes" else 7.5
elif (bill_amount >= 600 < 1500):
    discount = 6.5 if membership_status == "Yes" else 3.25


if (discount > 0):
    bill_amount = bill_amount-(discount/100*bill_amount)
    print('Your bill is', bill_amount)
else:
    print('Your bill is', bill_amount)
