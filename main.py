#--Fórmula de Bhaskara--

#a = int(input('Digite o valor de a: '))
#b = int(input('Digite o valor de b: '))
#c = int(input('Digite o valor de c: '))
#d = (b**2) - (4 * a * c)

#if d < 0:
   #print("Não existem raízes reais")
#else:
    #e = d ** 0.5
    #x1 = round(-b + e) / (2 * a)
    #x2 = round(-b - e) / (2 * a)

    #print('O valor de x1 é:', x1, 'e o de x2 é:', x2)

#--Teorema de Pitágoras--

#A=int(input('Digite um número: '))
#B=int(input('Digite um número: '))
#C=(A**2+B**2)**0.5
#print('A hipotenusa é:',C)

#--Fórmula da Velocidade--
#distancia=int(input('Informe a distância percorrida em metros: '))
#tempo=int(input('Informe o tempo gasto em segundos: '))
#velocidade=distancia/tempo
#print('A velocidade é de', velocidade,'m/s')

#--Fórmula da área no quadrado e retângulo--
#lado_quadrado=int(input('Coloque o lado do quadrado: '))
#area_quadrado=lado_quadrado**2
#print('A área do quadrado é de', area_quadrado)

#lado_retangulo=int(input('Coloque o lado do retângulo: '))
#altura_retangulo=int(input('Coloque a altura do retângulo: '))
#area_retangulo=lado_retangulo*altura_retangulo
#print('A área do retângulo é de',area_retangulo)

#--Fórmula da área no triângulo--
#base_triangulo=int(input('Informe a base do triângulo: '))
#altura_triangulo=int(input('Informe a altura do triângulo'))
#area_triangulo=base_triangulo*altura_triangulo/2
#print('A área do triângulo é de',area_triangulo)

#--Fórmula da área do losango--
#diagonal_maior=int(input('Informe a diagonal maior do losango:'))
#diagonal_menor=int(input('Informe a diagonal menor do losango:'))
#area_losango=diagonal_maior*diagonal_menor/2
#if diagonal_maior < diagonal_menor:
   #print('A diagonal maior deve ser maior que a menor')
#elif diagonal_maior == diagonal_menor:
   #print('A diagonal maior e a menor devem ser diferentes')
#else:
   #print('A área do losango é de',area_losango)

 # Calculadora
print('Calculadora funcional')
print('\n \n')

print('Escolha entre "+ , - , * , / , ** , // , % , rq1 , rq2 , pit"')
#Bota o sinal da operação na forma especificada acima, por favor.
print()
print('Escolha entre "Soma , Subtração , Multiplicação , Divisão\nPotência , Divisão total , Resto , Raiz quadrada (rq1 e rq2), Pitágoras\n(Apenas funciona com o simbolo respectivo)"')
#O print acima é meramente para mostrar as opções de operação.
print()


# --Código para dar o valor as variáveis--

operacao=input('Informe a operação desejada: ')
numero_1=int(input('Escolha o primeiro número: '))
numero_2=int(input('Escolha o segundo número: '))

# --Código para fazer as contas--

if operacao == '+': # Soma
   print(numero_1+numero_2)
elif operacao == '-': # Subtração
   print(numero_1-numero_2)
elif operacao == '*': # Multiplicação
   print(numero_1*numero_2)
elif operacao == '/': # Divisão
   print (int(numero_1/numero_2))
elif operacao == '**': # Potência
   print (int(numero_1**numero_2))
elif operacao == '//': # Divisão inteira
   print(numero_1//numero_2)
elif operacao == '%': # Resto
   print(numero_1%numero_2)
elif operacao == 'rq1': # Raiz quadrada do numero_1
   print(numero_1**0.5)
elif operacao == 'rq2': # Raiz quadrada do numero_2
   print(numero_2**0.5)
elif operacao == 'pit': # Hipotenusa de um triângulo retângulo
   print((numero_1**2+numero_2**2)**0.5)
else:
   print('A operação está incorreta, tente novamente por favor!')
# --Fim do código--
   