
def exercicio_20():
    print("\n--- Exercício 20: Projeto Final - Cadastro de Aluno ---")
    
    # 1 Nome
    nome = input("Digite o nome do aluno: ").strip()
    if not nome or nome.isdigit():
        print("Erro: Nome do aluno é inválido.")
        return

    # 2 Idade com try-except
    try:
        idade = int(input("Digite a idade do aluno: ").strip())
        if idade <= 0 or idade > 120:
            print("Erro de Limite: Idade fora da faixa válida (1-120).")
            return
    except ValueError:
        print("Erro de Tipo: A idade deve ser um número inteiro.")
        return

    # 3 Três Notas
    notas = []
    for i in range(1, 4):
        try:
            nota = float(input(f"Digite a nota {i} (0.0 a 10.0): ").strip().replace(',', '.'))
            if nota < 0.0 or nota > 10.0:
                print(f"Erro de Validação: A nota {i} deve estar entre 0 e 10.")
                return
            notas.append(nota)
        except ValueError:
            print("Erro de Tipo: A nota deve ser um valor numérico.")
            return

    # 4. Cálculo da Média e Situação
    media = sum(notas) / len(notas)

    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

  
    print("\n" + "=" * 30)
    print("      RELATÓRIO DO ALUNO      ")
    print("=" * 30)
    print(f"Aluno: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Notas: {notas[0]:.1f} | {notas[1]:.1f} | {notas[2]:.1f}")
    print(f"Média Final: {media:.2f}")
    print(f"Situação: {situacao}")
    print("=" * 30)

if __name__ == "__main__":
    exercicio_20()