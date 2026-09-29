
def exercicio_05():
    print("\n--- Exercício 5: Classificação de Notas ---")
    while True:
        entrada = input("Digite a nota do aluno (0.0 a 10.0): ").strip().replace(',', '.')
        
        if not entrada:
            print("Erro: A entrada não pode estar vazia.")
            continue

        try:
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print(f"Erro: A nota {nota} está fora da faixa permitida (0 a 10).")
                continue

            print(f"\nNota registrada: {nota:.1f}")
            if nota >= 7.0:
                print("Situação: Aprovado")
            elif nota >= 5.0:
                print("Situação: Recuperação")
            else:
                print("Situação: Reprovado")
            break

        except ValueError:
            print("Erro: Digite um número decimal válido (ex: 8.5).")

if __name__ == "__main__":
    exercicio_05()