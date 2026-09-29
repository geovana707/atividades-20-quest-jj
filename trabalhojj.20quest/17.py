
def exercicio_17():
    print("\n--- Exercício 17: Validação de Cadastro de Aluno ---")
    
    nome = input("Digite o nome do aluno: ").strip()
    
    try:
        idade = int(input("Digite a idade: ").strip())
        curso = input("Digite o curso: ").strip()
        ano = int(input("Digite o ano letivo (1, 2 ou 3): ").strip())

        erros = []

        if not nome:
            erros.append("Nome não pode ficar vazio.")
        if idade <= 0 or idade > 120:
            erros.append(f"Idade '{idade}' é inválida.")
        if not curso:
            erros.append("Curso não pode ficar vazio.")
        if ano not in [1, 2, 3]:
            erros.append(f"Ano '{ano}' é inválido (deve ser 1, 2 ou 3).")

        if erros:
            print("\nErro: Cadastro rejeitado pelos seguintes motivos:")
            for e in erros:
                print(f"- {e}")
        else:
            print(f"\nSucesso: Aluno {nome} ({curso} - {ano}º Ano, {idade} anos) cadastrado!")

    except ValueError:
        print("Erro: Idade e ano letivo devem ser números inteiros.")

if __name__ == "__main__":
    exercicio_17()