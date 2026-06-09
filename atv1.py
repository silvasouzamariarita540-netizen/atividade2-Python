nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
idade = input("Digite sua idade: ")
plano = input("Digite seu plano (BRONZE, PRATA ou OURO): ").upper()

if plano == "BRONZE":
    print("Filmes disponiveis:")
    print("Forrest Gump")
    print("Toy Story")
    print("O Rei Leão")
    print("Jurassic Park")
    print("Titanic")
    print("Harry Potter e a Pedra Filosofal")
    print("De Volta para o Futuro")

elif plano == "PRATA":
    print("Filmes disponiveis:")
    print("Matrix")
    print("Gladiador")
    print("Os Vingadores")

elif plano == "OURO":
    print("Filmes disponiveis:")
    print("Interestelar")
    print("Clube da Luta")
    print("A Origem")

elif int(idade) >= 18:
    print("Filmes disponiveis:")
    print("O Exorcista")
    print("It — A Coisa")