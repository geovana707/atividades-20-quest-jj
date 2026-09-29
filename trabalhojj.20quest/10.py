
def exercicio_10():
    print("\n--- Exercício 10: Acumulador de Números (Digitar 0 para sair) ---")
    soma = 0
    contador = 0

    while True:
        try:
            num = int(input("Digite um número inteiro (ou 0 para encerrar): ").strip())
            
            # Condição de parada explícita para evitar loop infinito
            if num == 0:
                break
                
            soma += num
            contador += 1

        except ValueError:
            print("Erro: Digite apenas números inteiros válidos.")

    print(f"\nTotal de números digitados: {contador}")
    print(f"Soma total acumulada: {soma}")

if __name__ == "__main__":
    exercicio_10()