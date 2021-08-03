price = input("How much was the bill?: ")

tip_amt = input("What percentage do you want to add?: ")

tip = float(price.strip()) * float(tip_amt.strip())/100


print("You should leave ${}".format(round(tip)))