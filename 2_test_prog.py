has_good_credit = False
price_house = 1000000
if has_good_credit:
    put_down = 0.1 * price_house
else:
    put_down = 0.2 * price_house

print(f'Down payment of the hpuse: {put_down}')