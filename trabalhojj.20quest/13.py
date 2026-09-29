
def exercicio_13():
    print("\n--- Exercício 13: Maior e Menor Temperatura ---")
    try:
        qtd = int(input("Quantas temperaturas deseja registrar? ").strip())
        if qtd <= 0:
            print("Erro: Informe pelo menos uma temperatura.")
            return

        temperaturas = []
        for i in range(1, qtd + 1):
            while True:
                try:
                    temp = float(input(f"Digite a temperatura {i} (°C): ").strip().replace(',', '.'))
                    temperaturas.append(temp)
                    break
                except ValueError:
                    print("Erro: Digite uma temperatura válida.")

        # Inicialização correta usando o primeiro elemento lido
        maior = temperaturas[0]
        menor = temperaturas[0]

        for temp in temperaturas[1:]:
            if temp > maior:
                maior = temp
            if temp < menor:
                menor = temp

        print("\n--- Extremos Encontrados ---")
        print(f"Temperaturas registradas: {temperaturas}")
        print(f"Maior temperatura: {maior}°C")
        print(f"Menor temperatura: {menor}°C")

    except ValueError:
        print("Erro: Digite um número inteiro para a quantidade.")

if __name__ == "__main__":
    exercicio_13()