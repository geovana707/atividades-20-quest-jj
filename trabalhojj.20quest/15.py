
# A função DEVE utilizar 'return' em vez de apenas dar 'print'
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def exercicio_15():
    print("\n--- Exercício 15: Função com Retorno de Dados ---")
    try:
        n1 = float(input("Digite a 1ª nota: ").strip().replace(',', '.'))
        n2 = float(input("Digite a 2ª nota: ").strip().replace(',', '.'))

        # O valor retornado é guardado na variável 'media' para uso posterior
        media = calcular_media(n1, n2)
        
        print(f"Média calculada pela função: {media:.2f}")
        
        # Exemplo de reutilização do retorno
        if media >= 7.0:
            print("Resultado: Aprovado!")
        else:
            print("Resultado: Necessita de pontos extras/recuperação.")

    except ValueError:
        print("Erro: Digite valores numéricos válidos.")

if __name__ == "__main__":
    exercicio_15()