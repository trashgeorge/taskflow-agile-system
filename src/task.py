class Task:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade

    def resumo(self):
        return f"{self.titulo} - {self.prioridade}"