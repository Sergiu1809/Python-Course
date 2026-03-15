import requests


def get_price(coin):
    response = requests.get(
        f"https://api.coinbase.com/v2/prices/{coin}-USD/spot")

    if (response.status_code == 200):
        data = response.json()

        price = data['data']['amount']
        currency = data['data']['currency']

        print(f"{coin} price: {price} {currency}")
    elif (response.status_code == 404):
        print("Invalid coin symbol.")
    else:
        print(f"Something went wrong: {response.status_code}")


while True:
    user_input = input(
        "What do you want to do?\n"
        "1. Check BTC price\n"
        "2. Check ETH price\n"
        "3. Check any coin\n"
        "4. Exit\n\n"
        "Choose (1-4): ")

    if (user_input == "1"):
        get_price("BTC")
    elif (user_input == "2"):
        get_price("ETH")
    elif (user_input == "3"):
        coin = input("Enter a coin symbol(SOL, DOGE, etc): ").upper()
        get_price(coin)
    elif (user_input == "4"):
        print("Exited the progam.")
        break
    else:
        print("Invalid option, choose between 1-4.")
