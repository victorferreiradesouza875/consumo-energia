#entrada
nome = input("Digite seu nome: ")


produtos = {
    "computador": 3000.00,
    "celular": 2000.00,
    "tablet": 1500.00,
    "fone": 500.00,
    "mouse": 300.00,
    "teclado": 300.00,
    "monitor": 1000.00,
    "impressora": 800.00
}

carrinho = []  # lista para guardar os produtos escolhidos

while True:
    produto = input("Digite o nome do produto (ou 'sair' para finalizar): ").lower()
    
    if produto == "sair":
        break
    
    if produto not in produtos:
        print("Produto não encontrado! Tente novamente.")
        continue
    
    carrinho.append(produto)
    print(f"{produto} adicionado ao carrinho!\n")

#saida
if not carrinho:
    print("Nenhum produto foi adicionado.")
else:
    total = 0
    print(f"\nOlá, {nome}! Aqui está o resumo da sua compra:\n")
    
    for produto in carrinho:
        preco = produtos[produto]
        
        if preco == 300.00:
            desconto = 0.05
        elif preco == 500.00:
            desconto = 0.10
        elif preco == 1000.00:
            desconto = 0.15
        else:
            desconto = 0
        
        valor_final = preco * (1 - desconto)
        total += valor_final
        
        print(f"- {produto}: desconto de {desconto*100:.0f}% | valor final: R$ {valor_final:.2f}")
    
    print(f"\nValor total da compra: R$ {total:.2f}")
    print(f"Obrigado por comprar conosco, {nome}!")
    print("Volte sempre!")