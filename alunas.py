nome = input('Digite o nome da aluna: ')
idade = int(input("Digite a idade da aluna:"))
altura = float(input("Digite a altura da aluna"))
hobbies = input("Digite os hobbies das alunas separados por virgula")
hobbies1 = hobbies.split(',')
endereco_rua = input("Digite o nome da rua da aluna: ")
endereco_numero = int(input("Digite o numero da casa da aluna: "))
endereco_cidade = input("Digite a cidade da aluna: ")
endereco = (endereco_rua, endereco_numero, endereco_cidade)
email = input("Digite o email da aluna: ")
telefone =input("Digite o telefone da aluna: ")
contato = {"email": email, "telefone": telefone}


print("Olá, segue informações sobre a aluna:\n ")
print("Nome:",nome)
print("idade:",idade)
print("altura:",altura)
print("hobbies:",hobbies)
print("hobbies1:",hobbies1)
print("endereco:",endereco)
print("contato:",contato)
