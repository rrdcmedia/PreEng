#Calculating the discount for the prices higher than 1000 v2.0

price = float(input('Enter the price: '))

if price >= 1000.00:
    discount = float(price) * 0.05
    print('Discount = ', discount)
    print('Final price = ', price - discount)
else:
    print('No Discount')
print('Thank you')

#Ravindu Rasanjana Herath
#E/23/147