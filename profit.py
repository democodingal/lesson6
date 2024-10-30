cost=float(input("enter the cost price of oranges"))
selling=float(input("enter the selling price"))
if selling>cost:
    profit= selling - cost
    print("profit is=   ", profit)
else:
    print("no profit")