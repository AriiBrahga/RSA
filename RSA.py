import random

#RSA ALGORITMO

# Texto Criptografado = (Texto Original ^ E) mod N
# Texto Original = (Texto Criptografado ^ D) mod N

# Criando uma Função para Verificar o Valor de P e Q para Ver se é Primo

def verificaPrimo(valor):
    num = int(valor)
    mult = 0
    primo = bool

    for count in range(2, num):
      if (num % count == 0):
        mult += 1

    if(mult == 0):
        primo = True
    else:
        primo = False
    return primo

#Criando uma função para Criar um numero aleatorio e Chamando a Função para Verificar se é Primo
    
def geraAleatorioPrimo():
  primo = False

  while primo != True:
    num = random.randint(1,1000)

    if verificaPrimo(num) == True:
      primo = True
    else:
      primo = False
  
  return num

# --------------------- MAIN ---------------------
print("----------Algoritmo RSA----------\n\n")

print("A criptografia começa definindo dois números aleatórios (P e Q) que possuem valores primos:")

P = geraAleatorioPrimo()
Q = geraAleatorioPrimo()

print("\tO valor de Q é: ",Q)
print("\tO valor de P é: ",P)

print("\nDepois faz o calculo de dois valores (N e Z) a partir de P e Q")

N = P * Q
Z = (P - 1) * (Q - 1)

print("\tO valor de N é: ",N)
print("\tO valor de Z é: ",Z)

print("\nDefini um valor D que seja primo a Z")

D = 7

print("\tO valor de D é: ",D)

print("\nEncontra o valor E que satisfaz a propriedade")

E = 0

while(E * D) % Z != 1:
  E += 1

print("\tO valor de E é: ", E)

print("\nA partir dos calculos acima, fica definido:\n\tChaves publica: E = {} | N = {}\n\tChaves privada: D = {} | N = {}".format(E, N, D, N))

#Texto

print("\n\n----------Criptografando com RSA----------\n")

texto = input("Digite seu texto para criptografar: " )

#Criando as variaveis para armazenar o texto
cript = []
descript = []

for i in range(len(texto)):
    #letra = texto[i]
    #numLetra = ord(letra)
    #numLetra = pow(numLetra , E)
    #numLetra = numLetra % N
    #cript.append(chr(numLetra))
    
    cript.append(chr((pow(ord(texto[i]), E) % N)))

print("\tO texto criptografado fica: ", cript)

print("\n\n----------Descriptografando com RSA----------\n")

print("Descriptografando o Texto: ")

for i in range(len(cript)):
    #letra = cript[i]   
    #numLetra = ord(letra)
    #numLetra = pow(numLetra , D)   
    #numLetra = numLetra % N
    #descript.append(chr(numLetra))

    descript.append(chr((pow(ord(cript[i]), D) % N)))
print("\tO texto descriptografado fica: " , descript)