
def exercicio_03():
    print("\n--- Exercício 3: Consulta de Alunos por Índice ---")
    alunos = []
    
    try:
        qtd = int(input("Quantos alunos deseja cadastrar na turma? "))
        if qtd <= 0:
            print("Erro: Cadastre pelo menos 1 aluno.")
            return

        for i in range(qtd):
            nome = input(f"Digite o nome do aluno {i + 1}: ").strip()
            while not nome:
                nome = input("O nome não pode ser vazio. Digite novamente: ").strip()
            alunos.append(nome)

        print("\n--- Lista de Alunos ---")
        for idx, nome in enumerate(alunos):
            print(f"Índice [{idx}] -> {nome}")

        while True:
            try:
                indice = int(input(f"\nDigite o índice que deseja consultar (0 a {len(alunos) - 1}): "))
                
                # Validação para impedir IndexError
                if 0 <= indice < len(alunos):
                    print(f"Sucesso: O aluno no índice {indice} é '{alunos[indice]}'.")
                    break
                else:
                    print(f"Erro de Índice: O índice {indice} é inválido. Escolha entre 0 e {len(alunos) - 1}.")
            except ValueError:
                print("Erro: Digite um número inteiro válido para o índice.")

    except ValueError:
        print("Erro: Digite um número inteiro para a quantidade.")

if __name__ == "__main__":
    exercicio_03()