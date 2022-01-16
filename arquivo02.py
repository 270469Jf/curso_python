## Opereradores lógicos com IF/ELSE
#nome = input("Qual o seu nome: ")

#if "Vitor" != "Vitor":
#    print("Acertou!")
#else:
#    print("Errou!")

# Operador números
#if 10 != 20:
#    print("Resultado caso verdadeiro")
#else:
#    print("Resultado caso falso")


# == Igualguade
# != Diferença
# > Maior que
# < Menor que
# >= Maior ou igual
# <= Menor ou igual

nome_1 = "Vitor"
nome_2 = "Italo"

numero_1 = 10
numero_2 = 134.34

# Operador and (todas condições iguais)
#if ((nome_1 != nome_2) and (numero_1 == numero_2)):
#    print(True)
#else:
#    print(False)

# Operador or (pelo menos uma deve ser veradeira)
# if ((nome_1 != nome_2) or (numero_1 == numero_2)):
#     print(True)
# else:
#     print(False)

# Estrutura IF/ELIF/ELSE
# if nome_1 == nome_2:
#     print(10)
# elif numero_1 == numero_2:
#     print(20)
# else:
#     print(False)

# Operadores juntos
# if (nome_1 != nome_2 or numero_1 == numero_2) and numero_1 == numero_2:
#     print(True)
# else:
#     print(False)


## WHILE (cuidado com loops infinitos)
nome = "Gui"
tentativas = 3
#while tentativas > 0:
#    nome = input("Qual o código: ")
#    tentativas = tentativas - 1

## FOR
#soma_letras = ""
#for letra in "Vitor":
#    print(letra)
#    soma_letras += letra
#
#print(soma_letras)

#soma_notas = 0
#for nota in [1, 2, 3, 5, 6, 7, 8]:
#    print(nota)
#    soma_notas = soma_notas + nota
#
#print(soma_notas)

## FOR + IF
def valida_nota(nota):
    if nota >= 8:
        return "Gabaritou"
    elif nota >=5:
        return "Cabeçudo"
    else:
        return "Estude mais"

def validacao_notas(lista_notas):
    retornos = []
    for nota in lista_notas:
        resposta = valida_nota(nota)
        retornos.append(resposta)

# lista_notas_b1 = [1, 2, 3, 5, 6, 7, 8]
# resultado_b1 = validacao_notas(lista_notas_b1)
# print(resultado_b1)

# lista_notas_b2 = [2, 3, 4, 6, 7, 8, 9]
# resultado_b2 = validacao_notas(lista_notas_b2)
# print(resultado_b2)

#nota = 4
#resultado = valida_nota(nota)
#print(resultado)


## Dicionários
alunos = { "aluno_1": {
               "nome": "Italo",
               "sobrenome": "Medeiros",
               "localizacao": "Ribeirão",
               "notas": [1, 2, 3, 4, 5, 6, 7, 8],
               "idade": 23
    },
            "aluno_2": {
                    "nome": "Guilherme",
                    "sobrenome": "Canechia",
                    "localizacao": "SP",
                    "notas": [1, 2, 3, 4, 5, 6, 7, 8],
                    "idade": 23
            },
            "aluno_3": {
                    "nome": "Ellen",
                    "sobrenome": "Freitas",
                    "localizacao": {
                        "Cidade": "RJ",
                        "Bairro": "Bangu"
                    },
                    "notas": [1, 2, 3, 4, 5, 6, 7, 8],
                    "idade": 23
            },
}

# for chave, valor in alunos.items():
#     for sub_chave, sub_valor in valor.items():
#         print(sub_chave)
#         print(sub_valor)
#         input()

lista_nomes = []
lista_notas = []

for chave in alunos:
    nome = alunos[chave]["nome"]
    print("Notas do aluno: ", nome)
    #lista_nomes.append(nome)

    for nota in alunos[chave]["notas"]:
        resultado = valida_nota(nota)
        print(nota, nota, nota, nota, nota , nota)
    #notas = alunos[chave]["notas"]
    #lista_notas.append(notas)
    input()
