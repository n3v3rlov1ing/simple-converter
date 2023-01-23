from requests import get

from1 = input().upper()
to1 = input().upper()
amount = int(input())
url = f'https://api.exchangerate.host/convert?from={from1}&to={to1}&amount={amount}'
response = get(url)
data = response.json()

print(data['result'])