# Classe responsável pelas tarefas do sistema

class Task:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "Pendente"
        
# Método responsável por retornar resumo da tarefa
    def resumo(self):
        return f"{self.titulo} - {self.prioridade}"

    def concluir(self):
        self.status = "Concluída"