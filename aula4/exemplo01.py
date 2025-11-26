# # Verificação de mair idade !
# idade =  int (input("Informe sua Idade: "))

# if idade >= 18: 
#     print('você é maior de idade')
# else:
#     print('você menor de idade ')


# testatndo mais condições 
# teste de pontos

# pontos = int (input('quantos pontos ?'))

# if pontos >= 100:
#     print('nivel maximo!')
# elif pontos >= 50:
#     print('nivel bom !')
# elif pontos >= 25:
#     print('Pontuação ruim!')

# else:
#     print('você precisa melhorar')

# verificação de login 

# usuario = input ('informe o usuario ')
# senha = input('informe a senha ! ')

# if usuario == ' adimin' and senha == ' 1234':
#     print('O Pai Ta On ')

# else:
#     print('Usuario invalido!')
    
# Condição para bride 

# compra = float(input('valor da compra '))
# cliente10 = input( 'cliente 10 ? [S/N]').lower ()

# if compra >= 1000 or cliente10 == 's':
#     print('voce tem direito a brinde')
# else:
#     print ('talvez na proxima!')

nota = float(input('informe a nota '))
frequencia = float(input('informe a frequencia'))

if nota >= 7 :
    if frequencia >= 75 :
        print('Aprovado')
    else :
        print('boa nota , mas reprovado por falta')
else :
    print('reprovado')        