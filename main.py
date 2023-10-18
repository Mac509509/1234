while True:
    try:
        a = float(input('введите первую сторону: '))
        b = float(input('введите вторую сторону: '))
        c = float(input('введите третью сторону: '))
        s =(a + b + c) / 2
        area =(s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('ответ %0.2f' %area)
        break
    except:
        print("что тупой переделывай")
        print("пиздец")