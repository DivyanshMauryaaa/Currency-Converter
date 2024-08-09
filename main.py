from currency_converter import CurrencyConverter

while True:
    #initialising converter
    converter = CurrencyConverter()

    #Getting Details
    current_currency = input("Your current currency (INR/USD/CAD etc...): ") #Getting current currency
    convert_currency = input("Which currency you want your amount to be converted into(INR/USD/CAD etc...): ") #Getting currency the amount is to be converted into
    current_currency_amount = float(input("Enter the amount in your current currency: ")) #Getting Main Amount

    #Converting Currency
    convertedCurrency = converter.convert(current_currency_amount, current_currency, convert_currency)
    print(f"{convertedCurrency:.2f} {convert_currency}")

    confirmation = input("Want to do more calculation? [y/n]: ")

    if confirmation == "y":
        continue
    elif confirmation == "n":
        break

