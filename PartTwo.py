wallet = 0

while wallet < 75:
    if wallet >= 75:
        break
    else:
        print("The price of the coffee is 75p.")
        print(f"You have", wallet, "in credit.")
        more = int(input("Please insert a coin."))
        wallet += more

wallet = wallet - 75
print("Enjoy your coffee.")
print("Your change is", wallet)