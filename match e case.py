num1 = int(input('digite um numero:'))
num_2 = int(input('digite outro numero:'))

op = int(input('qual operação você quer fazer?\n1-Soma\n2-subtração\n3-multiplicação\n4-divisão').lower())

match op :
    case 1:
        print(f"adição: {num1+num_2}")
    case 2:
        print(num1 - num_2)
    case 3:
        print(num1 * num_2)
    case 4:
        print(num1 / num_2)




