
def exercicio_08():
    print("\n--- Exercício 8: Média de 3 Notas (Correção de Lógica) ---")
    notas = []
    
    for i in range(1, 4):
        while True:
            try:
                n = float(input(f"Digite a {i}ª nota: ").strip().replace(',', '.'))
                if 0 <= n <= 10:
                    notas.append(n)
                    break
                else:
                    print("Erro: Digite uma nota entre 0 e 10.")
            except ValueError:
                print("Erro: Digite um número válido.")

    # Correção da lógica utilizando parênteses para forçar a precedência da soma
    media = (notas[0] + notas[1] + notas[2]) / 3
    print(f"\nMédia das 3 notas: {media:.2f}")

if __name__ == "__main__":
    exercicio_08()