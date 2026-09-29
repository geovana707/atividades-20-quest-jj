
def exercicio_07():
    print("\n--- Exercício 7: Validação de Identificador / CPF ---")
    while True:
        entrada = input("Digite o identificador numérico (ex: CPF com 11 dígitos): ").strip()
        
        # Limpa pontos e traços
        limpo = entrada.replace(".", "").replace("-", "")

        if not limpo.isdigit():
            print("Erro: O identificador deve conter apenas dígitos numéricos.")
            continue

        if len(limpo) != 11:
            print(f"Erro: Quantidade de dígitos incorreta! Esperado: 11. Informado: {len(limpo)}.")
            continue

        print(f"Sucesso: Identificador '{limpo}' está no formato estrutural correto (11 dígitos).")
        break

if __name__ == "__main__":
    exercicio_07()