def hiterar_conjunto(n1 , n2):
    for n in list(n1):
       if n == "," or n == " " or n == "]" or n == "[":
           continue
       eval(f"{n} + {"op"} + {n}")
       print (int (n) - int (n2))

       