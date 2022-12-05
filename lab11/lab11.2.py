import json

def main():
    with open('tgreangle.json', 'r') as json_file:
        tr = json.load(json_file)
        
    if tr['A'] > tr['B'] + tr['C']:
        print('треугольник не существует')
        return 0
    elif tr['B'] > tr['A'] + tr['C']:
        print('треугольник не существует')
        return 0
    elif tr['C'] > tr['A'] + tr['B']:
        print('треугольник не существует')
        return 0
    else:
        print('треугольник существует')
        
    if tr['A'] > tr['B'] and tr['A'] > tr['C']:
        if tr['A'] * tr['A'] == (tr['B'] * tr['B']) + (tr['C'] * tr['C']):
            print('прямоугольный')
        elif tr['A'] * tr['A'] < (tr['B'] * tr['B']) + (tr['C'] * tr['C']):
            print('остроугольный')
        elif tr['A'] * tr['A'] > (tr['B'] * tr['B']) + (tr['C'] * tr['C']):
            print('тупоугольный')
    elif tr['B'] > tr['A'] and tr['B'] > tr['C']:
        if tr['B'] * tr['B'] == (tr['A'] * tr['A']) + (tr['C'] * tr['C']):
            print('прямоугольный')
        elif tr['B'] * tr['B'] < (tr['A'] * tr['A']) + (tr['C'] * tr['C']):
            print('остроугольный')
        elif tr['B'] * tr['B'] > (tr['A'] * tr['A']) + (tr['C'] * tr['C']):
            print('тупоугольный')
    else:
        if tr['C'] * tr['C'] == (tr['B'] * tr['B']) + (tr['A'] * tr['A']):
            print('прямоугольный')
        elif tr['C'] * tr['C'] < (tr['B'] * tr['B']) + (tr['A'] * tr['A']):
            print('остроугольный')
        elif tr['C'] * tr['C'] > (tr['B'] * tr['B']) + (tr['A'] * tr['A']):
            print('тупоугольный')
    
main()