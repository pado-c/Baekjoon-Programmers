burger = [int(input()) for _ in range(3)]
drink = [int(input()) for _ in range(2)]

set_price = min(burger) + min(drink) - 50
print(set_price)