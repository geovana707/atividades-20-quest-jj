
def exercicio_02():
    print("\n--- Exercício 2: Cálculo de Média com Segurança ---")
    while True:
        try:
            qtd = int(input("Digite a quantidade de notas (ou 0 para cancelar): "))
            
            # Impedindo a divisão por zero
            if qtd == 0:
                print("Erro: Impossível calcular a média com 0 notas (divisão por zero).")
                break
            elif qtd < 0:
                print("Erro: A quantidade não pode ser negativa.")
                continue

            soma = 0
            for i in range(1, qtd + 1):
                while True:
                    try:
                        nota = float(input(f"Digite a nota {i}: ").strip().replace(',', '.'))
                        soma += nota
                        break
                    except ValueError:
                        print("Erro: Digite um número válido para a nota.")

            media = soma / qtd
            print(f"Média final calculada: {media:.2f}")
            break

        except ValueError:
            print("Erro: A quantidade deve ser um número inteiro.")

if __name__ == "__main__":
    exercicio_02()