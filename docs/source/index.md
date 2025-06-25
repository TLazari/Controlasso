created by  
sphinx-quickstart on Mon Jun 23 16:58:04 2025.  
contain the root `toctree` directive.

# Controlasso - Sistema de Gerenciamento Financeiro

```{toctree}
:maxdepth: 2
:caption: Contents

modules

```

# Documentação de Software

Este documento descreve a visão inicial do projeto **Controlasso**.

## 1. Integrantes e Título

- **Título do Projeto:** Controlasso
- **Integrantes:** Preencher com os nomes da equipe.

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

Esta documentação apresenta um panorama inicial do projeto Controlasso. O progresso das tarefas deve ser acompanhado via sprints, garantindo que cada ponto desta lista seja revisado e concluído.

# Guia Completo de Testes Django com Pytest

Este documento fornece um guia abrangente para o sistema de testes do projeto Django usando pytest.

## 🎯 Visão Geral

Este projeto utiliza pytest para testes, fornecendo:

- **Testes Unitários**: Testam componentes individuais
- **Cobertura de Código**: Relatórios detalhados de cobertura
- **Fixtures Reutilizáveis**: Para criação de dados de teste

## 📁 Estrutura dos Testes

```
core/tests/
├── conftest.py              # Configurações e fixtures globais
├── pytest.ini              # Configuração do pytest
├── test_models.py          # Testes dos modelos Django
├── test_views.py           # Testes das views
├── test_forms.py           # Testes dos formulários
├── test_urls.py            # Testes das URLs
```

## 🚀 Configuração e Instalação

### 1. Instalar Dependências

```bash
# Instalar dependências de teste
pip install -r requirements-test.txt

```

### 2. Configurar Banco de Dados

```bash
# Criar migrações (se necessário)
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate
```
## 🧪 Executando os Testes

```bash
# Executar todos os testes
pytest
```

## 📊 Tipos de Teste

### 1. Testes de Modelos (`test_models.py`)

Testam os modelos Django incluindo:

- ✅ Criação e validação de instâncias
- ✅ Relacionamentos entre modelos
- ✅ Métodos personalizados
- ✅ Validações e restrições
- ✅ Cenários de erro

### 2. Testes de Views (`test_views.py`)

Testam as views da aplicação:

- ✅ Autenticação e autorização
- ✅ Respostas HTTP corretas
- ✅ Contexto das templates
- ✅ Redirecionamentos
- ✅ Tratamento de erros

### 3. Testes de Formulários (`test_forms.py`)

Testam os formulários Django:

- ✅ Validação de campos
- ✅ Dados válidos e inválidos
- ✅ Classes CSS (Bootstrap)
- ✅ Segurança contra injeção
- ✅ Campos obrigatórios

### 4. Testes de URLs (`test_urls.py`)

Testam as configurações de URL:

- ✅ Mapeamento correto de URLs
- ✅ Parâmetros de URL
- ✅ Resolução de nomes de URL
- ✅ URLs alternativas

### 5. Testes de Integração (`test_integration.py`)

Testam fluxos completos:

- ✅ Fluxo de registro e login
- ✅ Processo completo de transferência
- ✅ Operações de compra e venda
- ✅ Interações entre múltiplos usuários

### 6. Testes de Performance (`test_performance.py`)

Testam performance e escalabilidade:

- ✅ Tempo de resposta das views
- ✅ Performance de consultas
- ✅ Operações em massa
- ✅ Uso de memória

## 🏭 Fixtures e Factories

### Fixtures Principais (`conftest.py`)

```python
@pytest.fixture
def user(user_factory):
    """Usuário de teste padrão."""
    return user_factory()

@pytest.fixture
def account(account_factory, user):
    """Conta de teste padrão."""
    return account_factory(user=user)

@pytest.fixture
def authenticated_client(client, user):
    """Cliente autenticado."""
    client.force_login(user)
    return client
```

### Factories Disponíveis

- `user_factory`: Cria usuários únicos
- `account_factory`: Cria contas bancárias
- `stock_factory`: Cria ações
- `trade_factory`: Cria operações de trade
- `transfer_factory`: Cria transferências
- `favorite_stock_factory`: Cria favoritos

### Métricas de Cobertura

- **Meta mínima**: 80%
- **Relatórios**: HTML e terminal
- **Exclusões**: Migrações, configurações

### Interpretando Relatórios

```bash
# Visualizar cobertura no terminal
pytest --cov=core --cov-report=term-missing

# Arquivos com baixa cobertura aparecem em vermelho
# Linhas não cobertas são listadas
```

## ✨ Boas Práticas

### 1. Nomenclatura de Testes

```python
# ✅ Bom: Nome descritivo
def test_transfer_with_insufficient_funds_should_raise_error(self):

# ❌ Ruim: Nome genérico
def test_transfer(self):
```

### 2. Organização de Testes

```python
class TestAccountModel:
    """Testes para o modelo Account."""
    
    def test_criacao_sucesso(self):
        """Testa criação bem-sucedida."""
        pass
    
    def test_validacao_campos(self):
        """Testa validação de campos."""
        pass
```

### 3. Uso de Fixtures

```python
# ✅ Usar fixtures para setup
def test_account_creation(self, user_factory):
    user = user_factory()
    # teste...

# ❌ Evitar setup manual repetitivo
def test_account_creation(self):
    user = User.objects.create(username='test')
    # teste...
```

### 4. Asserções Claras

```python
# ✅ Asserção específica
assert account.balance == Decimal('1000.00')

# ❌ Asserção vaga
assert account.balance
```

### 5. Testes Independentes

```python
# ✅ Cada teste é independente
def test_account_balance_update(self, account_factory):
    account = account_factory(balance=100.00)
    # teste isolado

# ❌ Dependência entre testes
def test_sequence_part_2(self):
    # depende do resultado do part_1
```

## 🐛 Resolução de Problemas

### Problemas Comuns

#### 1. Erro de Configuração Django

```bash
# Erro: django.core.exceptions.ImproperlyConfigured
# Solução: Definir DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE=core.settings
```

#### 2. Banco de Dados em Uso

```bash
# Erro: database is locked
# Solução: Usar banco em memória para testes
# Em settings de teste:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
```

#### 3. Falhas de Fixture

```bash
# Debug de fixture específica
pytest -v -s --setup-show

# Verificar dependências de fixture
pytest --fixtures
```

### Debug de Testes

```bash
# Saída mais detalhada
pytest -vvv --tb=long
```

### Performance de Testes

```bash
# Mostrar testes mais lentos
pytest --durations=10

```

## 🔧 Comandos Úteis


### Desenvolvimento de Novos Testes

```python
# Estrutura básica de teste
@pytest.mark.django_db
class TestNovoRecurso:
    """Testes para novo recurso."""
    
    def test_funcionalidade_basica(self, fixture_necessaria):
        """Testa funcionalidade básica."""
        # Arrange
        dados = setup_inicial()
        
        # Act
        resultado = executar_operacao(dados)
        
        # Assert
        assert resultado.status == 'success'
        assert resultado.valor == esperado
```

## 🎓 Conclusão

Este sistema de testes fornece:

- **Cobertura abrangente**
- **Relatórios detalhados** de cobertura e performance
- **Boas práticas** e padrões estabelecidos

Para dúvidas ou problemas específicos, consulte a documentação do pytest ou abra uma issue no projeto.

---

**Autor**: Matheus Maia  
**Versão**: 0.1  
**Data**: 2025-15-06