import pygad
import numpy as np
import matplotlib.pyplot as plt
import time

# Definição de habilidades dos desenvolvedores (nome: [habilidades])
desenvolvedores = {
    'Aluno1': ["Desenvolvimento Software", "Banco de dados", " Teste de Software"],
    'Aluno2': ["Desenvolvimento campo legado", "Gestor de projetos"],
    'Aluno3': ["Arquiteto de software", "Desenvolvimento mobile"],
    'Aluno4': ["Desenvolvedor FullStack", "Banco de dados"],
    'Aluno5': ["Infraestrutura parte 1 - cloud", "Data Science"],
    'Aluno6': ["Desenvolvimento web"],
    'Aluno7': ["Infraestrutura parte 2 - seguranca", "Desenvolvimento campo legado"],
    'Aluno8': ["Desenvolvimento Software"],
    'Aluno9': ["Banco de dados"],
    'Aluno10': ["Desenvolvimento campo legado", "Arquiteto de software"],
    'Aluno11': ["Arquiteto de software"],
    'Aluno12': ["Desenvolvimento mobile", "Teste de software"],
    'Aluno13': ["Desenvolvedor FullStack", "Banco de dados"],
    'Aluno14': ["Desenvolvimento Software", "Data Science"],
    'Aluno15': ["Infraestrutura parte 2 - seguranca", "Desenvolvimento campo legado", "Gestor de projetos"],
    'Aluno16': ["Teste de software", "Arquiteto de software"],
    'Aluno17': ["Desenvolvimento campo legado", "Desenvolvedor FullStack"],
    'Aluno18': ["Desenvolvimento web", "Gestor de projetos"],
    'Aluno19': ["Desenvolvimento mobile", "Desenvolvimento Software"],
    'Aluno20': ["Data Science", "Teste de software"],
    'Aluno21': ["Desenvolvedor FullStack", "Desenvolvimento Software"],
    'Aluno22': ["Arquiteto de software"],
    'Aluno23': ["Desenvolvimento mobile"],
    'Aluno24': ["Infraestrutura parte 1 - cloud"],
    'Aluno25': ["Desenvolvimento de software", "Teste de software", "Data Science"],
    'Aluno26': ["Infraestrutura parte 2 - seguranca", "Desenvolvimento campo legado", "Arquiteto de software"],
    'Aluno27': ["Gestor de projetos", "Teste de software"],
    'Aluno28': ["Data Science", "Gestor de projetos", "Desenvolvimento Software"],
    'Aluno29': ["Arquiteto de software", "Desenvolvimento mobile", "Banco de dados"],
    'Aluno30': ["Desenvolvimento campo legado"],
    'Aluno31': ["Data Science", "Banco de dados", "Teste de software"],
    'Aluno32': ["Gestor de projetos"],
    'Aluno33': ["Desenvolvimento web", "Desenvolvimento Software", "Banco de dados"],
    'Aluno34': ["Data Science", "Desenvolvimento campo legado", "Arquiteto de software"],
    'Aluno35': ["Arquiteto de software", "Desenvolvimento Software"]
}


# Habilidades necessárias para o projeto e suas prioridades (maior valor significa maior prioridade)
habilidades_prioridade = {
    3: ['Desenvolvimento campo legado', 'Desenvolvimento mobile', 'Banco de dados'],  # Alta prioridade
    2: ['Arquiteto de software', 'Teste de software'],  # Média prioridade
    1: ['Desenvolvedor FullStack']  # Baixa prioridade
}

# Definir os pesos das prioridades
pesos_prioridade = {
    3: 3,  # Alta prioridade tem peso 3
    2: 2,  # Média prioridade tem peso 2
    1: 1   # Baixa prioridade tem peso 1
}

tempo_por_geracao = []
coincidencias_por_geracao = []
start_time = time.time()

def fitness_func_cenario1(ga_instance, solution, solution_idx):
    habilidades_equipe = []
    desenvolvedores_selecionados = set()
    somatorio_coincidencias = 0

    # Iterar sobre os desenvolvedores na solução
    for dev_idx in solution:
        dev_idx = int(dev_idx)

        # Penalizar repetições
        if dev_idx in desenvolvedores_selecionados:
            return 0  # Penalização máxima por repetição

        desenvolvedores_selecionados.add(dev_idx)
        dev_nome = list(desenvolvedores.keys())[dev_idx]
        habilidades_dev = desenvolvedores[dev_nome]

        # Verificar coincidências de habilidades com o projeto, ponderando pela prioridade
        for prioridade, habilidades in habilidades_prioridade.items():
            coincidencias = set(habilidades_dev).intersection(habilidades)
            somatorio_coincidencias += len(coincidencias) * pesos_prioridade[prioridade]

        # Para o cenário 1, onde cada estudante tem 1 habilidade variando de 1 a 3
        fitness = somatorio_coincidencias / 3.0

    return fitness



def on_generation_cenario1(ga_instance):
    global tempo_por_geracao, start_time
    end_time = time.time()
    tempo_por_geracao.append(end_time - start_time)
    start_time = end_time

#Cenário 1, onde cada estudante tem 1 habilidade variando de 1 a 3
#Parâmetros do algoritmo genético
num_generations = 1000  # Número de gerações
num_parents_mating = 500  # Número de pais para cruzamento
sol_per_pop = 500  # Número de soluções por população
num_genes = 5  # Tamanho da equipe (número de desenvolvedores por equipe)

# Limites dos valores dos genes (índices dos desenvolvedores de 0 a len(desenvolvedores) - 1)
gene_space = list(range(len(desenvolvedores)))

# Criar instância do algoritmo genético
ga_instance = pygad.GA(
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func_cenario1,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type="rws",
    gene_space=gene_space,  # Corrigido para uma única lista
    mutation_percent_genes=15,  # Percentual de mutação nos genes
    allow_duplicate_genes=False,  # Evita selecionar o mesmo desenvolvedor mais de uma vez
    on_generation=on_generation_cenario1
)

start_time = time.time()

# Executar o algoritmo genético
ga_instance.run()


execution_time = time.time() - start_time

# Exibir o progresso do tempo de execução por geração
plt.plot(range(1, len(tempo_por_geracao) + 1), tempo_por_geracao)
plt.xlabel('Geração')
plt.ylabel('Tempo de execução (segundos)')
plt.title('Tempo de Execução por Geração')
plt.grid(True)
plt.show()

# Obter a melhor solução encontrada
solution, solution_fitness, solution_idx = ga_instance.best_solution()

#Equipe selecionada no cenário 1
equipe_selecionada = [list(desenvolvedores.keys())[int(dev_idx)] for dev_idx in solution]

# Limitar a impressão de gerações para evitar overflow de dados
max_generations_to_print = 5

if len(coincidencias_por_geracao) > 0:
    coincidencias_ultima_geracao = coincidencias_por_geracao[-1]
    print(f"Coincidências na última geração: {coincidencias_ultima_geracao}")
else:
    print("Nenhuma coincidência encontrada.")

# Exibir coincidências das primeiras gerações
for i, coincidencia in enumerate(coincidencias_por_geracao[:max_generations_to_print]):
    print(f"Geração {i}: Coincidências: {coincidencia}")

# Exibir os detalhes da melhor equipe

print('----------Cenário 1---------------')

print(f"\nMelhor equipe: {equipe_selecionada}")
print(f"Fitness da melhor solução: {solution_fitness}")
print(f"Tempo de execução: {execution_time:.10f} segundos")

# Exibir as habilidades e cargos de cada desenvolvedor da melhor equipe para o cenário 1
for dev_nome in equipe_selecionada:
    habilidades = desenvolvedores[dev_nome]
    print(f"{dev_nome}: {habilidades}")

try:
    ga_instance.plot_fitness()
except ImportError:
    print("Matplotlib não está instalada. Gráfico não será exibido.")