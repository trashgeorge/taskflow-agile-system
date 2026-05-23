import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task import Task


def test_resumo_task():
    task = Task("Teste", "Descricao", "Alta")

    assert task.resumo() == "Teste - Alta"