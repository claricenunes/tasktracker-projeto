# TaskTracker

Sistema de linha de comando desenvolvido em Python 3 para cadastrar, visualizar e acompanhar tarefas.

## Funcionalidades

* Cadastrar tarefas com título, descrição, prioridade e data limite.
* Validar o título obrigatório e as prioridades permitidas: Alta, Média ou Baixa.
* Validar a data limite no formato `DD/MM/AAAA`.
* Listar as tarefas cadastradas com seus dados e status.
* Marcar tarefas como concluídas.
* Exibir o total de tarefas concluídas.

## Tecnologias utilizadas

* Python 3: implementação da aplicação.
* Git: controle de versão do código.
* GitHub: hospedagem do repositório.

## Requisitos

* Python 3 instalado.
* Git instalado, caso deseje clonar e versionar o projeto.

## Instalação e execução

Clone o repositório:

```bash
git clone https://github.com/claricenunes/tasktracker-projeto.git
```

Entre na pasta do projeto:

```bash
cd tasktracker-projeto
```

Execute a aplicação:

```bash
python3 src/main.py
```

## Menu da aplicação

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Concluir tarefa
4. Sair da aplicação

## Observação

Nesta versão, as tarefas ficam armazenadas na memória enquanto o programa está em execução. Ao fechar o programa, elas não são salvas em arquivo ou banco de dados.
