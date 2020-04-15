coins = [25,10,5,1]
remainder = 0

def CoinChanger (amount):
    if amount == 0:
        print([])
        return []
    if amount == coins[0]:
        print([coins[0]])
        return [coins[0]]
    if amount > coins[0]:
        remainder = amount - coins[0]
        print(remainder)
        return  [coins[0]]+CoinChanger(remainder)
    if amount < coins[0]:
        coins.pop()
        return CoinChanger(amount)

print(CoinChanger(100))
