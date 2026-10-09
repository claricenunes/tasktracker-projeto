# TaskTracker

Sistema de linha de comando para cadastrar e acompanhar tarefas.

## Funcionalidades

- Cadastrar tarefas com título, descrição, prioridade e data limite.
- Validar título obrigatório, prioridade e data no formato `DD/MM/AAAA`.
- Listar todas as tarefas e exibir seus dados.
- Marcar tarefas como concluídas.
- Mostrar o total de tarefas concluídas.

## Tecnologias

- Python 3
- Git e GitHub

## Requisitos

Ter o Python 3 instalado.

## Como executar

Na pasta raiz do projeto, execute:

```bash
python3 src/main.py
```

No menu, escolha uma opção:
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Concluir tarefa
4. Sair da aplicação

## Observação

Nesta versão, as tarefas ficam armazenadas na memória enquanto o programa está em execução. Ao fechar o programa, elas não são salvas em arquivo ou banco de dados.
