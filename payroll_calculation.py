from sys import argv

working, bet, premium = argv
result = int(working) * int(bet) + int(premium)

print('Выработанное время - ', working)
print('Ставка - ', bet)
print('Премия - ', premium)
print('Зарплата - ', result)
