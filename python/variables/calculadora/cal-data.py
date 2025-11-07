from funcion import interar
n1 = input("numero 1: ")
n2 = input("numero 2: ")
op = input("operador: ")



if op == "-":
    if n1[0] =="[" and  n1[-1] == "]":
        
        print("\n",int(n1[1]) - int (n2))
        print(int(n1[3]) -  int (n2), "\n")
    interar.hiterar_conjunto (n1, n2)
        
    # print (int(n1) - int(n2))  
elif op =="+" :
    print (int(n1) + int(n2))
elif op  == "*":
    print (int(n1)) * int(n2)
elif op == "/":
    print (int(n1) / int(n2))
else:
    print("error")

