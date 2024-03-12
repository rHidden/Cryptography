days = 30
total = 0
penny = 0.01

for i in range(1, days):
    penny*=2
    total += penny
    print('Penny after', i, 'days', float(penny))

print('Total money', float(total))