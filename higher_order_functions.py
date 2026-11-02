prices = [20, 75, 120, 45, 90]
prices = list(filter(lambda p: p > 50 , prices))
prices = list(map(lambda p: p + 10, prices))
print(prices)