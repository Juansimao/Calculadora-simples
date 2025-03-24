import math as mat

opcao = int(input(
  
  """Digite um número a seguir para realizar uma operação de dois números:
  
  1 para somar
  2 para subtrair
  3 para dividir
  4 para multiplicar
  5 para raiz quadrada
  6 para potenciação entre eles
        
  \n"""))

numero_1 = float(input("Digite o primeiro número:"))
numero_2 = float(input("Digite o segundo número:"))

match opcao:
  
  case 1:
    print("Vamos somar os dois numeros")
    print(f"Resultado: {numero_1 + numero_2}")

  case 2:
    print("Vamos subtrair os dois numeros")
    print(f"Resultado: {numero_1 - numero_2}")

  case 3:
    print("Vamos dividir os dois numeros")
    while numero_2 == 0:
      numero_2 = float(input("Digite o segundo número:"))
      if numero_2 != 0:
        print(numero_1 / numero_2)    
    
  case 4:
    print(numero_1 * numero_2)

  case 5:
    raiz = numero_1 + numero_2
    print(mat.sqrt(raiz))

  case 6: 
    print(pow(numero_1, numero_2))
  
