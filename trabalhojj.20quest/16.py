
def exercicio_16():
    print("\n--- Exercício 16: Leitura Segura de Arquivos ---")
    nome_arquivo = input("Digite o nome do arquivo para abrir (ex: alunos.txt): ").strip()

    try:
        # Tratamento com bloco try-except para a exceção FileNotFoundError
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("\n--- Conteúdo do Arquivo ---")
            print(conteudo)

    except FileNotFoundError:
        print(f"\nErro de Execução: O arquivo '{nome_arquivo}' não foi encontrado na pasta atual.")
        print("Dica: Crie o arquivo ou verifique se digitou o nome corretamente.")

if __name__ == "__main__":
    exercicio_16()