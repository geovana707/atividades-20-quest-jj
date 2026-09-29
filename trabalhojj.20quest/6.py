
def exercicio_06():
    print("\n--- Exercício 6: Sistema de Autenticação ---")
    SENHA_CORRETA = "123456"
    tentativas = 3

    while tentativas > 0:
        senha = input(f"Digite a senha ({tentativas} tentativa(s) restante(s)): ").strip()
        
        if len(senha) < 6:
            print("Aviso de Segurança: Senhas de acesso possuem no mínimo 6 caracteres.")

        if senha == SENHA_CORRETA:
            print("Sucesso: Acesso liberado ao sistema!")
            return
        else:
            tentativas -= 1
            if tentativas > 0:
                print("Erro: Senha incorreta. Tente novamente.\n")
            else:
                print("Bloqueio: Excesso de tentativas incorretas!")

if __name__ == "__main__":
    exercicio_06()