# 🛒 Carrinho de Compras com Desconto

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![GitHub](https://img.shields.io/badge/GitHub-repo-black?logo=github)

## 📌 Sobre o projeto

Sistema simples em Python que simula um carrinho de compras. O usuário digita
seu nome e vai adicionando produtos de uma loja de eletrônicos ao carrinho.
No final, o programa calcula o valor de cada item (aplicando desconto quando
houver) e mostra o resumo total da compra.

## 🐍 Tecnologia utilizada

- **Linguagem:** Python 3
- **Bibliotecas:** nenhuma (apenas Python puro)

## 🛍️ Produtos disponíveis

| Produto      | Preço (R$) |
|--------------|-----------:|
| Computador   | 3000.00    |
| Celular      | 2000.00    |
| Tablet       | 1500.00    |
| Monitor      | 1000.00    |
| Impressora   | 800.00     |
| Fone         | 500.00     |
| Mouse        | 300.00     |
| Teclado      | 300.00     |

## 🧮 Regra de desconto

O desconto aplicado depende do preço do produto:

| Preço do produto | Desconto |
|-------------------|----------|
| R$ 300,00          | 5%       |
| R$ 500,00          | 10%      |
| R$ 1000,00         | 15%      |
| Outros valores     | 0%       |

**Fórmula do valor final:**

```
Valor final = Preço × (1 − Desconto)
```

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o programa:
   ```bash
   python app.py
   ```
4. Digite seu nome, depois vá digitando os nomes dos produtos que quer
   adicionar ao carrinho (ex: `mouse`, `teclado`). Digite `sair` para
   finalizar e ver o resumo da compra.

## 💡 Exemplo de uso

```
Digite seu nome: Victor
Digite o nome do produto (ou 'sair' para finalizar): mouse
mouse adicionado ao carrinho!

Digite o nome do produto (ou 'sair' para finalizar): sair

Olá, Victor! Aqui está o resumo da sua compra:

- mouse: desconto de 5% | valor final: R$ 285.00

Valor total da compra: R$ 285.00
Obrigado por comprar conosco, Victor!
Volte sempre!
```

## 🧑‍💻 Autor

Feito por [Victor Ferreira de Souza](https://github.com/seu-usuario) 🚀
