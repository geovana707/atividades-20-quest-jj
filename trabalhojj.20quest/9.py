
def exercicio_09():
    print("\n--- Exercício 9: Classificação por Faixa de Desempenho ---")
    while True:
        try:
            nota = float(input("Digite a nota final do aluno (0 a 10): ").strip().replace(',', '.'))
            if nota < 0 or nota > 10:
                print("Erro: A nota precisa estar entre 0 e 10.")
                continue

          
            if nota < 5.0:
                classificacao = "Insuficiente"
            elif nota < 7.0:
                classificacao = "Regular"
            elif nota < 9.0:
                classificacao = "Bom"
            else:
                classificacao = "Excelente"

            print(f"Nota: {nota:.1f} -> Classificação: {classificacao}")
            break

        except ValueError:
            print("Erro: Digite um valor numérico.")

if __name__ == "__main__":
    exercicio_09()