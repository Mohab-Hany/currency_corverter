import requests

API_KEY = "AuBjvIDWOpgzmjYXDyhEI3IP4faMHx4H"

VALID_CURRENCIES = [
    "USD", "EUR", "EGP", "SAR",
    "AED", "GBP", "JPY", "CAD"
]


def show_currencies():
    print("\nAvailable Currencies:")
    print(", ".join(VALID_CURRENCIES))


def get_user_input():
    while True:
        show_currencies()

        base = input("\nEnter base currency: ").strip().upper()
        target = input("Enter target currency: ").strip().upper()

        try:
            amount = float(input("Enter amount: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if base not in VALID_CURRENCIES:
            print("Invalid base currency.")
            continue

        if target not in VALID_CURRENCIES:
            print("Invalid target currency.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return base, target, amount


def convert_currency(base, target, amount):
    url = (
        f"https://api.apilayer.com/fixer/convert"
        f"?to={target}&from={base}&amount={amount}"
    )

    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data.get("success", False):
            result = data["result"]

            print("\n===== Conversion Result =====")
            print(f"{amount} {base} = {result:.2f} {target}")
            print("============================")

        else:
            print("\nConversion failed!")

            if "error" in data:
                print(data["error"].get("info", "Unknown error."))

    except requests.exceptions.Timeout:
        print("\nRequest timed out.")

    except requests.exceptions.ConnectionError:
        print("\nPlease check your internet connection.")

    except requests.exceptions.RequestException as error:
        print(f"\nAn error occurred: {error}")


def play_again():
    answer = input(
        "\nWould you like another conversion? (yes/no): "
    ).strip().lower()

    return answer == "yes"


def main():
    print("===== Currency Converter =====")

    while True:
        base, target, amount = get_user_input()

        convert_currency(base, target, amount)

        if not play_again():
            print("\nThank you for using Currency Converter!")
            break


# Run Program
main()