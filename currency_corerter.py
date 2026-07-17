import requests

API_KEY = "AuBjvIDWOpgzmjYXDyhEI3IP4faMHx4H"
valid_currencies = [
    "USD", "EUR", "EGP", "SAR",
    "AED", "GBP", "JPY", "CAD"
]

print("=== Currency Converter ===")

while True:
    base = input("Enter base currency (USD, EUR, EGP): ").upper()
    target = input("Enter target currency: ").upper()
    amount = float(input("Enter amount: "))

    if base not in valid_currencies:
        print("Invalid base currency!")
        continue

    if target not in valid_currencies:
        print("Invalid target currency!")
        continue

    if amount <= 0:
        print("Amount must be greater than 0.")
        continue

    url = (
        f"https://api.apilayer.com/fixer/convert"
        f"?to={target}&from={base}&amount={amount}"
    )

    headers = {
        "apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data.get("success", False):
            result = data["result"]
            print(f"\n{amount} {base} = {result:.2f} {target}")

        else:
            print("\nConversion failed!")
            print(data["error"]["info"])

    else:
        print("\nAPI request failed!")
        print(response.text)

    again = input("\nTry again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using Currency Converter!")
        break