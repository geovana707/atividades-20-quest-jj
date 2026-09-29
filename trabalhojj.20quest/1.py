
def exercicio_01():
    print("\n--- Exercício 1: Validação de Idade ---")
    while True:
        entrada = input("Digite a idade do estudante: ").strip()
        
        if not entrada:
            print("Erro: A entrada não pode estar vazia. Tente novamente.")
            continue

        try:
            idade = int(entrada)
            if idade <= 0:
                print("Erro: A idade deve ser um número inteiro positivo maior que zero.")
                continue
            
            if idade >= 12:
                print(f"Sucesso: Estudante com {idade} anos está liberado para a atividade.")
            else:
                print(f"Aviso: Estudante com {idade} anos não possui a idade mínima recomendada.")
            break

        except ValueError:
            print("Erro: Entrada inválida. Digite apenas um número inteiro.")

if __name__ == "__main__":
    exercicio_01()