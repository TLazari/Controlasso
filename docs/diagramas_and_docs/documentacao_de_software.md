# Documentação de Software

Este documento descreve a visão inicial do projeto **Controlasso**.

## 1. Integrantes e Título

- **Título do Projeto:** Controlasso
- **Integrantes:** André Samouilian, Matheus Maia, Ruan Lucas, Rayza Anchayhua, Thiago Lazari
, 
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

### 4.3 Diagramas UML

- Diagrama de Caso de Uso
- Diagrama de Classes
- Diagrama de Atividades / Fluxograma


### 4.4 Cronograma de Desenvolvimento

Planejar sprints semanais contemplando as principais funcionalidades.

## 5. Resultado Esperado

Ao término do projeto, espera-se que o sistema ofereça todas as funcionalidades descritas nos requisitos, com autenticação robusta e dashboards informativos.

### 5.1 Papel no Scrum

- **Product Owner (PO)**: responsável por priorizar funcionalidades.
- **Scrum Master (SM)**: responsável por facilitar o processo Scrum.

### 5.2 Análise de Riscos

Risco 1: Falta de domínio em Django 
Causa: Pouca experiência da equipe com o framework. 
Consequência: Atrasos e retrabalho por decisões técnicas equivocadas. 

Risco 2: Integração fraca de front-end e back-end 
Causa: Comunicação deficiente entre as camadas do sistema. 
Consequência: Falta de informação nas páginas, dificuldade na navegação. 

Risco 3: Pouco tempo para testes 
Causa: Priorização do desenvolvimento e falta de testes para lançamento em produção. 
Consequência: Bugs em produção e baixa confiabilidade do sistema. 

Risco 4: Conflitos no versionamento de código 
Causa: Falta de disciplina no uso do Git. 
Consequência: Perda de código e falhas na integração. 

Risco 5: Interface pouco amigável 
Causa: Falta de foco em design e UX. 
Consequência: Má experiência do usuário e rejeição da ferramenta. 

Risco 6: Falhas de segurança na autenticação 
Causa: Implementação frágil ou mal validada. 
Consequência: Acesso indevido e comprometimento de dados. 

Risco 7: Falta de documentação técnica 
Causa: Priorização exclusiva no desenvolvimento funcional. 
Consequência: Dificuldade de manutenção e expansão futura. 

Risco 8: Sobreposição de tarefas entre membros 
Causa: Falta de definição de papéis claros. 
Consequência: Perda de tempo e retrabalho. 

Risco 9: Complexidade excessiva em funcionalidades simples 
Causa: Superengenharia. 
Consequência: Tempo desperdiçado e sistema difícil de manter.

Risco 10: Problemas com deploy (Railway, Render etc.) 
Causa: Configurações erradas ou instabilidade da plataforma. 
Consequência: Sistema fora do ar ou com falhas. 

Risco 11: APIs externas (ex: dados de ações) fora do ar 
Causa: Dependência de serviços de terceiros. 
Consequência: Funcionalidade quebrada ou desatualizada. 

Risco 12: Falta de validação dos dados de entrada 
Causa: Falhas nos formulários e na sanitização. 
Consequência: Erros de lógica, vulnerabilidades e falhas críticas. 

### Classificação e Análise Qualitativa 

| **Risco**                                               | **Probabilidade** | **Impacto** | **Prioridade** |
|---------------------------------------------------------|-------------------|-------------|----------------|
| Integração fraca de front-end e back-end                | Alta              | Média       | Alta           |
| APIs externas (ex: dados de ações) fora do ar           | Alta              | Alta        | Alta           |
| Complexidade excessiva em funcionalidades simples       | Baixa             | Média       | Baixa          |
| Problemas com deploy (Railway, Render etc.)             | Média             | Alta        | Alta           |
| Falta de documentação técnica                           | Alta              | Média       | Alta           |

### Plano de Resposta aos Riscos

| **Risco**                                | **Estratégia** | **Ação prática**                                                                                                  |
|------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| Integração fraca de front-end e back-end | Reduzir        | Definir escopo claro de interface, criar diagrama de classes, realizar reuniões semanais com entregas definidas. |
| APIs externas fora do ar                 | Aceitar        | Implementar fallback de cache local e utilizar múltiplas fontes de dados.                                        |
| Problemas com deploy (Railway, Render)   | Reduzir        | Usar hospedagem local como alternativa e avaliar ferramentas e planos de deploy.                                 |
| Falta de documentação técnica            | Evitar         | Estabelecer rotina de documentação ao final de cada sprint.                                                      |
| Pouco tempo para testes                  | Reduzir        | Planejar tempo exclusivo para testes em cada sprint com responsável designado.                                   |


### 5.3 Funcionalidade do Projeto

Sistema web para movimentação de contas e negociação de ações de forma simplificada.

## 6. Conclusão

Esta documentação apresenta um panorama inicial do projeto Controlasso. O progresso das tarefas deve ser acompanhado via sprints, garantindo que cada ponto desta lista seja revisado e concluído.

