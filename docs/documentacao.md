# Documentação de Software

Este documento descreve a visão inicial do projeto **CodexFinancial**.

## 1. Integrantes e Título

- **Título do Projeto:** CodexFinancial
- **Integrantes:** Preencher com os nomes da equipe.

## 2. Introdução

Sistema de gerenciamento de contas e negociação de ações, com dashboards de movimentações e carteira.

## 3. Definição do Projeto

### 3.1 Nome do Sistema

CodexFinancial

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

### 4.3 Diagramas UML

- Diagrama de Caso de Uso
- Diagrama de Classes
- Diagrama de Atividades / Fluxograma

*(Os diagramas devem ser elaborados em ferramenta apropriada e adicionados ao repositório quando disponíveis.)*

### 4.4 Cronograma de Desenvolvimento

Planejar sprints semanais contemplando as principais funcionalidades.

## 5. Resultado Esperado

Ao término do projeto, espera-se que o sistema ofereça todas as funcionalidades descritas nos requisitos, com autenticação robusta e dashboards informativos.

### 5.1 Papel no Scrum

- **Product Owner (PO)**: responsável por priorizar funcionalidades.
- **Scrum Master (SM)**: responsável por facilitar o processo Scrum.

### 5.2 Análise de Riscos

Identificar riscos técnicos (falhas na integração), humanos (falta de recursos), de cronograma e financeiros. Definir planos de mitigação.

### 5.3 Funcionalidade do Projeto

Sistema web para movimentação de contas e negociação de ações de forma simplificada.

## 6. Conclusão

Esta documentação apresenta um panorama inicial do projeto CodexFinancial. O progresso das tarefas deve ser acompanhado via sprints, garantindo que cada ponto desta lista seja revisado e concluído.

