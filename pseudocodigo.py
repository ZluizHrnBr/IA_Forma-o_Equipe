import time
import math

def combinacoes(n, k):
    """Calcula o número de combinações de n elementos tomados k a k."""
    return math.comb(n, k)

def tarefa():
    #Simulação de uma operação matemática para somar de 0 à 999 pela quantidade de combinações realizadas
    resultado = sum(range(1000))  # Soma de 0 a 999
    return resultado


def executar_forca_bruta(n, k):
    """Executa uma tarefa pela quantidade de combinações e mede o tempo."""
    qtd_combinacoes = combinacoes(n, k)
    print(f"Número de combinações C({n}, {k}) = {qtd_combinacoes}")

    start_time = time.perf_counter()  # Inicia a contagem do tempo


    for _ in range(qtd_combinacoes):
      tarefa()

    end_time = time.perf_counter()  # Finaliza a contagem do tempo
    tempo_gasto = end_time - start_time
    print(f"Tempo gasto na execução: {tempo_gasto:.6f} segundos")

# Exemplo de uso
n = 35  # Total de elementos
k = 5  # Elementos a serem escolhidos
executar_forca_bruta(n, k)