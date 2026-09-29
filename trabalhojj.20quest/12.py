
def exercicio_12():
    print("\n--- Exercício 12: Verificação de Nomes Duplicados ---")
    nomes = []
    
    try:
        qtd = int(input("Quantos nomes de estudantes deseja cadastrar? "))
        if qtd <= 0:
            print("Erro: Quantidade inválida.")
            return

        for i in range(qtd):
            nome = input(f"Digite o nome do {i + 1}º estudante: ").strip().title()
            while not nome:
                nome = input("O nome não pode ser vazio. Digite novamente: ").strip().title()
            nomes.append(nome)

        vistos = set()
        duplicados = set()

        for nome in nomes:
            if nome in vistos:
                duplicados.add(nome)
            else:
                vistos.add(nome)

        print("\n--- Resultado da Análise ---")
        print(f"Lista digitada: {nomes}")
        if duplicados:
            print(f"Atenção: Os seguintes nomes estão duplicados: {list(duplicados)}")
        else:
            print("Sucesso: Nenhum nome duplicado foi encontrado.")

    except ValueError:
        print("Erro: Digite um número inteiro para a quantidade.")

if __name__ == "__main__":
    exercicio_12()