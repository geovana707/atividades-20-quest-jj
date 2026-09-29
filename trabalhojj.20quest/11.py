
def exercicio_11():
    print("\n--- Exercício 11: Contagem de Números Pares ---")
    while True:
        try:
            n = int(input("Digite um número limite N (maior que 0): ").strip())
            if n <= 0:
                print("Erro: Digite um número inteiro maior que zero.")
                continue

            contador_pares = 0
            # Usamos N + 1 para garantir que N seja incluído no teste
            for i in range(1, n + 1):
                if i % 2 == 0:
                    contador_pares += 1

            print(f"Sucesso: Existem {contador_pares} número(s) par(es) entre 1 e {n}.")
            break

        except ValueError:
            print("Erro: Digite apenas números inteiros válidos.")

if __name__ == "__main__":
    exercicio_11()