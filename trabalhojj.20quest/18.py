
def exercicio_18():
    print("\n--- Exercício 18: Teste Caixa-Preta (Desconto em Compras) ---")
    print("Regras: Compras até R$ 100 não têm desconto. Acima de R$ 100 ganham 10% de desconto.")
    
    try:
        valor_compra = float(input("Digite o valor total da compra: R$ ").strip().replace(',', '.'))
        
        if valor_compra < 0:
            print("Erro: O valor da compra não pode ser negativo.")
            return

        if valor_compra > 100.00:
            valor_final = valor_compra * 0.90
            print(f"Desconto de 10% aplicado! Valor final: R$ {valor_final:.2f}")
        else:
            valor_final = valor_compra
            print(f"Sem desconto aplicado. Valor final: R$ {valor_final:.2f}")

    except ValueError:
        print("Erro: Digite um valor numérico válido.")

if __name__ == "__main__":
    exercicio_18()