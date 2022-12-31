def header(text):
    '''Create a pattern of headers for the system'''
    print()
    print(40*'-')
    print(f'{text:^40}')
    print(40*'-')
    print()


def add(n1, n2):
    '''will sum the variables n1 and n2.'''
    return n1 + n2


def subtract(n1, n2):
    '''will subtract the variables n1 and n2'''
    return n1 - n2


def multiply(n1, n2):
    '''will multiply the variables n1 and n2'''
    return n1 * n2


def divide(n1, n2):
    '''will divide the variables n1 and n2'''
    return n1 / n2


def number_validator(text, pick=''):
    '''Check if the input is a valid number to calculate'''
    while True:
        n = input(text).strip()
        try:
            if ',' in n:
                n = n.replace(',', '.')
            float(n)
            if pick == '/' and float(n) <= 0:
                print("❌ You can't divide any number by zero or a negative number\n")
                continue
            break
        except:
            print(f"❌ '{n}' is not a valid number.\n")
    return float(n)
