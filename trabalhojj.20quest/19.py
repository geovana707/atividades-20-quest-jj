
def exercicio_19():
    print("\n--- Exercício 19: Teste Caixa-Branca (Cobertura de Caminhos) ---")
    
    try:
        idade = int(input("Digite a idade do usuário: ").strip())
        renda = float(input("Digite a renda mensal: R$ ").strip().replace(',', '.'))
        cadastrado = input("O cadastro está ativo? (s/n): ").strip().lower() == 's'

        # Caminho 1
        if idade < 18:
            resultado = "Negado: Idade mínima de 18 anos necessária."
        # Caminho 2
        elif renda < 1500.00:
            resultado = "Negado: Renda mínima de R$ 1500.00 necessária."
        # Caminho 3
        elif not cadastrado:
            resultado = "Pendente: O cadastro precisa estar ativo."
        # Caminho 4
        else:
            resultado = "Aprovado: Solicitação concedida com sucesso!"

        print(f"\nResultado da Avaliação: {resultado}")

    except ValueError:
        print("Erro: Entradas de idade e renda devem ser numéricas.")

if __name__ == "__main__":
    exercicio_19()