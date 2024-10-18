print('#####################################################')
print('Exercicio 1 => NÚMERO POSITIVO OU NEGATIVO:')
numero = int(input('Digite 1 número:'))
print('o Número DIGITADO é:',numero)
if numero > 0:
    print('o Número é POSITIVO')
elif numero < 0:
     print('o Número é NEGATIVO')
elif numero == 0:
     print('o Número é IGUAL a 0')

print('#####################################################')
print('Exercicio 2 => MAIORIDADE: ')
idade = int(input('Digite a idade:'))
if idade >= 18:
    print('É Maior de idade !!!')
else:
    print('É Menor de idade !!!')

print('#####################################################')
print('Exercicio 3 => PAR OU IMPAR: ')
numero = int(input('Digite um Número: '))
if numero % 2 == 0:
    print('O Número é PAR !!!')
else:
    print('O Número é IMPAR !!!')

print('#####################################################')
print('Exercicio 4 => NÚMERO MAIOR: ')
numero1 = int(input('Digite o Número 1: '))
numero2 = int(input('Digite o Número 2: '))
if numero1 > numero2:
    print('O NÚMERO 1 É MAIOR que o NÚMERO 2')
else:
    print('O NÚMERO 1 É MENOR que o NÚMERO 2')

print('#####################################################')
print('Exercicio 5 => DESCONTO DE COMPRA: ')
valor = float(input('Digite o Valor de uma compra: '))
if valor > 100:
    desconto = valor - (valor * 0.10)
    print(f'Valor da compra com deconto:{desconto: .2f}')
else:
    print('Valor da compra não tem deconto')

print('#####################################################')
print('Exercicio 6 => VERIFICAR MULTIPLO: ')
numero = int(input('Digite 1 Número: '))
if numero % 5 == 0:
    print(f'Número "{numero}" É multiplo de 5')
else:
    print(f'Número "{numero}" NÃO É multiplo de 5')

print('#####################################################')
print('Exercicio 7 => CALCULO DE MÉDIA: ')
nota1 = float(input('Digite a NOTA 1: '))
nota2 = float(input('Digite a NOTA 2: '))
nota3 = float(input('Digite a NOTA 3: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f'O Aluno foi APROVADO !!! Nota:{media: .2f}')
else:
    print(f'O Aluno foi REPROVADO !!! Nota:{media: .2f}')

print('#####################################################')
print('Exercicio 8 => SENHA CORRETA: ')
senha1 = input('Digite a SENHA: ')
senha2 = 'python123_EFG'
if senha1 == senha2:
    print('Acesso Permitido !!!')
else:
    print('Senha Incorreta !!!')

print('#####################################################')
print('Exercicio 9 => ENTRADA GRATUITA: ')
idade = int(input('Digite sua IDADE: '))
if idade <= 5 or idade >= 60:
    print('Tem direito a entrada GRATUITA')
else:
    print('Não tem direito a entrada GRATUITA')

print('#####################################################')
print('Exercicio 10 => VERIFICAR NOTA: ')
nota = float(input('Digite uma NOTA entre 0 e 10: '))
if nota >=  0 and nota <= 10:
    print('Valor está entre 0 e 10: ', nota)
else:
    print('Valor INVALIDO !!!')

print('#####################################################')
print('Exercicio 11 => CATEGORIA DE IDADE: ')
idade = int(input('Digite a idade: '))
if idade < 12:
    print('Criança')
elif idade > 12 or idade < 17:
    print('Adolescente')
else:
    print('Adulto')
print('#####################################################')
print('Exercicio 12 => MAIOR DE 3 NÚMEROS: ')
numero1 = int(input('Digite o NÚMERO 1: '))
numero2 = int(input('Digite o NÚMERO 2: '))
numero3 = int(input('Digite o NÚMERO 3: '))
maior = numero1
if numero2 > maior and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print(f'O Maior valor é:{maior}')

print('#####################################################')
print('Exercicio 13 => DIVISÃO SEGURA: ')
numero1 = int(input('Digite o Número 1 : '))
numero2 = int(input('Digite o Número 2 : '))
if numero2 == 0:
    print('Divisao não é possivel', numero2)
divisao = numero1 / numero2
print(f'A Divisao de:"{numero1}" por: "{numero2}" é: =>{divisao}')

print('#####################################################')
print('Exercicio 14 => NÚMERO DENTRO DO INTERVALO: ')
numero = int(input('Digite 1 Número: '))
if numero >= 0 and numero <= 50:
    print(f'O Número "{numero}" ESTÁ entre 0 e 50 ')
else:
    print(f'O Número "{numero}" NÃO ESTÁ entre 0 e 50')

print('#####################################################')
print('Exercicio 15 => APROVADO , RECUPERAÇÃO e REPROVADO: ')
media = float(input('Digite a Média do Aluno: '))

if media >= 7:
    print(f'O Aluno está APROVADO !!! com a MEDIA: "{media}"')
elif media > 5 or media < 7:
    print(f'O Aluno está em RECUPERAÇÃO !!! com a MEDIA: "{media}"')
else:
    print(f'O Aluno está REPROVADO !!! com a MEDIA: "{media}"')

print('#####################################################')
print('Exercicio 16 => CALCULAR O IMC: ')
altura = float(input('Digite a ALTURA: '))
peso = float(input('Digite o PESO em KG: '))
print(f'A Altura Digitada é: {altura: .2f}')
print(f'A Peso  Digitado é: {peso: .2f}')
imc = peso / altura ** 2
if imc < 18.5:
    print(f'O Usuario está ABAIXO DO PESO: {imc: .2f}')
elif imc >= 18.5 and imc < 25:
    print(f'O Usuario está NORMAL: {imc: .2f}')
elif imc >= 25:
    print(f'O Usuario está ACIMA DO PESO: {imc: .2f}') 

print('#####################################################')
print('Exercicio 17 => IDENTIFICAR TRIÂNGULO: ')
lado1 = int(input('Digite 1 lado do TRIÂNGULO: '))
lado2 = int(input('Digite outro lado do TRIÂNGULO: '))
lado3 = int(input('Digite outro lado do TRIÂNGULO: '))
if lado1 == lado2 and lado2 == lado3:
    print('O Triângulo é EQUILATERO: ')
elif lado1 != lado2 and lado2 != lado3:
    print('O Triângulo é ESCALENO: ')
elif lado1 != lado2 and lado2 == lado3:
    print('O Triângulo é ISÓCELES: ')

print('#####################################################')
print('Exercicio 18 => LOGIN E SENHA: ')
usuario = input('Digite o Usuário: ')
senha = input('Digite a SENHA: ')
if usuario == 'admin' and senha == '1234':
    print('Login bem sucedido !!!')
else:
    print('Usuário ou Senha Incorreto !!!')

print('#####################################################')
print('Exercicio 19 => VERIFICAR MAIORIDADE PARA DIRIGIR: ')
idade = int(input('Digite a Idade: '))
maioridade = 18 - idade
if idade >= 18:
    print('Usuário PODE DIRIGIR !!!')
else:
    print(f'Usuário Não PODE DIRIGIR !!! Ainda falta "{maioridade}" para dirigir') 



    