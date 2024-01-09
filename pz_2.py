while True:
    print('Добро пожаловать в конвертор валют!')
    cash = int(input('Введите сколько вы хотите сконвертировать (в долларах) >> '))
    currency_change = input('Введите валюту для конвертации >> ')
    exchange_rate = float(input('Введите курс валюты для конвертации'))


    if currency_change == 'Рубли':
        rub = cash * exchange_rate
        print(f'{cash} долларов = {rub:.1f} рублей')
    elif currency_change == 'Евро':
        eur = cash * exchange_rate
        print(f'{cash} долларов = {eur:.1f} евро')
    elif currency_change == 'Юани':
        cny = cash * exchange_rate
        print(f'{cash} долларов = {cny:.1f} китайских юаней')
    elif currency_change == 'Дирхамы':
        aed = cash * exchange_rate
        print(f'{cash} долларов = {aed:.1f} дирхам')
    elif currency_change == 'Йена':
        jpy = cash * exchange_rate
        print(f'{cash} долларов = {jpy:.1f} йен')
    else:
        print('Error')
        