from requests import get 

r = get('https://www.cbr-xml-daily.ru/daily_json.js').json()
def convert(cur : int, valute : str) -> int:
    try:
        res = cur * r['Valute'][valute]['Value'] 
        return res
    except (ValueError, KeyError):
        return 'Ошибка'

while True:
    print(convert(int(input()), input().upper()))