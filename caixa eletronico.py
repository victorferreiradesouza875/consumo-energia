# entrada
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
#verificaçao do cliente
if nome == "Lucas" and senha == "4231":
    saldo = 1500.00
elif nome == "Maria" and senha == "1111":
    saldo = 2000.00
elif nome == "João" and senha == "2222":
    saldo = 1000.00
elif nome == "Ana" and senha == "3333":
    saldo = 2500.00
elif nome == "Pedro" and senha == "4444":
    saldo = 3000.00
elif nome == "Carla" and senha == "5555":
    saldo = 3500.00
elif nome == "Rafael" and senha == "6666":
    saldo = 4000.00
else:
    print("Nome ou senha incorretos. Acesso negado.")
    raise SystemExit
print("Senha correta. Acesso permitido.")
#operaçao
if saldo > 0:
    print(f"Seu saldo inicial é: R$ {saldo:.2f}")

    saque = float(input("Digite o valor do saque: "))

    if saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo = saldo - saque
        print(f"Olá, {nome}!")
        print(f"Saque realizado com sucesso.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
#processamento


if saque > saldo:
    print("Saldo insuficiente para realizar o saque.") 
    while saque > saldo:
        saque = float(input("Digite o valor do saque novamente: "))
        if saque > saldo:
            print("Saldo insuficiente para realizar o saque.")
        
else:
    
    continuar = input("Deseja realizar outro saque? (s/n): ")
while continuar.lower() == "s":
    saque = float(input("Digite o valor do saque: "))
    if saque > calculo:
        print("Saldo insuficiente para realizar o saque.")
        while saque > calculo:
            saque = float(input("Digite o valor do saque novamente: "))
            if saque > calculo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                calculo -= saque
                print(f"Olá {nome}, seu novo saldo é: R$ {calculo:.2f}")
                print("Saque realizado com sucesso.")
                continuar = input("Deseja realizar outro saque? (s/n): ")
    else:
        calculo -= saque
        print(f"Olá {nome}, seu novo saldo é: R$ {calculo:.2f}")
        print("Saque realizado com sucesso.")
        continuar = input("Deseja realizar outro saque? (s/n): ")
        