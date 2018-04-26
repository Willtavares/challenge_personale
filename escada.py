num = int(input("Digite um numero: "))
symbol = '#'
for i in range(num):
    print((symbol*(i+1)).rjust(num-1))