
def exercicio_04():
    print("\n--- Exercício 4: Cálculo do Total da Compra ---")
    
    produto = input("Digite o nome do produto: ").strip()
    while not produto:
        produto = input("Nome inválido. Digite o nome do produto: ").strip()

    while True:
        try:
            preco = float(input(f"Digite o preço unitário de '{produto}': R$ ").strip().replace(',', '.'))
            if preco <= 0:
                print("Erro: O preço deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido para o preço (ex: 15.50).")

    while True:
        try:
            quantidade = int(input(f"Digite a quantidade comprada de '{produto}': ").strip())
            if quantidade <= 0:
                print("Erro: A quantidade deve ser de pelo menos 1 item.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro para a quantidade.")

    total = preco * quantidade
    print(f"\n--- Resumo ---")
    print(f"Produto: {produto}")
    print(f"Total a pagar ({quantidade}x R$ {preco:.2f}): R$ {total:.2f}")

if __name__ == "__main__":
    exercicio_04()