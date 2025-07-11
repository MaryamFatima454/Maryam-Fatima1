pkr = float(input("Enter amount in PKR: "))
print("Convert to: USD, EUR, GBP, AED")
currency = input("Enter currency code: ").upper()
rates = {
    "USD": 0.0036,   # 1 PKR = 0.0036 USD
    "EUR": 0.0033,   # 1 PKR = 0.0033 EUR
    "GBP": 0.0028,   # 1 PKR = 0.0028 GBP
    "AED": 0.013     # 1 PKR = 0.013 AED
}
if currency in rates:
    converted = pkr * rates[currency]
    print(f"{pkr} PKR = {converted:.2f} {currency}")
else:
    print("Invalid currency code!")
