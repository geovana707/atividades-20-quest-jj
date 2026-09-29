
def exercicio_14():
    print("\n--- Exercício 14: Cadastro de Produto com Campos Obrigatórios ---")
    
    produto = input("Digite o nome do produto: ").strip()
    preco_input = input("Digite o preço (ou deixe em branco para testar campo ausente): ").strip()
    
    # Tratamento para impedir cálculos com dados ausentes
    if not produto or not preco_input:
        print("\nErro de Validação: Não é possível calcular o preço. Há campos obrigatórios ausentes!")
        return

    try:
        preco = float(preco_input.replace(',', '.'))
        qtd = int(input("Digite a quantidade: ").strip())
        
        total = preco * qtd
        print(f"\nProduto: {produto} | Total: R$ {total:.2f}")

    except ValueError:
        print("Erro: Preço ou quantidade com formato numérico inválido.")

if __name__ == "__main__":
    exercicio_14()