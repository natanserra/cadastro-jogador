def obter_numero_positivo(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor > 0:
                return valor
            print("Número inválido. Deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_gols_por_partida(num_partidas):
    gols_por_partida = []
    for i in range(num_partidas):
        while True:
            try:
                gols = int(input(f"Digite a quantidade de gols na partida {i + 1}: "))
                if gols >= 0:
                    gols_por_partida.append(gols)
                    break
                print("Número inválido. A quantidade de gols não pode ser negativa.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    return gols_por_partida

def exibir_aproveitamento(nome_jogador, num_partidas, gols_por_partida, total_gols):
    aproveitamento = {
        'Nome': nome_jogador,
        'Partidas Jogadas': num_partidas,
        'Gols por Partida': gols_por_partida,
        'Total de Gols': total_gols
    }

    print("\nAproveitamento do Jogador:")
    for chave, valor in aproveitamento.items():
        print(f"{chave}: {valor}")

def main():
    print("Gerenciador de Aproveitamento do Jogador")

    nome_jogador = input("Digite o nome do jogador: ").strip()
    num_partidas = obter_numero_positivo("Digite o número de partidas jogadas: ")

    gols_por_partida = obter_gols_por_partida(num_partidas)
    total_gols = sum(gols_por_partida)

    exibir_aproveitamento(nome_jogador, num_partidas, gols_por_partida, total_gols)

if __name__ == "__main__":
    main()
