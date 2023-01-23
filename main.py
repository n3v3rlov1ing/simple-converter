from requests import get 

r = get('https://www.cbr-xml-daily.ru/daily_json.js').json()
def convert(cur : int, valute : str) -> int:
    res = cur * r['Valute'][valute]['Value'] 
    return res

print(convert(int(input()), input().upper()))
