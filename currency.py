import currencyapicom


def get_currency(currency):
    print("Getting Currency")
    try:
        response = currencyapicom.Client("cur_live_CZ8QPY8bVVNSQm4Q8KQ1c7h1kZhJNyjqikspmMBz")
        # data = response.latest(currency, currencies=["USD", "CAD", "EUR"])
        data = response.currencies()

        # cur = mapCurrency(currencies["data"])
        # cur = currencies.get("data")
        # print("Currencies: "+ cur, end="   ")
        
        
        

        return data
    except Exception as e:
        print(e)
    
    
def mapCurrency(datas):
    arr = []
    for data in datas:
            arr.append(datas[data]["name"])
    return arr



# cur = input("Enter Currency: ")
# amount = input("Enter Amount: ")
# cur = cur.upper()

data =get_currency("USD")
cur = mapCurrency(data["data"])
print(cur)
print(data["data"]["USD"]["name"])
# cur = mapCurrency(json_data["data"])

# print(data)


# converted = float(amount) * mul

# print(f"{amount} {cur} is {converted} CAD")



