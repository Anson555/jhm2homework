priceA = float(input("Enter the price of A: "))
priceB = float(input("Enter the price of B: "))

if priceA < priceB:
    print("A is cheaper than B")
elif priceA > priceB:
    print("A is more expensive than B")
else:
    print("The prices are the same")
