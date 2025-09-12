# tres chicos quiere comprar una consola, pero ha un problema, los precios no están a lado del estantes, ellos quieren comprar la consola mas cara.
# tenemos que solicitar el dinero que tiene cada uno, si hay dos consola con el mismo precio debemos mostrar la dos consola
# tipos de datos: str(), int(), float()
adrian_cash = 13000
nico_cash = 14000 
mauro_cash = 10000

console = {
    # "console": "precio",
    "play 5": "13000", # cadena de texto string
    "xbox360": "9000"
} 

if adrian_cash <=  int(console["play 5"]):
    print(f"adrian podes  compra la console {console["play 5"]}") 
elif adrian_cash <= int(console["xbox360"]) and adrian_cash <= int(console["play 5"]):
  print(f"mauro_cash podes  compra la console xbox360 ${console["xbox360"]}, o te podes comprar play 5 ${console['play 5']}") 

if nico_cash <= int(console["play 5"]):
   print(f"nico_cash podes compra la console play 5 ${console["play 5"]} ")
elif  nico_cash <= int(console["xbox360"]) and nico_cash <= int(console["play 5"]):
    print(f"mauro_cash podes compra la console xbox360 ${console["xbox360"]}, o te podes comprar play 5 ${console["play 5" ]}")