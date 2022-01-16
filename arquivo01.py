## Tipos de variáveis
variavel = "Aula"

var_str = "Texto" # str
var_int = 10 # int
var_float = 10.01 # float 

var_texto_1 = "Batata"
var_texto_2 = " Controle" # Variável com espaço em branco
var_int_1 = str(10) # "cast" de variável: transformação do tipo "int" para "str"
var_texto_3 = var_texto_1 + var_texto_2 + var_int_1 # Soma de variáveis str (apenas str)

## Interação com o usuário (input sempre retorna str)

#var_interacao = input("Qual o seu nome: ")

#primero_numero = input("Digite o primeiro número: ")
#segundo_numero = input("Digite o segundo número: ")

#print(primero_numero + segundo_numero)

#primero_numero_int = float(primero_numero)
#segundo_numero_int = float(segundo_numero)

#print(primero_numero_int + segundo_numero_int) 

## Formatação de Strings

var_texto_4 = "COD-1298391283921-INT"

#print(var_texto_1[4:-4])

str_elimina_primeiros = var_texto_4[4:]
str_apenas_os_primeiros = var_texto_4[:4]
str_elimina_ultimos = var_texto_4[:-4]
str_conteudo_do_meio = var_texto_4[4:-4]

var_texto_5 = "10"
var_texto_6 = "ESSETEXTO"

#print(var_texto_5.upper())
#print(var_texto_6.lower())

#print(var_texto_5.capitalize())
#print(var_texto_5.isdigit())

#print(type(var_texto_5))

## Aspas triplas (texto com espaçamento)
var_text = """
Consigo
Fazer\n
coisa
assim """

#print(var_text)

## Operadores Aritméticos

numero_1 = 10
numero_2 = 20

soma_numeros = numero_1 + numero_2 # Soma
sub_num = numero_1 - numero_2 # Subtração
mult_num = numero_1 * numero_2 # Multiplicação
div_num = numero_2 / numero_1 # Divisão

#print(soma_numeros)
#print(sub_num)
#print(mult_num)
#print(div_num*mult_num + soma_numeros - numero_2)

var_texto_7 = "tuts "

#print(var_texto_7 * 10)

## Tipos extras de variáveis

operadores = [soma_numeros, sub_num, mult_num, div_num, 10, "Outro texto"]

notas_aluno = [1, 2, 3, 4, 6, 7, 8]

notas_aluno.append("esse text"+"outro texto")
notas_aluno.append(10.10+90)
notas_aluno.append(var_texto_7*10)

print(notas_aluno)
