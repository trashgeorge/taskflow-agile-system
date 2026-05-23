# Aplicação principal do sistema TaskFlow

from task import Task

nova_tarefa = Task(
    "Corrigir bugs",
    "Resolver erros do sistema",
    "Alta"
)

print(nova_tarefa.resumo())

# Inicialização do sistema

# Sistema principal