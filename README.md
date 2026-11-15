# Rastro_Selvagem

# Rastro Selvagem

## 1. O que é o sistema?

O **Rastro Selvagem** é um sistema web desenvolvido para auxiliar na organização e no gerenciamento de projetos, permitindo estruturar atividades, acompanhar demandas e organizar o desenvolvimento por meio de metodologias ágeis.

O sistema utiliza conceitos do Scrum e ferramentas de priorização de tarefas, como MoSCoW e RICE, possibilitando organizar histórias de usuário, épicos, backlogs e critérios de aceitação.

A aplicação foi desenvolvida utilizando Python e Django, com PostgreSQL como sistema de gerenciamento de banco de dados.

## 2. Palavras que aparecem no sistema

| Termo | Significado |
|---|---|
| Projeto | Conjunto de atividades organizadas com um objetivo. |
| Product Backlog | Lista de funcionalidades e demandas do produto. |
| Sprint Backlog | Conjunto de atividades selecionadas para uma Sprint. |
| Épico | Funcionalidade ou objetivo amplo que pode ser dividido em histórias menores. |
| História de Usuário | Descrição de uma funcionalidade sob a perspectiva de quem utilizará o sistema. |
| Critério de Aceitação | Condições que determinam se uma funcionalidade atende ao que foi solicitado. |
| Kanban | Quadro visual utilizado para acompanhar o andamento das atividades. |
| MoSCoW | Método de priorização que classifica demandas em Must have, Should have, Could have e Won't have. |
| RICE | Método de priorização baseado em alcance, impacto, confiança e esforço. |
| Scrum | Metodologia ágil utilizada para organizar o desenvolvimento de projetos. |
| Administrador | Usuário com papel administrativo. |
| Gestor | Perfil de usuário destinado à gestão. |
| Voluntário | Perfil de usuário destinado à participação nas atividades. |

## 3. O que o sistema faz?

O Rastro Selvagem disponibiliza funcionalidades para organização e acompanhamento de projetos.

Entre suas principais funcionalidades estão:

- **Cadastro de usuários:** permite criar contas e realizar autenticação no sistema.
- **Gerenciamento de projetos:** permite cadastrar, visualizar, editar e excluir projetos.
- **Gerenciamento de Backlogs:** permite criar, visualizar, editar e excluir backlogs associados aos projetos.
- **Gerenciamento de épicos:** permite cadastrar e organizar grandes funcionalidades dentro de um projeto.
- **Histórias de usuário:** permite cadastrar, consultar, editar e excluir histórias de usuário.
- **Priorização de demandas:** utiliza os métodos MoSCoW e RICE para auxiliar na organização das prioridades.
- **Critérios de aceitação:** permite definir condições e resultados esperados para as histórias de usuário.
- **Quadro Kanban:** permite visualizar as histórias de usuário organizadas conforme seus estados de desenvolvimento.
- **Acompanhamento de status:** possibilita alterar o andamento das histórias entre as etapas disponíveis.

Os status utilizados no sistema são:

- A fazer;
- Em andamento;
- Em revisão;
- Concluída.

## 4. O que você precisa instalar?

Para executar o projeto localmente, é necessário ter os seguintes programas:

1. **Python:** linguagem utilizada no desenvolvimento da aplicação.
2. **PostgreSQL:** sistema de gerenciamento do banco de dados.
3. **Git:** ferramenta para baixar o projeto do GitHub.
4. **Visual Studio Code (opcional):** editor de código recomendado para visualizar e executar o projeto.

As bibliotecas Python utilizadas estão registradas no arquivo `requirements.txt`.

Entre as principais dependências estão:

- Django 6.1.2;
- Flask 3.0.3;
- Flask-Cors;
- psycopg;
- Pillow;
- python-dotenv;
- CustomTkinter.

## 5. Instalação passo a passo

### Passo 1 — Baixar o projeto

Abra o terminal ou prompt de comando e execute:

```bash
git clone https://github.com/SantiagoJu/Rastro_Selvagem.git
```

Entre na pasta:

```bash
cd Rastro_Selvagem
```

### Passo 2 — Criar um ambiente virtual

Execute:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

### Passo 3 — Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

Esse comando instala as bibliotecas necessárias listadas no arquivo de dependências.

### Passo 4 — Configurar o PostgreSQL

Instale e inicie o PostgreSQL.

Crie um banco de dados chamado:

```sql
CREATE DATABASE rastro_selvagem;
```

Configure também o usuário e as credenciais de acesso ao banco de dados conforme as configurações locais da aplicação.

**Importante:** o arquivo `config/settings.py` contém as configurações de conexão com o PostgreSQL. Verifique essas informações antes de executar o projeto.

### Passo 5 — Executar as migrações

Com o banco de dados criado e a conexão configurada, execute:

```bash
python manage.py migrate
```

Esse comando cria as tabelas necessárias para o funcionamento do Django.

### Passo 6 — Iniciar o servidor

Execute:

```bash
python manage.py runserver
```

O servidor local será iniciado e a aplicação poderá ser acessada pelo navegador.

## 6. Como abrir o sistema no navegador?

Depois de iniciar o servidor com:

```bash
python manage.py runserver
```

Abra o navegador e acesse:

**http://127.0.0.1:8000/**

Para acessar diretamente as funcionalidades:

- Login: `http://127.0.0.1:8000/contas/login/`
- Cadastro: `http://127.0.0.1:8000/contas/cadastro/`
- Projetos: `http://127.0.0.1:8000/projetos/`
- Backlogs: `http://127.0.0.1:8000/backlog/`
- Épicos: `http://127.0.0.1:8000/criterios/epico/`
- Histórias de usuário: `http://127.0.0.1:8000/criterios/historia/`
- Critérios de aceitação: `http://127.0.0.1:8000/criterios/criterio/`

Para encerrar o servidor, volte ao terminal e pressione `CTRL + C`.

## 7. Onde estão os documentos do projeto?

Os principais arquivos e diretórios estão organizados na raiz do repositório:


## 9. Participantes


A relação completa dos participantes responsáveis pelo desenvolvimento:.

- Angel Flavius Alves Negri;
- Caio Lucas Borges Nascimento;
- Jussara Santiago;
- Miguel de Souza;
- Tang Sheng.
