created by  
sphinx-quickstart on Mon Jun 23 16:58:04 2025.  
contain the root `toctree` directive.

# Controlasso - Sistema de Gerenciamento Financeiro

## 1. Integrantes e Título

- **Título do Projeto:** Controlasso
- **Integrantes:** [Nomes da equipe]

## 2. Introdução

Sistema de gerenciamento de contas e negociação de ações, com dashboards de movimentações e carteira.

## 3. Definição do Projeto

### 3.1 Nome do Sistema

Controlasso

### 3.2 Justificativa

Aplicação web para simulação de contas e operações financeiras, permitindo estudos e protótipos de movimentações.

### 3.3 Problema a ser Resolvido

Facilitar a aprendizagem e experimentação com transações bancárias e operações de compra e venda de ações.

### 3.4 Público-alvo

Estudantes e entusiastas do mercado financeiro que desejam praticar em um ambiente controlado.

### 3.5 Objetivo do Sistema

Oferecer uma plataforma para transferência entre usuários, negociação de ações e acompanhamento de histórico.

## 4. Metodologia

### 4.1 Metodologia de Desenvolvimento (Scrum)

O projeto utiliza a metodologia ágil Scrum para gestão de sprints. A escolha visa promover entregas iterativas e feedback constante.

### 4.2 Lista de Requisitos

#### Requisitos Funcionais (RFs)

1. Cadastro de usuário gerando conta e saldo aleatório.
2. Transferência de valores entre usuários.
3. Compra e venda de ações.
4. Marcação de ações favoritas.
5. Dashboards de saldo, movimentações e ações.
6. Autenticação e controle de permissões (ADM e usuário).

#### Requisitos Não-funcionais (RNFs)

1. Utilizar Django como framework principal.
2. Proteger todas as rotas que exigem autenticação.
3. Persistir dados em banco relacional (ex.: PostgreSQL).

#### Regras de Negócio (RN)

1. Cada usuário possui uma conta única.
2. Transferências somente são efetivadas com saldo suficiente.
3. Movimentações de compra e venda alteram o saldo da conta.

## 5. Diagramas de Arquitetura

5.1 Diagrama de Entidades e Relacionamentos
-------------------------------------------

.. mermaid::

   erDiagram
       LogEntry ||--o{ ContentType : "content_type"
       LogEntry ||--o{ User : "user"
       Account ||--|| User : "user"
       Transfer ||--o{ User : "sender"
       Transfer ||--o{ User : "recipient"
       Trade ||--o{ User : "user"
       Trade ||--o{ Stock : "stock"
       FavoriteStock ||--o{ User : "user"
       FavoriteStock ||--o{ Stock : "stock"
       Session ||--|| AbstractBaseSession : "herda"
       User ||--|| AbstractUser : "herda"
       AbstractUser ||--|| AbstractBaseUser : "herda"
       AbstractUser ||--|| PermissionsMixin : "inclui"
       Permission ||--o{ ContentType : "content_type"

       LogEntry {
           AutoField id
           ForeignKey content_type
           ForeignKey user
           PositiveSmallIntegerField action_flag
           DateTimeField action_time
           TextField change_message
           TextField object_id
           CharField object_repr
       }

       Account {
           BigAutoField id
           OneToOneField user
           CharField account_number
           DecimalField balance
           CharField theme
       }

       Transfer {
           BigAutoField id
           ForeignKey recipient
           ForeignKey sender
           DecimalField amount
           DateTimeField created_at
       }

       Trade {
           BigAutoField id
           ForeignKey stock
           ForeignKey user
           DateTimeField created_at
           DecimalField price
           PositiveIntegerField quantity
           CharField trade_type
       }

       FavoriteStock {
           BigAutoField id
           ForeignKey stock
           ForeignKey user
       }

       Session {
           CharField session_key
           DateTimeField expire_date
           TextField session_data
       }

       AbstractBaseSession {
           DateTimeField expire_date
           TextField session_data
       }

       User {
           AutoField id
           DateTimeField date_joined
           EmailField email
           CharField first_name
           BooleanField is_active
           BooleanField is_staff
           BooleanField is_superuser
           DateTimeField last_login
           CharField last_name
           CharField password
           CharField username
       }

       Stock {
           BigAutoField id
           CharField code
           DecimalField current_price
           CharField name
       }

       Group {
           AutoField id
           CharField name
       }

       Permission {
           AutoField id
           ForeignKey content_type
           CharField codename
           CharField name
       }

       ContentType {
           AutoField id
           CharField app_label
           CharField model
       }

       AbstractUser {
           DateTimeField date_joined
           EmailField email
           CharField first_name
           BooleanField is_active
           BooleanField is_staff
           BooleanField is_superuser
           DateTimeField last_login
           CharField last_name
           CharField password
           CharField username
       }

       PermissionsMixin {
           abstract inheritance
       }

       AbstractBaseUser {
           abstract inheritance
       }

```{toctree}
:maxdepth: 2
:caption: Contents

modules


