n1 = input("numero 1: ")
n2 = input("numero 2: ")
op = input("operador: ")

def hiterar_conjunto(n1 , n2):
    for  n in list(n1) :
        if n == "," or n == " " or n == "]" or n == "[":
            continue
        eval(f"{n} + {op} + {n}")
        print(int (n) - int (n2))

if op == "-":
    if n1[0] =="[" and  n1[-1] == "]":
        
        print("\n",int(n1[1]) - int (n2))
        print(int(n1[3]) -  int (n2), "\n")
        hiterar_conjunto(n1, n2)
        
    # print (int(n1) - int(n2))  
elif op =="+" :
    print (int(n1) + int(n2))
elif op  == "*":
    print (int(n1)) * int(n2)
elif op == "/":
    print (int(n1) / int(n2))
else:
    print("error")

