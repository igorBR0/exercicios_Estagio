from time import sleep


n0 = 0
n1 = 1
r = 0
flag_number =int(input("Digite um numero, e veremos se ele esta contido na sequencia de fibonacchi"))
while(True):
    r = (n0 + n1)
    n0 = n1
    n1 = r
    print(r) 
    if r == flag_number:
        print(f"Numero {flag_number}, pertenci a sequencia de fibonacchi")
        break
    #sleep(1)
        
