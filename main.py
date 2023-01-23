from requests import get 

r = get('https://www.cbr-xml-daily.ru/daily_json.js').json()

def convert(cur : int, valute : str) -> str:
    try:
        if r['Valute'][valute]['Nominal'] > 1:
            return cur * r['Valute'][valute]['Value']  / r['Valute'][valute]['Nominal']
        res = cur * r['Valute'][valute]['Value'] 
        return f'{cur} {valute} в рублях будет: {res} руб.'
    except (ValueError, KeyError):
        return 'Ошибка'

while True:
    print(convert(int(input()), input().upper()))